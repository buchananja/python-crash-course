from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
lines = contents.splitlines()
        
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
birthday = input('Please enter your birthday (mmddyy): ')
if birthday in pi_string:
    print('Your birthday appears in the first million digits of pi!')
else:
    print('Your birthday does not appear in the first million digits of pi.')