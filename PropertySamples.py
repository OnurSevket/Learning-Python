
# region Exercise 1

# class Celcius:
#     def __init__(self, temprature=0):
#         self.temprature = temprature

#     def to_fahrenheit(self):
#         return (self.temprature*1.8)+32


# man = Celcius()

# man.temprature = 37

# print(man.temprature)

# print(man.to_fahrenheit())

# print(man.__dict__)

# endregion
###############################################################################################################################################################

# region Exercise 2

# class Celcius:
#     def __init__(self, temprature=0):
#         self.set_temperature(temprature)

#     def to_fahrenheit(self):
#         return (self.get_temprature()*1.8+32)

#     def get_temprature(self):
#         return self._temprature

#     def set_temperature(self, value):
#         if value < -273:
#             raise ValueError("Temprature below -273 is not possible")
#         self._temprature = value


# c = Celcius()

# c = Celcius(-37)

# c.get_temprature()

# c.set_temperature(10)

# c.set_temperature(-300)

# print(c.set_temperature(-277))

# c = Celcius()
# c._temprature = -300
# print(c.get_temprature())


# endregion
###############################################################################################################################################################

# region Exercise 3

# class Celsius:
#     def __init__(self, temperature = 0):
#         self.temperature = temperature

#     def to_fahrenheit(self):
#         return (self.temperature * 1.8) + 32

#     def get_temperature(self):
#         print("Getting value")
#         return self._temperature

#     def set_temperature(self, value):
#         if value < -273:
#             raise ValueError("Temperature below -273 is not possible")
#         print("Setting value")
#         self._temperature = value

#     temperature = property(get_temperature,set_temperature)


#c = Celcius()
# c.temperature = 43


# print(c.to_fahrenheit())

# endregion
###############################################################################################################################################################

# region Exercise 4

import math



print(math.pi)
print(math.e)


# endregion
###############################################################################################################################################################
