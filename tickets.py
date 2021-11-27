import requests
from envs import EMAIL, API_TOKEN, DOMAIN


def get_tickets(page=None, tickets_per_page=25):
    '''
    Raises exception if the GET request fails\n
    Else returns a dict that contains\n
    1. list of all tickets\n
    2. link to the next page\n
    3. link to the prev page\n
    4. count indicating the total number of tickets
    '''
    if page is None:
        page = f'{DOMAIN}/api/v2/tickets.json?page[size]={tickets_per_page}'
    data = requests.get(page, auth=(EMAIL, API_TOKEN))
    if (data.status_code != 200):
        raise Exception(data.json()['error'])
    return data.json()


def get_ticket(ticket_id):
    '''
    Raises exception if the GET request fails\n
    Else returns a dict that contains ticket info
    '''
    url = f'{DOMAIN}/api/v2/tickets/{ticket_id}'
    data = requests.get(url, auth=(EMAIL, API_TOKEN))
    if (data.status_code != 200):
        raise Exception(data.json()['error'])
    return data.json()
