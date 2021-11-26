from display_data import display_error


def get_user_input(prev_input):
    if prev_input is None or prev_input == 'GET_ID':
        print('1. GET TICKETS')
        print('2. GET TICKET BY ID')
        print('9. EXIT')
        user_input = get_input('Enter your choice: ')
        if user_input == '1':
            return 'GET_ALL'
        elif user_input == '2':
            return 'GET_ID'
        elif user_input == '9':
            return 'EXIT'
        else:
            display_error(Exception('Input not recognized. Please enter a number from 1/2/9.'))
            return

    print('1. PREV PAGE')
    print('2. NEXT PAGE')
    print('3. GET BY ID')
    print('9. EXIT')
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
        display_error('Input not recognized. Please enter a number from 1/2/3/9.')


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
