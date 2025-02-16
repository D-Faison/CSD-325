#DeJanae Faison 2/16/24 Assignment TestCases

#import file function
from city_functions import city_country
#import testing function
import unittest

#general class for testing that inherits from unittests testcase
class testingMethods(unittest.TestCase):
    #method to call upon the script
    def test_city_country(self):
      #does the value from the function == the desireed answer 
      #when inputting the city and country does it = City,Country
      self.assertEqual(city_country("Tokyo","Japan"),"Tokyo,Japan")
      self.assertEqual(city_country("Beijing","China"),"Beijing,China")
      self.assertEqual(city_country("Jersey City","USA"),"Jersey City,USA")

#run the script
if __name__ == '__main__':
   unittest.main()