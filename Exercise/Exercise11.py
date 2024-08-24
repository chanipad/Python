'''
Defined the same ranking
create a program that:
1. Contains the above list
2. Prompts the user to input the person's name
3. Return the rank that person has.
For example:
Enter a name: Sen
2
'''

ranking = ['John', 'Sen', 'Lisa']


input_name = input("Enter a name: ")
match ranking:
    case 'John':
        print("1")
    case 'Sen':
        print("2")
    case 'Lisa':
        print("3")