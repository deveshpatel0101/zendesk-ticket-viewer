## Zendesk Ticket Viewer

### Contents

1. Run the program
2. Run unit tests
3. Basic folder structure and file info

### Run the program

To start the program, follow the below instructions:

1. Clone or download this repository.
2. Open your terminal and navigate where the repository was downloaded.
3. Create `.env` file in the root directory and paste the following contents and add the corresponding details.

   ```
   EMAIL=YOUR_EMAIL_ASSOCIATED_WITH_ZENDESK
   API_TOKEN=YOUR_API_TOKEN
   DOMAIN=https://{YOUR_DOMAIN_NAME}.zendesk.com
   ```

   To generate API TOKEN, go to Admin Center > Apps and Integrations > Zendesk API > Add API Token

   For email, do not append `/token`. Just write your email as `example@gmail.com`.

4. Use the following command to install the required libraries.
   ```
   pip install requests python-dateutil colorama python-decouple
   ```
5. Once all the libraries have been installed, run the following command to start the program.
   ```
   python main.py
   ```

### Run unit tests

1. To run the tests, execute the following:
   ```
   python -m unittest tests/*.py -b
   ```
   Please note the `-b` option. Since there are a lot of print statements, this option will supress them during tests.

### Folder structure and file info

The root directory has following files:

1. `display_data.py`: Bunch of functions to print statements to display ticket information and error messages
2. `envs.py`: Loads environment variables set in `.env` file using `python-decouple` library.
3. `main.py`: Main execution point of the program.
4. `tickets.py`: Two functions to get list of tickets and a ticket by id from zendesk API.
5. `user_input.py`: Has function to get the user input.
6. `tests/`: Folder contains unit tests that tests the code of `tickets.py` and `user_input.py` files.

```
HAVE FUN!!
```
