import requests
from envs import EMAIL, API_TOKEN, DOMAIN


def get_tickets(page=None, tickets_per_page=25):
    '''
    Raises exception if the GET request fails\n
    Else returns the response
    '''
    if page is None:
        page = f'{DOMAIN}/api/v2/tickets.json?page[size]={tickets_per_page}'
    response = requests.get(page, auth=(EMAIL, API_TOKEN))
    return process_response(response)


def get_ticket(ticket_id):
    '''
    Raises exception if the GET request fails\n
    Else returns a dict that contains ticket info
    '''
    url = f'{DOMAIN}/api/v2/tickets/{ticket_id}'
    response = requests.get(url, auth=(EMAIL, API_TOKEN))
    return process_response(response)


def process_response(response):
    if response.status_code == 200:
        return response.json()

    if 'application/json' in response.headers['content-type']:
        data = response.json()
        error_msg = data['error']
        if 'description' in data:
            error_msg += f' - {data["description"]}'
        raise Exception(error_msg)
    else:
        raise Exception(response.text)
