file1 = "Letters.txt"

with open(file1,"r+") as file2:
    content = file2.readlines()

print(content)    

content = [i.strip("\n") for i in content if "\n" in i] 

print(content)  

