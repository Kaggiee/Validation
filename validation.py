def main():
    """
    This function will declare the variable test_acct and initialize it as an empty string so
    that it can be initialized later in the input and if-else loop. First, it will open the
    designated .txt file and read the lines and length, then ask for user input for a number.
    The file will close and an if-else loop will check if the number is in the text file.
    If it is, it will return an affirmative line. If not, it will say invalid. If the text
    file chosen is not available in the directory, the program will give an error explaining
    the file can't be found.
    """
    test_acct = ''

    try:
        infile = open('7-2-accounts.txt', 'r', encoding='UTF-8')
        account_list = infile.readlines()
        for num in range(len(account_list)):
            account_list[num] = account_list[num].rstrip('\n')
        test_acct = (input('Enter the account number to be validated: '))
        infile.close()
        if test_acct in account_list:
            print(f'Account number {test_acct} is valid.')
        else:
            print(f'Account number {test_acct} is not valid.')
    except IOError:
        print("The file can't be found")

# Call the main function.
if __name__ == '__main__':
    main()
