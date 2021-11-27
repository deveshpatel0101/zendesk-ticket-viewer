from dateutil.parser import parse
from colorama import init, Fore
init(autoreset=True)


def display_tickets(tickets):
    if len(tickets) == 0:
        print(Fore.YELLOW + '==========================================')
        print(Fore.YELLOW + 'NO TICKETS TO DISPLAY')
        print(Fore.YELLOW + '==========================================')
    for ticket in tickets:
        display_ticket(ticket)


def display_ticket(ticket, full_info=False):
    print(Fore.GREEN + '==========================================')
    print(Fore.CYAN + 'ID' + Fore.RESET + f': {ticket["id"]}')
    print(Fore.CYAN + 'SUBJECT' + Fore.RESET + f': {ticket["subject"]}')
    print(Fore.CYAN + 'DATE OPENED' + Fore.RESET +
          f': {format_datetime(ticket["created_at"])}')
    if not full_info:
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
        print(Fore.CYAN + 'TAGS' + Fore.RESET + f': {", ".join(ticket["tags"])}')
    print(Fore.GREEN + '==========================================')


def display_error(message):
    print(Fore.YELLOW + '==========================================')
    print(Fore.YELLOW + str(message))
    print(Fore.YELLOW + '==========================================')


def format_datetime(utc_date_string):
    date = parse(utc_date_string)
    return date.strftime('%b-%d-%Y %I:%M:%S %p')
