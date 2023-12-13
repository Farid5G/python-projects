# Welcome the user 
print("Welcome to Our BrandName Genrator Code")

# storing input Values from user to CityName and PetName
cityName,petName = input("Enter your City Name: "),input("Enter Your Pet Name: ")
BrandName = cityName.capitalize() + petName.capitalize()

# Printing the BrandName Using String Concatination operator - "+"
print("Your BrandName could be :" + BrandName)

# Doing  the Same in Single Line
# print("Welcome to BrandName Generator"),print(f"Your BrandName could be: {input("Enter your city Name: ").capitalize()}{input("Enter Your PetName: ").capitalize()}")