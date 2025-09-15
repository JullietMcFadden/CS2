#flowerbox

def reverse_name(name):
    pass

def get_initials(fullname):
    '''
    takes a name and gets the initials
    Args:
        fullname (str): the given name
    Returns:
        returns: the initials
    '''
    names = fullname.split(' ')
    initials = ''
    for name in names:
        initials += name[0]
    return initials


def reverse_string(word):
    '''
    reserves a string
    Args:
        word (str): the given word
    Returns:
        return: the reserved string
    '''
    return word[::-1]

def count_vowels(fullname):
    '''
    counts vowels in a given word
    Args:
        word (str): the given word
    Returns:
        return: count of vowels
    '''
    a,e,i,o,u = 0
    for character in fullname:
        if character == "a":
            a+= 1
        if character == "e":
            e+= 1
        if character == "i":
            i+= 1
        if character == "o":
            o+= 1
        if character == "u":
            u+= 1
        print(f'there are {a} a(s),{e} e(s),{i} i(s),{o} o(s),{u} u(s)')

def first_name(fullname):
    names = fullname.split(' ')
    first_name = names[0]
    return first_name

def last_name(fullname):
    names = fullname.split(' ')
    last_name = names[-1]
    return last_name

def middle_names(fullname):
    names = fullname.split(' ')
    del names[0]
    del names[-1]
    
    if len(names) > 1:
        middle_names = ''.join(names)
    else:
        middle_names = names[0]
    return middle_names

def hyphen(fullname):
    return "-" in last_name(fullname)

def title_name(fullname):
    if ["Dr.", "Sir", "Ph.d", "Esq"] in last_name(fullname):
        return True
    else:
        return False

def is_palindrome(first_name):
    return reverse_string(first_name) == first_name

def make_lower(fullname):
    name_out= ""
    for letter in fullname:
        if ord(letter)>64 and ord(letter)<91:
            num=ord(letter)
            num=num+32
            letter= chr(num)
            name_out = name_out +  letter
        else:
            name_out = name_out +  letter
    fullname = name_out
    return fullname
        
def make_upper(fullname):
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
12. Check full name
13. Get your initials
14. Do you have a title?
15. ect
Q. quit
"""))
            if option == "1":
                print(reverse_string(fullname))
            elif option == "2":
                count_vowels(fullname)
            elif option == "3":
                colors = ['red','white','blue']
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
                fullname = input("enter your full name:")
                print(get_initials(fullname))

                #print(replace_character("hello world","l","j"))
            elif option == "12":
                print("I will give you a number inbetween them")
                #get_random()
                pass
            elif option == "13":
                word=input("enter a word: ")
                print(f"the number of vowels in your word was..{count_vowels(word)}")
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