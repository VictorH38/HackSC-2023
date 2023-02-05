import openai

openai.api_key = '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'

def generate(prompt):
    response = openai.Completion.create(
        model='text-davinci-003',
            prompt=prompt,
            temperature=0.2,
            max_tokens=600,
            top_p=1.0,
            frequency_penalty=0.3,
            presence_penalty=0.3
    )

    return response.choices[0].text

class Personality:
    def __init__(self, name):
        self.name = name
        self.qualities = []
        self.journal_entries = []
        self.prevText = []
        self.personalityDescription = ""

    def addQuality(self, quality):
        self.qualities.append(quality)

    def addEntry(self, entry):
        self.journal_entries.append(entry)

    def generatePersonalityDesc(self):
        qualities = '\n'.join(self.qualities)
        journal_entries = '\n'.join(self.journal_entries)
        prompt =  f"""
You are going to write a detailed description of a person based on general characteristics of this person and a collection of personal diary entries that this person wrote.
This person has the following qualities and characteristics:
{qualities}
The person wrote the following things in their personal journal:
{journal_entries}
Write a detailed description of this using these information.
"""
        self.personalityDescription = generate(prompt)
        
    
    def generateChatPrompt(self, personality, memory):
        prompt = f"""
You are acting as a person with the following description: {personality}
        
Conversation so far:
{memory}

Reply to this conversation acting as the person described by the description.
"""
        return prompt

    def generateMemory(self, prevText, username, identityName):
        memory = ""
        talkers = [username, identityName]
        idx = 0
        for text in prevText[-5:]:
            talker = talkers[(idx)%2]
            idx += 1
            memory += (talker + ": ")
            memory += (text + '\n\n')
            #print(memory)
        
        return memory


    def ask(self):
        inputText = input()
        self.prevText.append(inputText)

    def talk(self, username):
        memory = self.generateMemory(self.prevText, username, self.name)
        prompt = self.generateChatPrompt(self.personalityDescription, memory)
        # print(prompt)
        outputText = generate(prompt)
        self.prevText.append(outputText)
        print(outputText)

