def display_tickets(tickets):
    if len(tickets) == 0:
        print('==========================================')
        print("NO TICKETS TO DISPLAY")
        print('==========================================')
    for index, ticket in enumerate(tickets):
        display_ticket(ticket, index+1)


def display_ticket(ticket, number):
    print('==========================================')
    print(f'{number}.')
    print(f'ID: {ticket["id"]}')
    print(f'SUBJECT: {ticket["subject"]}')
    print(f'DESCRIPTION: {ticket["description"][:50]}...')
    print(f'PRIORITY: {ticket["priority"]}')
    print(f'STATUS: {ticket["status"]}')
    print('==========================================')


def display_error(error):
    print('==========================================')
    print('ERROR OCCURRED!')
    print(str(error))
    print('==========================================')


def get_user_input(curr_page, has_more, prev_input):
    if prev_input is None or prev_input == 'GET_ID':
        while True:
            print('1. GET TICKETS')
            print('2. GET TICKET BY ID')
            print('9. EXIT')
            user_input = input('Enter your choice: ')
            if user_input == '1':
                return 'GET_ALL'
            elif user_input == '2':
                return 'GET_ID'
            elif user_input == '9':
                return 'EXIT'
            else:
                print('==========================================')
                print(f'Input not recognized. Please enter a number from 1/2/9.')
                print('==========================================')

    while True:
        index = 1
        if curr_page != 1:
            print(f'{index}. PREV PAGE')
            index += 1

        if has_more:
            print(f'{index}. NEXT PAGE')
            index += 1
        print(f'{index}. GET BY ID')
        print('9. EXIT')
        user_input = input('Enter your choice: ')

        if user_input == '1' and curr_page != 1:
            return 'PREV'
        elif user_input == '1' and curr_page == 1 and has_more:
            return 'NEXT'
        elif user_input == '1' and curr_page == 1 and not has_more:
            return 'GET_ID'
        elif user_input == '2' and curr_page != 1 and has_more:
            return 'NEXT'
        elif user_input == '2' and curr_page != 1 and not has_more:
            return 'GET_ID'
        elif user_input == '3' and index == 3:
            return 'GET_ID'
        elif user_input == '9':
            return 'EXIT'
        else:
            user_choices = [str(index) for index in range(1, index+1)]
            user_choices.append('9')
            print('==========================================')
            print(f'Input not recognized. Please enter a number from {"/".join(user_choices)}.')
            print('==========================================')
