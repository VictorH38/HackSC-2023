import openai
from personality import Personality

openai.api_key = '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'

qualities = ""
journal_entries = ""

qualitiesList = ['moody', 'lashes out to close people', 'often cries']
journalList = ['Today I had a bad day', "today was not too bad, I actually felt good but I feel like my roommate thinks I'm dirty"]


qualities = '\n'.join(qualitiesList)
journal_entries = '\n'.join(journalList)

print(qualities, journal_entries)

prompt =  f"""
You are going to write a detailed description of a person based on general characteristics of this person and a collection of personal diary entries that this person wrote.

This person has the following qualities and characteristics:
{qualities}

The person wrote the following things in their personal journal:
{journal_entries}

Write a detailed description of this using these information.
"""

print(prompt)


def generate(prompt):
    response = openai.Completion.create(
        model='text-davinci-003',
            prompt=prompt,
            temperature=0.3,
            max_tokens=600,
            top_p=1.0,
            frequency_penalty=0,
            presence_penalty=0
    )

    return response.choices[0].text

def generateChatPrompt(personality, memory):
    prompt = f"""You are acting as a person with the following description: {personality}
    
Conversation so far:
{memory}

Reply to this conversation acting as the person described by the description.

"""
    return prompt

def generateMemory(prevText, username, identityName):
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

# personalityDescription = generate(prompt)
# print(personalityDescription)
personalityDescription = "This person is a complex individual who is often moody and unpredictable. They can lash out to people close to them and are prone to bouts of crying. They often feel misunderstood and can be hard to read. In their personal diary entries, they express a range of emotions from feeling good to feeling like their roommate thinks they are dirty. This person is likely to be a deep thinker, who is constantly reflecting on their life and the world around them. They are likely to be a sensitive soul, who is easily hurt by the words and actions of others. They are likely to be a passionate person, who is driven by their emotions and feelings."

inputText = ""
prevText = []

username = "Mark"
identityname = "Marky Sparky"

markyIdentity = Personality()

while inputText != 'q':
    inputText = input()
    prevText.append(inputText)
    #print(prevText)

    memory = generateMemory(prevText, username, identityname)
    prompt = generateChatPrompt(personalityDescription, memory)
    #print(prompt)
    outputText = generate(prompt)
    prevText.append(outputText)
    print(outputText)
    
