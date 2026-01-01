word = "Artifical Intelligence and Machine Learning"
count = 0
for var in word:
    if(var == "a" or var == "e" or var == "i" or var == "o" or var == "u" or
       var == "A" or var == "E" or var == "I" or var == "O" or var == "U" ):
        print("It is in Vowel", var)
        count +=1