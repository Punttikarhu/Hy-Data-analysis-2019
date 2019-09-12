#!/usr/bin/env python3

def word_frequencies(filename):
    D = {}
    with open(filename) as f:
        words = f.read().split()
        words = list(map(lambda word: word.strip("""!"#$%&'()*,-./:;?@[]_'"""), words))
#        words = list(filter(lambda word: word is not '', words))

        setWords = set(words)

        for word in setWords:
            counter = 0
            for word2 in words:
                if word2 == word:
                    counter = counter + 1
            D[word] = counter
    return D



        #print(words)



    return {}

def main():
    word_frequencies('alice.txt')

if __name__ == "__main__":
    main()
