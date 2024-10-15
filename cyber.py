 # this is python

# print("IM eddy!")

# print (10 > 4)

 #varibles

device_ID = "EB3/56398"

# print (device_ID)

#type function

# data_type = type(device_ID)
# print(data_type)

#conditional statements

# operating_System = "OS 3"

# if (operating_System == "OS 2"):
#     print("Updates needed")
# else:
# #     print("no updates needed")


# #loops

# for i in range(10):
#     print("I'm Eddy")

# max_devices = 5
# i =1 

# while i <= max_devices:
#     print("connect")
#     i = i +1
# print("cant")


#define a function

# def greet_employee(firstname, lastname):
#     print("hello", firstname, lastname)
  
# greet_employee("eddy", "Kilonzo")


#retun info from a fuction 

def caclulate_fails(total_attempts, failed_attempts):
    fail_percentage = failed_attempts / total_attempts

    return fail_percentage

percentage = caclulate_fails(4, 2)


if (percentage >= .5):
    print("account locked")

