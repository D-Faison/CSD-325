#DeJanae Faison DATE Assignment 7.2
#Test Cases;

def city_country(city,country,population):
    #Format the city name
    formatted_City = f"{city},{country}-population:{population}"
    return(formatted_City)

#Several City Variables
city1 = city_country("Tokyo","Japan",4000)
city2 = city_country("Beijing","China",8000)
city3 = city_country("Jersey City","USA",2000)

print()
print(city1)
print()
print(city2)
print()
print(city3)
print()