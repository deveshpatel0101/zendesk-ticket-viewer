import json
import unittest
from unittest import mock
from controllers.tickets import get_tickets, get_ticket
from mockers.mock_tickets import mock_get_tickets, mock_get_ticket


class TestTickets(unittest.TestCase):
    @mock.patch('controllers.tickets.requests.get', side_effect=mock_get_tickets)
    def test_get_tickets(self, mocker):
        data = get_tickets(None, 25)
        f = open('tests/response.json')
        originalData = json.load(f)
        f.close()
        self.assertEqual(originalData, data)

    @mock.patch('controllers.tickets.requests.get', side_effect=mock_get_ticket)
    def test_get_ticket(self, mocker):
        response = get_ticket(14)
        f = open('tests/response.json')
        data = json.load(f)
        f.close()
        originalTicket = None
        for ticket in data['tickets']:
            if ticket['id'] == 14:
                originalTicket = ticket
                break
        self.assertEqual(response['ticket'], originalTicket)
        self.assertRaises(Exception, get_ticket, 100)
