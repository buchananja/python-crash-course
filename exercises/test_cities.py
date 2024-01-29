from city_functions import format_city_country

def test_city_country():
    city_country_name = format_city_country('aberdeen', 'scotland')
    assert city_country_name == 'Aberdeen, Scotland'

def test_city_country_population():
    city_country_name = format_city_country('aberdeen', 'scotland', population = '198,590')
    assert city_country_name == 'Aberdeen, Scotland - population: 198,590'

def test_city_country_population_different_name():
    city_country_name = format_city_country('santiago', 'chile', population = '5,000,000')
    assert city_country_name == 'Santiago, Chile - population: 5,000,000'