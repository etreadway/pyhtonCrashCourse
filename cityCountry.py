def cityCountry(cityName, countryName, population=''):
    properLocation = cityName.title() + ', ' + countryName.title()
    if population:
        properLocation += ', ' + str(population)
    return properLocation
