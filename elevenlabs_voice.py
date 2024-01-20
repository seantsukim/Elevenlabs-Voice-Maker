# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import elevenlabs

audio = elevenlabs.generate(
    text = "My name is Charlotte and I am the elevenlabs model speaking",
    voice = "Charlotte",
    model = "eleven_multilingual_v1"
)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    elevenlabs.play(audio)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
