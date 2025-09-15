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

def count_vowels(word):
    '''
    counts vowels in a given word
    Args:
        word (str): the given word
    Returns:
        return: count of vowels
    '''
    count=0
    for character in word:
        if character in ['a','e','i','o','u']:
            count +=1
    return count

def first_name(fullname):
    names = fullname.split(' ')
    first_name = names[0]
    return first_name













def main():
    fullname = input("enter your full name:")
    while True:
            option = input(str.lower("""enter the number of the action you would like to do!
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
                a, b = get_integers()
                print("I will add together these 2 numbers")
                add(a, b)
            elif option == "3":
                colors = ['red','white','blue']
                print_list(colors)
            elif option == "4":
                print(f"your first name is {first_name(fullname)}")
            elif option == "5":
                print(is_integer('2'))
                print(is_integer('yellow'))
            elif option == "6":
                print("I will give you a number inbetween them")
                get_random()
            elif option == "7":
                word=input("enter a word: ")
                print(f"the number of vowels in your word was..{count_vowels(word)}")
            elif option == "8":
                word=input("enter a word: ")
                print(reverse_string(word))
            elif option == "9":
                word=input("enter a word: ")
                print(is_palindrome(word))
            elif option == "10":
                fullname = input("enter your full name:")
                print(get_initials(fullname))
            elif option == "11":
                print(replace_character("hello world","l","j"))
            elif option == "12":
                print("I will give you a number inbetween them")
                get_random()
            elif option == "13":
                word=input("enter a word: ")
                print(f"the number of vowels in your word was..{count_vowels(word)}")
            elif option == "14":
                word=input("enter a word: ")
                print(reverse_string(word))
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