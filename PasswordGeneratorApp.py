# This program will generate password by 
#  substring first 2 characters  and display
# combined character.

import random

#1. Crreate a greeting for your program
print('Welcome Strong password generator app')

# Create an array to store the user's inputs
inputs = []
new_password = []
random_pass = []

#2. Ask the user for his/her mother's middle name
mother_middle_name = input('What is your mother middle name:')

# Add to the list 
inputs.append(mother_middle_name)


#3. Ask the user for his/her pet's name
pet_name = input('What is your pet name: ')
inputs.append(pet_name)

#4. Ask the user for his/her older' son name
older_son_name = input('What is your older son name: ')
inputs.append(older_son_name)

#5. Ask the user for his/her city of birth name
city_of_birth = input('What is the name of city of your brith? ')
inputs.append(city_of_birth)


# Generate strong password using provided information

for x in inputs:
  print(x)
  first_two_chars = x[0:2]
  #first_two_chars = x[2:-2]
  new_password.append(first_two_chars)

# Get the first 2 character of each element
# store it inside new array - new password
#new_password.append((x[0:2]))

# Profile information like  first name, last name, SSN, Phone number,
# address, email should not be included in the generated password


# Add all characters of array new_password
for y in new_password:
   print(y)


# print('Your new generated password is : '+ new_password)
joined_password = ''.join(new_password)

# Display the output
print("The generated password is : " + joined_password)




