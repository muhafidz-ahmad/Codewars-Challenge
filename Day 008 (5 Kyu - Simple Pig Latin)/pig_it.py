import string

def pig_it(text):
    new_text = []
    for word in text.split(" "):
        if word not in string.punctuation:
            new_text.append(word[1:] + word[0] + "ay")
        else:
            new_text.append(word)
    return " ".join(new_text)