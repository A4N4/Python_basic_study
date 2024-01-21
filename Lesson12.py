# Task 1
# class Town:
#     __town_name: str = "no name"
#     __region: str = "no region"
#     __country_name: str = "no name"
#     __town_population: int = 0
#     __town_postIndex: str = "no index"
#     __town_phoneCode: str = "no code"
#
#     def __init__(self, town_name, region, country_name, town_population, town_postIndex, town_phoneCode):
#         self.town_name = town_name
#         self.region = region
#         self.country_name = country_name
#         self.town_population = town_population
#         self.town_postIndex = town_postIndex
#         self.town_phoneCode = town_phoneCode
#
#     @property
#     def town_name(self):
#         return self.__town_name
#
#     @town_name.setter
#     def town_name(self, town_name):
#         if 2 < len(town_name) < 55:
#             self.__town_name = town_name
#         else:
#             print("Town name is incorrect!")
#
#     @property
#     def region(self):
#         return self.__region
#
#     @region.setter
#     def region(self, region):
#         if 2 < len(region) < 55:
#             self.__region = region
#         else:
#             print("Region name is incorrect!")
#
#     @property
#     def country_name(self):
#         return self.__country_name
#
#     @country_name.setter
#     def country_name(self, country_name):
#         if 2 < len(country_name) < 55:
#             self.__country_name = country_name
#         else:
#             print("Country name is incorrect!")
#
#     @property
#     def town_population(self):
#         return self.__town_population
#
#     @town_population.setter
#     def town_population(self, town_population):
#         if 0 < town_population < 150000000:
#             self.__town_population = town_population
#         else:
#             print("Population filled incorrectly!")
#
#     @property
#     def town_postIndex(self):
#         return self.__town_postIndex
#
#     @town_postIndex.setter
#     def town_postIndex(self, town_postIndex):
#         if 0 < len(town_postIndex) < 6 and town_postIndex.isdigit():
#             self.__town_postIndex = town_postIndex
#         else:
#             print("Town post index is incorrect!")
#
#     @property
#     def town_phoneCode(self):
#             return self.__town_phoneCode
#
#     @town_phoneCode.setter
#     def town_phoneCode(self, town_phoneCode):
#             if 0 < len(town_phoneCode) <6 and town_phoneCode.isdigit():
#                 self.__town_phoneCode = town_phoneCode
#             else:
#                 print("Town phone code is incorrect!")
#
#     def show_town_info (self):
#         print(f"Town:{self.town_name},\nRegion: {self.region},\nCountry: {self.country_name},\n"
#                         f"Population: {self.town_population},\nIndex: {self.town_postIndex},\n"
#                          f"Phone code: {self.town_phoneCode} ")
#
# test_Town= Town('Kharkiv','Kharkiv', 'Ukraine', 1556, '61166' ,'380')
# test_Town.show_town_info()
#
# Task 2
#
# class Country:
#     __country_name: str = "no name"
#     __continent: str = "no name"
#     __country_population: int = 0
#     __country_phoneCode: str = "no code"
#     __country_capitol: str = "no name"
#     __country_cities: str = "no name"
#
#     def __init__( self, country_name,continent, country_population, country_phoneCode, country_capitol, country_cities,):
#         self.country_name = country_name
#         self.continent = continent
#         self.country_population = country_population
#         self.country_phoneCode = country_phoneCode
#         self.country_capitol = country_capitol
#         self.country_cities = country_cities
#
#     @property
#     def country_name(self):
#         return self.__country_name
#
#     @country_name.setter
#     def country_name(self, country_name):
#         if 2 < len(country_name) < 55:
#             self.__country_name = country_name
#         else:
#             print("Country name is incorrect!")
#
#     @property
#     def continent(self):
#         return self.__continent
#
#     @continent.setter
#     def continent(self, continent):
#         if 2 < len(continent) < 17:
#             self.__continent = continent
#         else:
#             print("Continent name is incorrect!")
#
#     @property
#     def country_capitol(self):
#         return self.__country_capitol
#
#     @country_capitol.setter
#     def country_capitol(self, country_capitol):
#         if 2 < len(country_capitol) < 17:
#             self.__country_capitol = country_capitol
#         else:
#             print("Country capitol name is incorrect!")
#
#     @property
#     def country_cities(self):
#         return self.__country_cities
#
#     @country_cities.setter
#     def country_cities(self, country_cities):
#         if 2 < len(country_cities) < 17:
#             self.__country_cities = country_cities
#         else:
#             print("City name is incorrect!")
#
#     @property
#     def country_population(self):
#         return self.__country_population
#
#     @country_population.setter
#     def country_population(self, country_population):
#         if 0 < country_population < 150000000:
#             self.__country_population = country_population
#         else:
#             print("Population filled incorrectly!")
#
#     @property
#     def country_phoneCode(self):
#         return self.__country_phoneCode
#
#     @country_phoneCode.setter
#     def country_phoneCode(self, country_phoneCode):
#         if 0 < len(country_phoneCode) <6 and country_phoneCode.isdigit():
#             self.__country_phoneCode = country_phoneCode
#         else:
#             print("Country code filled incorrectly!")
#
#
#     def show_country_info(self):
#         print(
#             f"Country:{self.country_name},\nContinent: {self.continent},\nCountry population: {self.country_population},\n"
#             f"Phone code: {self.country_phoneCode},\nCapitol: {self.country_capitol},\nCities: {self.country_cities} "
#         )
#
#
# test_Country = Country("Denmark", "Europe", 745000, "+5558", "Copenhagen", "Aarhus")
# test_Country.show_country_info()
