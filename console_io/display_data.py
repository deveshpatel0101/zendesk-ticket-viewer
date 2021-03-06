from dateutil.parser import parse
from colorama import init, Fore
init(autoreset=True)

DELIMITER_SIZE = 45


def display_tickets(tickets):
    '''
    Displays the list of tickets
    '''
    if len(tickets) == 0:
        print(Fore.YELLOW + '='*DELIMITER_SIZE)
        print(Fore.YELLOW + 'NO TICKETS TO SHOW')
        print(Fore.YELLOW + '='*DELIMITER_SIZE)
        return
    print(Fore.GREEN + '='*DELIMITER_SIZE)
    for (index, ticket) in enumerate(tickets):
        display_ticket(ticket)
        if index != len(tickets) - 1:
            print(Fore.GREEN + '-'*DELIMITER_SIZE)
        else:
            print(Fore.GREEN + '='*DELIMITER_SIZE)


def display_ticket(ticket, full_info=False):
    '''
    Displays a single ticket
    '''
    if full_info:
        print(Fore.GREEN + '='*DELIMITER_SIZE)
    print(Fore.CYAN + 'ID' + Fore.RESET + f': {ticket["id"]}')
    print(Fore.CYAN + 'SUBJECT' + Fore.RESET + f': {ticket["subject"][:50]}')
    print(Fore.CYAN + 'DATE OPENED' + Fore.RESET +
          f': {format_datetime(ticket["created_at"])}')
    if not full_info:
        print(Fore.CYAN + 'STATUS' + Fore.RESET + f': {ticket["status"]}')
        description = ticket['description'].replace('\n', ' ')[:50]
        print(Fore.CYAN + 'DESCRIPTION' + Fore.RESET +
              f': {description}...')
    if full_info:
        print(Fore.CYAN + 'LAST UPDATED' + Fore.RESET +
              f': {format_datetime(ticket["updated_at"])}')
        print(Fore.CYAN + 'DESCRIPTION' + Fore.RESET +
              f': {ticket["description"]}')
        print(Fore.CYAN + 'PRIORITY' + Fore.RESET + f': {ticket["priority"]}')
        print(Fore.CYAN + 'STATUS' + Fore.RESET + f': {ticket["status"]}')
        print(Fore.CYAN + 'TAGS' + Fore.RESET +
              f': {", ".join(ticket["tags"])}')
    if full_info:
        print(Fore.GREEN + '='*DELIMITER_SIZE)


def display_error(message):
    '''
    Displays error message
    '''
    print(Fore.YELLOW + '='*DELIMITER_SIZE)
    print(Fore.YELLOW + str(message))
    print(Fore.YELLOW + '='*DELIMITER_SIZE)


def format_datetime(utc_date_string):
    '''
    Converts UTC datetime string to readable format
    '''
    date = parse(utc_date_string)
    return date.strftime('%b-%d-%Y %I:%M:%S %p')
