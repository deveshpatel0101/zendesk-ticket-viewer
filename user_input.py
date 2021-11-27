from display_data import display_error
from colorama import init, Fore
from termcolor import colored
init(autoreset=True)


def get_user_input(prev_input):
    if prev_input is None or prev_input == 'GET_ID':
        print('* Enter ' + Fore.CYAN + "'1'" + Fore.RESET + ' to view tickets')
        print('* Enter ' + Fore.CYAN + "'2'" + Fore.RESET + ' to view a ticket by ID')
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

    print('* Enter ' + Fore.CYAN + "'1'" + Fore.RESET + ' for previous page')
    print('* Enter ' + Fore.CYAN + "'2'" + Fore.RESET + ' for next page')
    print('* Enter ' + Fore.CYAN + "'3'" + Fore.RESET + ' to get a ticket by ID')
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


def is_valid_input(user_input, curr_page, has_more):
    if curr_page <= 1 and user_input == 'PREV':
        display_error('YOU ARE ALREADY ON FIRST PAGE')
        return False
    elif not has_more and user_input == 'NEXT':
        display_error('NO MORE TICKETS TO SHOW')
        return False

    return True


def get_input(text):
    return input(text)
