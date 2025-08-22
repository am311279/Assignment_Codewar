#Solution: 1.Even or Odd
def even_or_odd(number):
    #Check if number is divisible by 2.
    #If the remainder is zero, the number is even.
    #If it is not, the number is odd
    if number%2==0:
        return "Even"
    else:
        return "Odd"

#Soultion: 2.Convert a Number to a String  
def number_to_string(num):
    #convert num to string and return
    return str(num)

#Solution: 3.Remove String Spaces
def no_space(x):
    new_x = "".join(x.split())
    return new_x

#Solution: 4.Vowel Count
def get_count(sentence):
    number_of_vowel = 0 #variable to track the number of vowels
    vowels = ['a', 'e', 'i', 'o', 'u'] #array that contains the vowels
    for x in vowels: #loop each vowels array entry to check if the vowels are in the sentence 
        for y in sentence:
            if x == y:
                number_of_vowel += 1 #increment the number_of_vowel by 1 if the vowel is in the sentence
    return number_of_vowel