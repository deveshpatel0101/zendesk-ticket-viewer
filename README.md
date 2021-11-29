# Zendesk Ticket Viewer

### Contents

1. Installation
2. Unit tests
3. Usage

### Installation

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
   pip install -r requirements.txt
   ```
5. Once all the libraries have been installed, run the following command to start the program.
   ```
   python main.py
   ```

### Unit tests

1. To run the tests, execute the following:
   ```
   python -m unittest tests/*.py -b
   ```
   Please note the `-b` option. Since there are a lot of print statements, this option will supress them during tests.

### Usage

After executing the command `python main.py`, you will have the following screen.

<p align="center">
<img src="https://i.imgur.com/kUQ3KEQ.jpeg" width="95%" align="center" />
</p>

Read the set of options displayed and hit the associated number to either page through the tickets or search a ticket by id.

Following are some of the screenshots.

<p align="center">
<img src="https://i.imgur.com/1yuS1FW.jpg" width="95%" />
</p>

<p align="center">
<img src="https://i.imgur.com/JKbhodh.jpg" width="95%" />
</p>

<p align="center">
<img src="https://i.imgur.com/HAq08aK.jpg" width="95%" />
</p>


<h2 align="center">
HAVE FUN
</h2>
