import requests
from actions import take_next_action
from display_data import display_error


store = {
    'user_input': None,
    'curr_page': 0,
    'prev_page': None,
    'next_page': None,
    'tickets_per_page': 5,
}


def func_main(store):
    while store['user_input'] != 'EXIT':
        try:
            take_next_action(store)
        except requests.exceptions.ConnectionError:
            display_error(
                'Connection Error!\nThis could be because either the server is down or your internet is not working!')
        except requests.exceptions.RequestException:
            display_error(
                'Something went wrong while fetching data from the API!')
        except Exception as error:
            display_error(error)


func_main(store)
