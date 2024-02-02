def get_formatted_city_country(city, country, population = ''):
    if population:
        formatted_name = f'{city.title()}, {country.title()} - Population: {population:,}'
    else:
        formatted_name = f'{city.title()}, {country.title()}'
    return formatted_name