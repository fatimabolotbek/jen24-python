

 
#  password = input("Enter user password")
#  if password < 8
#   print(len(password))
# else 
# if isupper(passwod)<

 

#  1.len(passwod)
#  2. in or isupper()
#  3. in or islower()
#  4. in or isdigit()
#  5. in 

password = input(" Enter your passw")
if len(password) > 8 or len(password) < 8:
    print("Password muse be accepted 8 characters.")
else:
    if any(let.isupper() for let in password):
        print("password muse be acceptet list one uppercase letter.")
    
    if   any(let.islower() for let in password):       
         print ("password muse be acceptet list one lowercase letter")
    if    any(let.isdigit() for let in password):
        print("Password must contain at least one numbe")

    if any(let in "#$%&*@!" for let in password)
       print("Password must contain at least one special character")
       else:
        print ("password eccsepted")
        break
    


