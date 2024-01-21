from pathlib import Path
import json

# try:
#     path = Path('favourite_number.json')
#     contents = path.read_text()
#     favourite_number = json.loads(contents)
#     print(f'Your favourite number is {favourite_number}.')
# except FileNotFoundError:
#     favourite_number = input('Please enter your favourite number: ')
#     contents = json.dumps(int(favourite_number))
#     path.write_text(contents)


#OR

path = Path('favourite_number.json')

if path.is_file():
    contents = path.read_text()
    favourite_number = json.loads(contents)
    print(f'Your favourite number is {favourite_number}.')
else:
    favourite_number = input('Please enter your favourite number: ')
    contents = json.dumps(int(favourite_number))
    path.write_text(contents)
