from city_functions import get_formatted_city_country

def test_city_formatted_name():
    formatted_name = get_formatted_city_country('aberdeen', 'scotland')
    assert formatted_name == 'Aberdeen, Scotland'
    
def test_city_formatted_name_population():
    formatted_name = get_formatted_city_country('aberdeen', 'scotland', 198590)
    assert formatted_name == 'Aberdeen, Scotland - Population: 198,590'