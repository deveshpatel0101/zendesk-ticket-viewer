from display_data import display_error
from colorama import init, Fore
init(autoreset=True)


def get_user_input(curr_page):
    '''
    Gets the user input based on which page is currently displayed\n
    returns either of [None, 'GET_ALL', 'GET_ID', 'PREV', 'NEXT', 'EXIT']
    '''
    if curr_page <= 0:
        print('* Enter ' + Fore.CYAN + "'1'" + Fore.RESET + ' to view tickets')
        print('* Enter ' + Fore.CYAN + "'2'" +
              Fore.RESET + ' to view a ticket by ID')
        print('* Enter ' + Fore.CYAN + "'9'" + Fore.RESET + ' to quit')
        user_input = get_input('Enter your choice: ')
        if user_input == '1':
            return 'GET_ALL'
        elif user_input == '2':
            return 'GET_ID'
        elif user_input == '9':
            return 'EXIT'
        else:
            display_error(
                Exception('Input not recognized. Please enter a number from 1/2/9.'))
            return

    if curr_page == 1:
        print('* Enter ' + Fore.CYAN + "'1'" + Fore.RESET + ' for next page')
        print('* Enter ' + Fore.CYAN + "'2'" +
              Fore.RESET + ' to view a ticket by ID')
        print('* Enter ' + Fore.CYAN + "'9'" + Fore.RESET + ' to quit')
        user_input = get_input('Enter your choice: ')
        if user_input == '1':
            return 'NEXT'
        elif user_input == '2':
            return 'GET_ID'
        elif user_input == '9':
            return 'EXIT'
        else:
            display_error(
                Exception('Input not recognized. Please enter a number from 1/2/9.'))
            return

    print('* Enter ' + Fore.CYAN + "'1'" + Fore.RESET + ' for previous page')
    print('* Enter ' + Fore.CYAN + "'2'" + Fore.RESET + ' for next page')
    print('* Enter ' + Fore.CYAN + "'3'" +
          Fore.RESET + ' to get a ticket by ID')
    print('* Enter ' + Fore.CYAN + "'9'" + Fore.RESET + ' to quit')
    user_input = get_input('Enter your choice: ')

    if user_input == '1':
        return 'PREV'
    elif user_input == '2':
        return 'NEXT'
    elif user_input == '3':
        return 'GET_ID'
    elif user_input == '9':
        return 'EXIT'
    else:
        display_error(
            'Input not recognized. Please enter a number from 1/2/3/9.')


def get_input(text):
    '''
    Reads user input
    '''
    return input(text)
