from tickets import get_tickets, get_ticket
from display_data import display_error, display_tickets, display_ticket
from user_input import get_user_input

user_input = None
tickets_per_page = 25
curr_page = 0
prev_page = None
next_page = None
has_more = None


def main_func(user_input, tickets_per_page, curr_page, prev_page, next_page, has_more):
    '''
    Interactes with the user, displays tickets and displays proper error messages.
    '''
    read_input = True
    while True:
        try:
            while read_input:
                user_input = get_user_input(curr_page, has_more, user_input)
                if user_input in ['GET_ALL', 'GET_ID', 'PREV', 'NEXT', 'EXIT']:
                    read_input = False

            if user_input == 'GET_ALL' or user_input == 'NEXT':
                data = get_tickets(
                    next_page, tickets_per_page=tickets_per_page)
                curr_page = curr_page + 1 if len(data['tickets']) > 0 else 0
                has_more = data['meta']['has_more']
                prev_page = data['links']['prev']
                next_page = data['links']['next']
                display_tickets(data['tickets'])
            elif user_input == 'PREV':
                data = get_tickets(prev_page, tickets_per_page)
                curr_page = curr_page - 1 if len(data['tickets']) > 0 else 0
                has_more = data['meta']['has_more']
                prev_page = data['links']['prev']
                next_page = data['links']['next']
                display_tickets(data['tickets'])
            elif user_input == 'GET_ID':
                ticket_id = input('Enter ticket id: ')
                ticket = get_ticket(ticket_id)
                display_ticket(ticket['ticket'], full_info=True)
                curr_page = 0
                next_page = None
                prev_page = None
                has_more = None
            else:
                return
            read_input = True
        except Exception as error:
            display_error(error)


main_func(user_input, tickets_per_page, curr_page,
          prev_page, next_page, has_more)
