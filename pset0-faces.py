def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def Main():
    word = input ("Give me a sentence ")
    print(convert(word))

Main()

