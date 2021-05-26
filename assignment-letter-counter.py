def letter_counter(sentence) :
    letter_dict = {}

    for i in sentence :
        if i in letter_dict :
            letter_dict[i] += 1

        else :
            letter_dict[i] = 1

    return letter_dict


sentence = input("Please enter a sentence : ")

print(letter_counter(sentence))