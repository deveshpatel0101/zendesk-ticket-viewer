import json


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
        ticket_id = args[0].split('/')[-1].split('=')[-1]
        for ticket in data['tickets']:
            if int(ticket['id']) == int(ticket_id):
                return MockResponse({'ticket': ticket}, 200)
    return MockResponse({
        "error": "RecordNotFound",
        "description": "Not found"
    }, 404)
