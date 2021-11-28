import unittest
from unittest import mock
from mockers.mock_tickets import mock_get_tickets, mock_get_ticket
from actions import take_next_action


def get_new_store():
    return {
        'user_input': None,
        'curr_page': 0,
        'prev_page': None,
        'next_page': None,
        'tickets_per_page': 5,
    }


class TestActions(unittest.TestCase):
    @mock.patch('console_io.user_input.get_input', return_value='1')
    @mock.patch('controllers.tickets.requests.get', side_effect=mock_get_tickets)
    def test_user_input_get_all(self, *args):
        store = get_new_store()
        take_next_action(store)
        self.assertEqual(store['user_input'], 'GET_ALL')
        self.assertEqual(store['curr_page'], 1)

    @mock.patch('console_io.user_input.get_input', return_value='1')
    @mock.patch('controllers.tickets.requests.get', side_effect=mock_get_tickets)
    def test_user_input_next(self, *args):
        store = get_new_store()
        store['curr_page'] = 1
        take_next_action(store)
        self.assertEqual(store['user_input'], 'NEXT')
        self.assertEqual(store['curr_page'], 2)

    @mock.patch('console_io.user_input.get_input', return_value='1')
    @mock.patch('controllers.tickets.requests.get', side_effect=mock_get_tickets)
    def test_user_input_prev(self, *args):
        store = get_new_store()
        store['curr_page'] = 2
        take_next_action(store)
        self.assertEqual(store['user_input'], 'PREV')
        self.assertEqual(store['curr_page'], 1)

    @mock.patch('console_io.user_input.get_input', return_value='2')
    @mock.patch('actions.get_input_id', return_value='2')
    @mock.patch('controllers.tickets.requests.get', side_effect=mock_get_ticket)
    def test_user_input_get_id_with_valid_id(self, *args):
        store = get_new_store()
        store['curr_page'] = 1
        take_next_action(store)
        self.assertEqual(store['user_input'], 'GET_ID')
        self.assertEqual(store['curr_page'], 0)

    @mock.patch('console_io.user_input.get_input', return_value='2')
    @mock.patch('actions.get_input_id', return_value='124')
    @mock.patch('controllers.tickets.requests.get', side_effect=mock_get_ticket)
    def test_user_input_get_id_with_invalid_id(self, *args):
        store = get_new_store()
        self.assertRaises(Exception, take_next_action, store)
        self.assertEqual(store['user_input'], 'GET_ID')
        self.assertEqual(store['curr_page'], 0)

    @mock.patch('console_io.user_input.get_input', return_value='9')
    @mock.patch('controllers.tickets.requests.get', side_effect=mock_get_tickets)
    def test_user_input_exit(self, *args):
        store = get_new_store()
        take_next_action(store)
        self.assertEqual(store['user_input'], 'EXIT')
