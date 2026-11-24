"""Pra:4)function with parameter and function  with return type"""

db = {

    "user_name" :"",
    "email":"",
    "password":""
}


def signup(username,email,password):

     if username in db.keys():
      return "user already exits !"
     else:
         db["user_name"] = username
         db["email"] = email
         db["password"] = password
         return "successfully registered ! "

def signin(email,password):

    print("----->",db.keys())

    print("----->email",db["email"])

    if db["email"] in db.keys():

       if db["email"] == email and db["password"] == password:
         
         return f"hello {db['user_name']}" 
       else: 
          return "invalid details"
    else:
          return "user does't exits" 
    
    
menu = """MENU: 
1) PRESS 1 FOR REGISTERATION
2) PRESS 2 FOR LOGIN"""  


print(menu)
status = True

while status:

   choice = input("enter your choice :")

   if choice == 1:
     print("Registration form")
     name = input("Enter your name:")
     email = input("Enter your email")
     password= input("Enter your password")

     print(signup(name,email,password))  #function calling with parameters

   elif choice == 2:

     pass

   else:
    ("Invalid input")  



exit_choice =input("do you want to continue ? 1/yes for yes and 2/no for no")

if exit_choice == "yes" or exit_choice == "y" or exit_choice == 1:

      status = True
else:
     status = False

