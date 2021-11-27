import requests
from tickets import get_tickets, get_ticket
from display_data import display_error, display_tickets, display_ticket
from user_input import get_user_input

user_input = None
tickets_per_page = 5
curr_page = 0
prev_page = None
next_page = None


def main_func(user_input, tickets_per_page, curr_page, prev_page, next_page):
    '''
    Interacts with the user, displays tickets and displays proper error messages.
    '''
    read_input = True
    response = None
    while True:
        try:
            while read_input:
                user_input = get_user_input(curr_page)
                if user_input in ['GET_ALL', 'GET_ID', 'PREV', 'NEXT', 'EXIT']:
                    read_input = False

            if user_input == 'GET_ALL' or user_input == 'NEXT':
                response = get_tickets(
                    next_page, tickets_per_page=tickets_per_page)
                curr_page = curr_page + \
                    1 if len(response['tickets']) > 0 else curr_page
                display_tickets(response['tickets'])
            elif user_input == 'PREV':
                response = get_tickets(prev_page, tickets_per_page)
                curr_page = curr_page - 1
                display_tickets(response['tickets'])
            elif user_input == 'GET_ID':
                ticket_id = input('Enter ticket id: ')
                response = get_ticket(ticket_id)
                display_ticket(response['ticket'], full_info=True)
            else:
                return
        except requests.exceptions.ConnectionError:
            display_error(
                'Connection Error!\nThis could be because either the server is down or your internet is not working!')
        except requests.exceptions.RequestException:
            display_error(
                'Something went wrong while fetching data from the API!')
        except Exception as error:
            display_error(error)
        finally:
            read_input = True
            if user_input != 'GET_ID':
                temp = response['links']['prev']
                prev_page = temp if temp else prev_page
                temp = response['links']['next']
                next_page = temp if temp else next_page
            elif user_input == 'GET_ID':
                curr_page = 0
                next_page = None
                prev_page = None


main_func(user_input, tickets_per_page, curr_page, prev_page, next_page)
