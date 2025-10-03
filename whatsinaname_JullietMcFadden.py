#flowerbox

import random

def get_initials(fullname):
    '''
    takes a name and gets the initials
    Args:
        fullname (str): the given name
    Returns:
        returns: the initials
    '''
    names = fullname.split(' ')                                 #split the string when there is a space
    initials = ''                                               #create a variable for initials
    for name in names:                                          #for the the names in the names list 
        initials += name[0]                                     #add the first item [0] of each name to the initials list
    return initials                                             #return the initials variable


def reverse_string(word):
    '''
    reserves a string
    Args:
        word (str): the given word
    Returns:
        return: the reserved string
    '''
    return word[::-1]                                           #read the str in the backwards direction(-1)

def count_vowels(vowels, fullname):
    '''
    counts vowels in a given word
    Args:
        word (str): the given word
        vowels (list): empty list of values that store counts of each vowel
    Returns:
        return: count of vowels
    '''
    fullname = make_lower(fullname)                             #make fullname lowercase using lowecase function
    for character in fullname:                                  #for each character in name
        if character == "a":                                    #if current character is a
            vowels[0]+= 1                                       #add 1 to the vowel counter at corresponding index
        if character == "e":
            vowels[1]+= 1
        if character == "i":
            vowels[2]+= 1
        if character == "o":
            vowels[3]+= 1
        if character == "u":
            vowels[4]+= 1
        else:                                                   #if name doesnt equal any vowel letters
            pass                                                #move onto next character
    return vowels                                               #return vowels variable

def count_consonant(cons, fullname):
    '''
    counts constants in a given word
    Args:
        word (str): the given word
        cons (list): empty list of values that store counts of each constant
    Returns:
        return: count of constants
    '''
    fullname = make_lower(fullname)
    for character in fullname:
        if character == "b":
            cons[0]+= 1
        if character == "c":
            cons[1]+= 1
        if character == "d":
            cons[2]+= 1
        if character == "f":
            cons[3]+= 1
        if character == "g":
            cons[4]+= 1
        if character == "h":
            cons[5]+= 1
        if character == "j":
            cons[6]+= 1
        if character == "k":
            cons[7]+= 1
        if character == "l":
            cons[8]+= 1
        if character == "m":
            cons[9]+= 1
        if character == "n":
            cons[10]+= 1
        if character == "p":
            cons[11]+= 1
        if character == "q":
            cons[12]+= 1
        if character == "r":
            cons[13]+= 1
        if character == "s":
            cons[14]+= 1
        if character == "t":
            cons[15]+= 1
        if character == "v":
            cons[16]+= 1
        if character == "w":
            cons[17]+= 1
        if character == "x":
            cons[18]+= 1
        if character == "y":
            cons[19]+= 1
        if character == "z":
            cons[20]+= 1
        else:                                                   #if name doesnt equal any vowel letters
            pass                                                #move onto next character
    return cons                                                 #return vowels constants
    
def mix_up(fullname):
    '''
    Function description
    Args:
        parameter names (types): context
    Returns:
        output type: context
    Extraneous (Raises etc.):
        description: context
    '''
    letters = list(fullname)                                    #make the list letters into a list of every letter in fullname
    random.shuffle(letters)                                     #randomly shuffle the list of letters
    return "".join(letters)                                     #join the mixed up name and return it

def first_name(fullname):
    '''
    Function description
    Args:
        parameter names (types): context
    Returns:
        output type: context
    Extraneous (Raises etc.):
        description: context
    '''
    names = fullname.split(' ')                                 #split the fullname when there is a space and put into the list names
    first_name = names[0]                                       #set the variable first name to the first item in the names list
    return first_name                                           #return variable first name

def last_name(fullname):
    '''
    Function description
    Args:
        parameter names (types): context
    Returns:
        output type: context
    Extraneous (Raises etc.):
        description: context
    '''                                        
    names = fullname.split(' ')                                 #split the fullname when there is a space and put into the list names
    last_name = names[-1]                                       #set the variable last name to the last item in the names list
    return last_name                                            #return variable last name

def middle_names(fullname):
    '''
    Function description
    Args:
        parameter names (types): context
    Returns:
        output type: context
    Extraneous (Raises etc.):
        description: context
    '''
    names = fullname.split(' ')                                 #split the fullname when there is a space and put into the list names
    del names[0]                                                #delete the first item in the list names
    del names[-1]                                               #delete the last item in the list names
    
    if len(names) > 1:                                          #if the length of names is greater then 1
        middle_names = ''.join(names)                           #join the middle names in the list together to a make a string
    if len(names) == 0:
        print("You have no middle name")
    else:                                                       
        middle_names = names[0]                                 #set middle names to the first value in the list
    return middle_names                                         #return middle_name 

def hyphen(fullname):
    '''
    Function description
    Args:
        parameter names (types): context
    Returns:
        output type: context
    Extraneous (Raises etc.):
        description: context
    '''
    return "-" in last_name(fullname)

def title_name(fullname):
    '''
    Function description
    Args:
        parameter names (types): context
    Returns:
        output type: context
    Extraneous (Raises etc.):
        description: context
    '''
    titles = ["Dr","Sir","Ph.d","Esq","Lady","Mr","Mrs","Ms","Miss"]
    for title in titles:
        if title in fullname:
            return True
        else:
            return False

def is_palindrome(first_name):
    '''
    Function description
    Args:
        parameter names (types): context
    Returns:
        output type: context
    Extraneous (Raises etc.):
        description: context
    '''
    return reverse_string(first_name) == first_name

def make_lower(fullname):
    '''
    Function description
    Args:
        parameter names (types): context
    Returns:
        output type: context
    Extraneous (Raises etc.):
        description: context
    '''
    name_out= ""
    for letter in fullname:
        if ord(letter)>64 and ord(letter)<91:                   #takes ordinal number from ascii table to see if its the range within the part of the table where the lowercase letters are
            num=ord(letter)                                     #
            num=num+32                                          #
            letter= chr(num)                                    #
            name_out = name_out +  letter                       #add newley changed letter to end of name so far
        else:
            name_out = name_out +  letter                       #keep letter as is and currents letter to end of name so far
    fullname = name_out
    return fullname
        
def make_upper(fullname):
    '''
    Function description
    Args:
        parameter names (types): context
    Returns:
        output type: context
    Extraneous (Raises etc.):
        description: context
    '''
    name_out= ""
    for letter in fullname:
        if ord(letter)>96 and ord(letter)<123:
            num=ord(letter)
            num=num-32
            letter= chr(num)
            name_out = name_out  + letter
        else:
            name_out = name_out +  letter
    fullname = name_out
    return fullname

def sort_name(fullname):
    '''
    Function description
    Args:
        parameter names (types): context
    Returns:
        output type: context
    Extraneous (Raises etc.):
        description: context
    '''
    arr = first_name(fullname)
    n = len(arr)                                                # Outer loop for each pass
    for i in range(n - 1):
                                                                # Inner loop to compare adjacent elements and swap them
                                                                # The range decreases with each pass because the largest elements
                                                                # are already in their correct positions at the end of the array.
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                                                                # Swap elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    #print (arr)
    return arr

# Example usage:
    #my_list = [64, 34, 25, 12, 22, 11, 90]
    #sorted_list = bubble_sort(my_list)
    #print(f"Sorted array: {sorted_list}")
    #name = first_name(fullname)
    #swapped = " "
    #for letters in name(len(name)-1):
    #swapped = False
    #for j in range(n-i-1):
    #    if name[j] > name[j+1]:
    #    name[j], name[j+1] = name[j+1], name[j]
    #    swapped = True
    #if not swapped:
    #    break
    #return name

        
def main():
    fullname = input("enter your full name:")
    while True:
            option = input(str("""enter the number of the action you would like to do!
1. Reverse string
2. Count vowels
3. Count constants
4. Check first name
5. Check last name 
6. Cheeck middle name(s)
7. Does last name have hyphen?
8. Make string lowercase
9. Make string uppercase
10. Mix up your name
11. Is your first name a palindrome?
12. Check full name in order
13. Get your initials
14. Do you have a title?
15. ect
Q. quit
"""))
            if option == "1":
                print(reverse_string(fullname))
            elif option == "2":
                vowels= [0,0,0,0,0]
                vowels = count_vowels(vowels, fullname)
                print(vowels[0])
                print(f"there are {vowels[0]} a'(s),{vowels[1]} e'(s),{vowels[2]} i'(s),{vowels[3]} o'(s),{vowels[4]} u'(s)")
            elif option == "3":
                cons= [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                cons = count_consonant(cons, fullname)
                print(f"there are {cons[0]} b'(s),{cons[1]} c'(s),{cons[2]} d'(s),{cons[3]} f'(s),{cons[4]} g'(s),{cons[5]} h'(s),{cons[6]} j'(s),{cons[7]} k'(s),{cons[8]} l'(s),{cons[9]} m'(s),{cons[10]} n'(s),{cons[11]} p'(s),{cons[12]} q'(s),{cons[13]} r'(s),{cons[14]} s'(s),{cons[15]} t'(s),{cons[16]} v'(s),{cons[17]} w'(s),{cons[18]} x'(s),{cons[19]} y'(s),{cons[20]} z'(s)")
            elif option == "4":
                print(f"your first name is {first_name(fullname)}")
            elif option == "5":
                print(f"your last name is {last_name(fullname)}")
            elif option == "6":
                print(f"your middle name(s) are {middle_names(fullname)}")
            elif option == "7":
                print(hyphen(fullname))
            elif option == "8":
                print(make_lower(fullname))
            elif option == "9":
                print(make_upper(fullname))
            elif option == "11":
                print(is_palindrome(fullname))
            elif option == "10":
                print(mix_up(fullname))
            elif option == "12":
                print(sort_name(fullname))
            elif option == "13":
                print(get_initials(fullname))
            elif option == "14":
                print(title_name(fullname))
            elif option == "15":
                word=input("enter a word: ")
                print(is_palindrome(word))
            elif option == "16":
                fullname = input("enter your full name:")
                print(get_initials(fullname))
            elif option == "17":
                print("hi")
            elif option == "q":
                break
            else:
                print("not an option")

main()
