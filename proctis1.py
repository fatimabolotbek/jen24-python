    
import re
while True:
    password = input(" Enter your password:")
    if len(password) < 8: 
        print("Password muse be accepted 8 characters")
    elif not re.search ('[A-Z]', password):
        print("password muse be acceptet list one uppercase letter.")
    elif not  re.search ('[a-z]', password):       
        print ("password muse be acceptet list one lowercase letter")
    elif not re.search ('[0-9]', password):
        print("Password must contain at least one numbe")
    elif not re.search('[#@^%$^]', password):
        print("Password must contain at least one special character")
    else:
        print ("password accepted")
        break
    















