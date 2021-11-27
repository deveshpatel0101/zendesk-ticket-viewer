from decouple import config

EMAIL = f'{config("EMAIL")}/token'
API_TOKEN = config('API_TOKEN')
DOMAIN = config('DOMAIN')
