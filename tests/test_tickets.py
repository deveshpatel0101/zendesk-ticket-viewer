import json
import unittest
from unittest import mock
from tickets import get_tickets, get_ticket


def mock_get_tickets(*args, **kwargs):
    class MockResponse:
        def __init__(self, data, status_code):
            self.status_code = status_code
            self.json_data = data

        def json(self):
            return self.json_data

    f = open('tests/response.json', 'r')
    data = json.load(f)
    f.close()
    return MockResponse(data, 200)


def mock_get_ticket(*args, **kwargs):
    class MockResponse:
        def __init__(self, data, status_code):
            self.status_code = status_code
            self.json_data = data

        def json(self):
            return self.json_data

    if len(args) > 0:
        f = open('tests/response.json', 'r')
        data = json.load(f)
        f.close()
        ticket_id = args[0].split('/')[-1]
        for ticket in data['tickets']:
            if int(ticket['id']) == int(ticket_id):
                return MockResponse({'ticket': ticket}, 200)
    return MockResponse({
        "error": "RecordNotFound",
        "description": "Not found"
    }, 404)


class TestTickets(unittest.TestCase):
    @mock.patch('tickets.requests.get', side_effect=mock_get_tickets)
    def test_get_tickets(self, mocker):
        data = get_tickets(None, 25)
        f = open('tests/response.json')
        originalData = json.load(f)
        f.close()
        self.assertEqual(originalData, data)

    @mock.patch('tickets.requests.get', side_effect=mock_get_ticket)
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
