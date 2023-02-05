from personality import Personality


markysparky = Personality('markysparky')

print("Enter some qualities/characteristics about this identity and press 'q' when done:")
quality = ''
while quality != 'q':
    quality = input()
    markysparky.addQuality(quality)

print("Enter some diary entries and press 'q' when done:")
entry = ''
while entry != 'q':
    entry = input()
    markysparky.addEntry(entry)

markysparky.generatePersonalityDesc()

print("Start talking to " + markysparky.name + "!")
userText = ''
while userText != 'q':
    markysparky.ask()
    markysparky.talk('sean')

