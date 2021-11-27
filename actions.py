from user_input import get_user_input
from display_data import display_tickets, display_ticket
from tickets import get_tickets, get_ticket


def take_next_action(store):
    read_input = True
    user_input = None
    while read_input:
        user_input = get_user_input(store['curr_page'])
        if user_input in ['GET_ALL', 'GET_ID', 'PREV', 'NEXT', 'EXIT']:
            read_input = False
            store['user_input'] = user_input

    if user_input == 'GET_ALL' or user_input == 'NEXT':
        response = get_tickets(
            store['next_page'], tickets_per_page=store['tickets_per_page'])
        store['curr_page'] = store['curr_page'] + \
            1 if len(response['tickets']) > 0 else store['curr_page']
        display_tickets(response['tickets'])
    elif user_input == 'PREV':
        response = get_tickets(store['prev_page'], store['tickets_per_page'])
        store['curr_page'] = store['curr_page'] - 1
        display_tickets(response['tickets'])
    elif user_input == 'GET_ID':
        # reset pagination
        store['curr_page'] = 0
        store['prev_page'] = None
        store['next_page'] = None
        ticket_id = input('Enter ticket id: ')
        response = get_ticket(ticket_id)
        display_ticket(response['ticket'], full_info=True)

    store['curr_page'] = 0 if store['curr_page'] < 0 else store['curr_page']
    if user_input != 'GET_ID' and user_input != 'EXIT':
        # get prev page and next page only if they are present.
        # If we are fetching 10 tickets per page and there are 100 tickets,
        # the last response will still have has_more value as true
        # The 11th request for getting 101 to 110 tickets will have null as prev and next page
        temp = response['links']['prev']
        store['prev_page'] = temp if temp else store['prev_page']
        temp = response['links']['next']
        store['next_page'] = temp if temp else store['next_page']
