'''
Extend the code do the program prints out the follwing out of that lis:
0-Document.txt
1-Report.txt
2-Presentation.txt
'''

filenames = ['document', 'report', 'presentation']

file_list = ""

for i, j in enumerate(filenames):
    file_list += f"{i}-{j.capitalize()}.txt\n" # If use only = oparetor will get only 2-Presentation.txt that why using +=
'''    print(file_list)  # If directly use print(file_list) here will get
0-Document.txt

0-Document.txt
1-Report.txt

0-Document.txt
1-Report.txt
2-Presentation.txt'''

# For geting the right answer is to print outside the loop
print(file_list)