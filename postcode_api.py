# ### Postcode with API

# - We already touched base on API using requests
# - In Terminal: pip install requests
# import requests
#
# # - First iteration
#
# check_response_postcode = requests.get("https://api.postcodes.io/postcodes/wc1h8jz")
# print(check_response_postcode.status_code)   # To check the status
#
#
# if check_response_postcode.status_code == 200:
#
#     print(f"The status code is: {check_response_postcode.status_code}")
#
# else :
#     print("Something went wrong, try another postcode")
#
#


# - Second iteration
# **NOTE** in this iteration there is no .status_code when checking the response, nor any condition ( == 200 )

# import requests
#
# check_response_postcode = requests.get("https://api.postcodes.io/postcodes/wc1h8jz")
#
# def checking_status_code():
#     if check_response_postcode:  # all the code and functionality is abstracted from the user.
#      return(f"Success: {check_response_postcode}")
#     else:
#      return(f"Unavailable{check_response_postcode}")
#
# print(checking_status_code())



# Third iteration
 # import requests
# check_response_postcode = requests.get("https://api.postcodes.io/postcodes/wc1h8jz")


#print(type(check_response_postcode.content)) # Type is bytes
#print(type(check_response_postcode.headers)) # Type is requests.structures.CaseInsensitiveDict
#print(type(check_response_postcode)) # Type is requests.models.Response


# Lets see how we pass or get the data from dictionary

# response_dict = check_response_postcode.json() # json() converts the data into dict.

#print(type(check_response_postcode.json())) # Type is dict
#print(type(response_dict))



# Lets store this data into a variable and iterate through it

# The `response_dict` has another dict inside it, we want to access that
# The 'result' dict is in the json dict
#
# result_dict = response_dict['result']
# print(result_dict)

# **The below for loops give the same results**
# This is from the lecture
# for key in result_dict.keys():
#     print(f"The name of the key is {key} and the vale inside is {result_dict[key]}")


# This is how I decided to do it
#
# for key, value in result_dict.items():
#     print(f"The name of the key is {key} and the value inside is {value}")
#


#- ------------------------------------------------------------------
# - **In class task**

# - Prompt the user to enter the postcode
# - Validate the postcode
# - Present the location back to the user with required message
# - Do again but apply OOP

# import requests
# # Get user postcode and remove any spaces
# user_postcode = input("What is your postcode?: ").replace(" ","")
#
# # Check the response
# check_response_postcode = requests.get(f"https://api.postcodes.io/postcodes/{user_postcode}")
#
# #
# def checking_status_code():
#     if check_response_postcode:  # all the code and functionality is abstracted from the user.
#      return(f"Correct postcode: {check_response_postcode}")
#     else:
#      return(f"Incorrect postcode: {check_response_postcode}")
#
# print(checking_status_code())
#
# # Lets store this data in a variable and change it to dictionary
# response_dict = check_response_postcode.json()
#
# # These 'result' are in the json dict, lets access them
# result_dict = response_dict['result']
#
#
# # iterating through the data
# for key, value in result_dict.items():
#    print(f"The name of the key is {key} and the value insider is {value}")


# -  Attempting to put everything in a class

import requests



class Postcode:
    def __init__(self,postcode):
        self.postcode = postcode
        self.status_code = requests.get(f"https://api.postcodes.io/postcodes/{self.postcode}").status_code


        if self.status_code == 200:
            print(f"Success: {self.status_code}")
        else:
            print(f"Unavailable{self.status_code}")



# Prompt user for postcode and get rid of any spaces
user_postcode = input("What is your postcode?: ").replace(" ","")


print(user_postcode) # Print to check if spaces are removed
print(type(user_postcode)) # Checking the type. The type is a str

obj = Postcode(user_postcode) # Creating an obj of the class
print(obj.postcode) # checking to see if def __init__ works
print(obj.status_code)


