letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
letters = letters.split(" ")
sentence = input()
for i in range(len(sentence)):
    if sentence[i].lower() in letters:
        letters.remove(sentence[i].lower())
if len(letters) == 0:
    print("Pangram")
else:
    print("Not a pangram")