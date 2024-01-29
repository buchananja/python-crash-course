from name_function import get_formatted_name

def test_first_last_name():
    formatted_name = get_formatted_name('james', 'buchanan')
    assert formatted_name == 'James Buchanan'

def test_first_last_middle_name():
    formatted_name = get_formatted_name('james', 'buchanan', 'allan')
    assert formatted_name == 'James Allan Buchanan'