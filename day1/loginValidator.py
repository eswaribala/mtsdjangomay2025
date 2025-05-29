import re
def validate(**details):
    userNamePattern= r'^[a-zA-Z]{5,10}$'
    passwordPattern = r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
    for key, value in details.items():
      
       if(key == 'userName'):         
         if(re.fullmatch(userNamePattern, value)):
              print(f"UserName{value} is valid")
       if(key == 'password'):         
         if(re.fullmatch(passwordPattern, value)):
              print(f"Password{value} is valid")

#main function created only when you execute current file
if __name__ == "__main__":
    userName = input("Enter UserName: ")
    password = input("Enter Password: ")
    validate(userName=userName, password=password)
    print("Validation completed")
          