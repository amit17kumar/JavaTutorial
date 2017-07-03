while True:
    I = raw_input("Please enter the Words:")
    if I == "CLOSE":
        break
    else:
        with open("Letters.txt",'a+') as file1:
            file1.write(I +"\n")
print("Your entry is saved into the file Letters")
