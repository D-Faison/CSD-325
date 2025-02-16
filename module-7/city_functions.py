#DeJanae Faison 2/16/24 Assignment 7.2
#Test Cases;

def city_country(city,country,population = None, language = None):
    #Format the city name
    formatted_City = f"{city},{country}"

    #Optional Parameters
    if population and language:
        #The Variable has all 4 parameters
        return(f"{formatted_City}-population:{population},{language}")
    #Variable has the city, country and language, NOT Population
    elif language:
        return(f"{formatted_City}-{language}")
    #Variable has the city, country and population but NOT language
    elif population:
        return(f"{formatted_City}-population:{population}")
    #Has city and country but NOT population and language
    else:
        return(formatted_City)
    


#Several City Variables
city1 = city_country("Tokyo","Japan")
city2 = city_country("Beijing","China",8000)
city3 = city_country("Jersey City","USA",2000,"English")
#Display City Variables
print()
print(city1)
print()
print(city2)
print()
print(city3)
print()