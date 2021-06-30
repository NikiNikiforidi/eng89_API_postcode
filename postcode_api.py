# We already touched base on API using requests
import requests



# First iteration
#check_response_postcode = requests.get("https://api.postcodes.io/postcodes/wc1h8jz")
# if check_response_postcode.status_code == 200:
#
#     print(f"The status code is: {check_response_postcode.status_code}")
#
# else :
#     print("Something went wrong")




# Second iteration


#Research how request is doing tha behind the scene
#check_response_postcode = requests.get("https://api.postcodes.io/postcodes/wc1h8jz")
# def checking_status_code():
#     if check_response_postcode:  # all the code and functionality is abstracted from the user.
#      return(f"Success: {check_response_postcode}")
#     else:
#      return(f"Unavailable{check_response_postcode}")
#
# print(checking_status_code())



# Third iteration
# check_response_postcode = requests.get("https://api.postcodes.io/postcodes/wc1h8jz")
# print(type(check_response_postcode.headers))
#
# # Lets see how we pass or get the data from dictionary
# print (check_response_postcode.json()) # json() converts the data. there is a lot of data in the dict
#
# # Lets store this data into a variable
# response_dict = check_response_postcode.json()
# print(response_dict)
# print(type(response_dict))
#
# # These 'result' in in the json dict
# result_dict = response_dict['result']
# print(response_dict)
#
# # iterating through the data
# for key in result_dict.keys():
#     print(f"The name of the key is {key} and the value insider is {result_dict}")


# **In class task**
# Prompt the user to enter the postcode
# validate the postcode
# present the location back to the user with required message
# Apply OOP

#
# user_postcode = input("What is your postcode?: ").replace(" ","")
#
# check_response_postcode = requests.get(f"https://api.postcodes.io/postcodes/{user_postcode}")
# # print(check_response_postcode)
#
# def checking_status_code():
#     if check_response_postcode:  # all the code and functionality is abstracted from the user.
#      return(f"Correct postcode: {check_response_postcode}")
#     else:
#      return(f"Incorrect postcode{check_response_postcode}")
#
# print(checking_status_code())
#
# # Lets store this data into a variable
# response_dict = check_response_postcode.json()
#
# # These 'result' are in the json dict. lest access them
# result_dict = response_dict['result']
#
#
# # iterating through the data
# for key, value in result_dict.items():
#    print(f"The name of the key is {key} and the value insider is {value}")


# Attempting to put everything in a class

class Postcode:

    def __init__(self,user_post):
        self.user_post = user_post.replace(" ","")

    check_response_postcode = requests.get(f"https://api.postcodes.io/postcodes/{self.user_post}")






user_postcode = input("Please enter your postcode: ")
postcode = Postcode(user_postcode)
print(postcode.user_post)




# # print(check_response_postcode)
#
# def checking_status_code():
#     if check_response_postcode:  # all the code and functionality is abstracted from the user.
#      return(f"Correct postcode: {check_response_postcode}")
#     else:
#      return(f"Incorrect postcode{check_response_postcode}")
#
# print(checking_status_code())
#
# # Lets store this data into a variable
# response_dict = check_response_postcode.json()
#
# # These 'result' are in the json dict. lest access them
# result_dict = response_dict['result']
#
#
# # iterating through the data
# for key, value in result_dict.items():
#    print(f"The name of the key is {key} and the value insider is {value}")