users = ['Ashish','Khushi','Rakhi','Rimjhim']

user_name = raw_input("Please enter the username:") 
if user_name in users:
    pass_word = raw_input("Please enter the Password")
else:
    print("User doesnot exist")
    pass_word = []
while True:
    if not any(i.isdigit() for i in pass_word):
        print("Password should contain atleast 1 number")
    break
        
