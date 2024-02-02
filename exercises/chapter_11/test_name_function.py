from name_function import get_formatted_name

def test_first_last_name():
    '''Do names like "James Buchanan" work?'''
    formatted_name = get_formatted_name('james', 'buchanan')
    assert formatted_name == 'James Buchanan'
    
def test_first_last_middle_name():
    '''Do names like "James Buchanan" work?'''
    formatted_name = get_formatted_name('james', 'buchanan', middle = 'allan')
    assert formatted_name == 'James Allan Buchanan'