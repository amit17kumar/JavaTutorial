Floc = "FileRead.txt"

# with open(Floc,'r+') as file1:
#     reader  = file1.readlines()
#     x = [i.strip("\n") for i in reader]
#         
# print(x)


# with open(Floc) as f:
#     for line in f:
#         print(line)
#         if 'str' in line:
#             break

with open(Floc,'r+') as file1:
    reader = file1.read()
    x = [i for i in reader]
print(x)