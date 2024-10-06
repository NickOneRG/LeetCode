

def missingCharacters(s):
    memo = []
    for i in range(10):
        i = str(i)
        if i not in s:
            memo.append(i)

    for i in range(26):
        if (i := chr(i+97)) not in s:
            memo.append(i)

    return ''.join(memo)


def transformSentence(sentence):
    memo = [sentence[0]]
    for i in range(1, len(sentence)):
        if sentence[i-1] == ' ' or sentence[i] == ' ':
            memo.append(sentence[i])
        else:
            if (a := ord(sentence[i].lower())) > (b := ord(sentence[i-1].lower())):
                memo.append(sentence[i].upper())
            elif a == b:
                memo.append(sentence[i])
            else:
                memo.append(sentence[i].lower())

    return "".join(memo)



if __name__ == '__main__':
    print(missingCharacters("kadknk6484sd6"))
    print(transformSentence("a Blue MOON"))
