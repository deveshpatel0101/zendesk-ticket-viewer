def display_tickets(tickets):
    if len(tickets) == 0:
        print('==========================================')
        print("NO TICKETS TO DISPLAY")
        print('==========================================')
    for index, ticket in enumerate(tickets):
        display_ticket(ticket, index+1)


def display_ticket(ticket, number=None, full_info=False):
    print('==========================================')
    if not full_info:
        print(f'{number}.')
    print(f'ID: {ticket["id"]}')
    print(f'SUBJECT: {ticket["subject"]}')
    print(f'DATE OPENED: {ticket["created_at"]}')
    if not full_info:
        print(f'DESCRIPTION: {ticket["description"][:50]}...')
    if full_info:
        print(f'DESCRIPTION: {ticket["description"]}')
        print(f'PRIORITY: {ticket["priority"]}')
        print(f'STATUS: {ticket["status"]}')
    print('==========================================')


def display_error(error):
    print('==========================================')
    print('ERROR OCCURRED!')
    print(str(error))
    print('==========================================')
