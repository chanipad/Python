ranking = ['John', 'Sen', 'Lisa']

rank_number = input("Enter rank number: ")

match rank_number:
    case '1':
        print(ranking[0])
    case '2':
        print(ranking[1])
    case '3':
        print(ranking[2])