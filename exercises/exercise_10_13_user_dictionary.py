from pathlib import Path
import json

def get_stored_account(path):
    '''Retrives stored username if present.'''
    if path.exists():
        contents = path.read_text()
        user_details = json.loads(contents)
        return user_details
    else: 
        return None
            
def get_new_account(path):
    # Setting account details
    user_details = dict()
    username = input('Please enter a username: ')
    user_details.update({'username': username})
    mobile = input('Please enter a mobile number: ')
    user_details.update({'mobile': mobile})
    email = input('Please enter an email address: ')
    user_details.update({'email': email})
    # Setting password
    user_password = dict
    password = input('Please enter your password: ')
    user_password.update({'password': password})

    contents = json.dumps(user_details)
    path.write_text(contents)
    print('Account created successfully!')

def check_password(path):
    '''Retrives stored username if present.'''
    if path.exists():
        contents = path.read_text()
        user_password = json.loads(contents)
        return user_password
    else: 
        return None

def greet_user():
    '''Greet user by username and display details.'''
    path = Path('user_details.json')
    user_details = get_stored_account(path)

    if user_details:
        print(f'Remembered username: {user_details["username"]}')
        account_response = input(f'Is this your username? (yes/no): ')
        if account_response.lower() == 'yes':
                {print(f'{k.title()}: {v}') for k, v in user_details.items()}
        else:
            print('Exiting...') 
    else:
        account_response = input(
            'Account does not exist, would you like to create one? (yes/no): '
            )
        if account_response.lower() == 'yes':
            get_new_account(path)
        else:
            print('Exiting...')
     
greet_user()