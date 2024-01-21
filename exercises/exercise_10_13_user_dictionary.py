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
    user_details = dict()
    username = input('Please enter a username: ')
    user_details.update({'username': username})
    mobile = input('Please enter a mobile number: ')
    user_details.update({'mobile': mobile})
    email = input('Please enter an email address: ')
    user_details.update({'email': email})

    contents = json.dumps(user_details)
    path.write_text(contents)
    print('Account created successfully!')
        
def greet_user():
    '''Greet user by username and display details.'''
    path = Path('user_details.json')
    user_details = get_stored_account(path)

    if user_details:
        # print(type(user_details))
        {print(f'{k.title()}: {v}') for k, v in user_details.items()}
    else:
        account_response = input(
            'Account does not exist, would you like to create one? (yes/no): '
            )
        if account_response.lower() == 'yes':
            get_new_account(path)
        else:
            print('Exiting...')
     
greet_user()