#Initialize counters
char_count=0
word_count=0
vowel_count=0

#Define vowels
vowels="aeiouAEIOU"
#Reas sentence fron user
sentence = input("Enter a sentence ending with a period:")
# Process each character
for i in range(len(sentence)):
    char = sentence[i]
    char_count +=1

    #Count vowels
    if char in vowels:
        vowel_count += 1
        #Count words based on space
        if char =='':
            word_count += 1
            #add one to word count to account for the last word before the period 
            if sentence.endswitch('.'):
                word_count += 1
                #Dsisplay results 
                print("Length of the sentence:", char_count)
                print("Number of words:", word_count)
                print("Number of vowels:", vowel_count)