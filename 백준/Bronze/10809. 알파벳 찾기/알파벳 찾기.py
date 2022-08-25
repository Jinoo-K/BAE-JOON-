word = input()

abc = list(range(97,123))

for i in abc :
    print(word.find(chr(i)), end=" ")