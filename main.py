# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import json
import time

def NewGame(UserKey, URL):
    ngurl = URL + "/new/"
    userjson = {'userkey': UserKey}
    return requests.post(ngurl, json=userjson)

def guessLetter(data, letter):
    gameurl = data.json()['url']
    letterjson = {'userkey': UserKey, 'letter': letter}
    gameurl = gameurl + "&type=letter"
    return requests.post(gameurl, json=letterjson)

def guessWord(data, word):
    gameurl = data.json()['url']
    wordjson = {'userkey': UserKey, 'word': word}
    gameurl = gameurl + "&type=word"
    return requests.post(gameurl, json=wordjson)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    UserKey = "7zTv9DMMfqPS6nMurJZEr5CQw5gEHGDe"
    URL = "https://hangman.timothyoesch.ch"
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    guesses_dict = []
    guesses_lst = []
    raw = NewGame(UserKey, URL)
    first = raw.json()
    wordlen = len(first['clue'])
    pos_words = []
    word_file = open("words.txt", "r")
    for line in word_file:
        if wordlen == len(line.rstrip()):
            # print(line.rstrip())
            pos_words.append(line.rstrip())
    i = 1
    while i <= 5:
        freq = []
        for letter in alphabet:
            num = 0
            for word in pos_words:
                if letter in word:
                    num += 1
            freq.append(num)
        curlet = alphabet[freq.index(max(freq))]
        save = guessLetter(raw, curlet).json()
        if save['clue'].find('*') == -1:
            break
        if save['status'] == 'strike':
            i += 1
            for word in pos_words:
                if curlet in word:
                    pos_words.remove(word)
        if save['status'] == 'correctletter':
            for word in pos_words:
                if curlet not in word:
                    pos_words.remove(word)
        print(save)
        alphabet.remove(curlet)
    time.sleep(2)
    print(pos_words)
    fin = []
    check = save['clue']
    for word in pos_words:
        auxboollist = []
        for i, let in enumerate(word):
            if check[i] == "*":
                continue
            elif let != check[i]:
                auxboollist.append("f")
        if "f" not in auxboollist:
            fin.append(word)

    print(guessWord(raw, fin[0]).json())





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
