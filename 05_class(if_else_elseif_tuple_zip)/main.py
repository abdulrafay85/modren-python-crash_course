# user_database : list[tuple[str, str]] = [('rafay', '123'), ('irsham', '456'), ('qasim', '789')]

## simple if_else
# user_name = input("Enter Your Name")
# user_password = input("Enter Your Password")

# for userInfo in user_database:
#     name, password = userInfo
#     if name==user_name and password==user_password:
#         print("Valid User")
#         break
# else:
#     print("please enter correct information")
    

##   nested if_else
# user_database : list[tuple[str, str]] = [('rafay', '123'), ('irsham', '456'), ('qasim', '789')]

# user_name = input("Enter Your Name")
# user_password = input("Enter Your Password")

# for userInfo in user_database:
#     name, password = userInfo
#     if name==user_name:
#         print("name is correct")
#         if password==user_password:
#             print("Valid User")
#             break
# else:
#     print("please enter correct information")
    



from typing import Union

perType = Union[float, int]
percantages :list[perType] 

percantages = [88, 99, 63, 45, 23, 32, 57]

grades : list[str] = []

for per in percantages:
    grade : str = ""
    
    if (per >= 0) and (per < 33):           # True becuase 99 >= 0  to 99 graterthan hay 0 say is liyen pehla bolck true hay
        grade = "Fail"
    elif (per >= 33) and (per < 40):
        grade = "E"
    elif (per >= 40) and (per < 50):
        grade = "D"
    elif (per >= 50) and (per < 60):
        grade = "C"
    elif (per >= 60) and (per < 70):
        grade = "B"
    elif (per >= 70) and (per < 80):
        grade = "A"
    elif (per >= 80) and (per <= 100):
        grade = "A+"
    grades.append(grade)

print(f"Percentage {percantages}")
print(f"Grade {grade}")

# print(f"Dear Student your percentage is {per} now your calculated grade is:\t {grade}")
