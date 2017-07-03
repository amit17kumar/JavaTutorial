import sysconfig

#Method 1
# a = [0,-2,3,-4,-5,6,-7]
# max = -((sysconfig.sys.maxsize)-1)
# for i in range(6):
#     Sum = a[i] + a[i+1]
#     if Sum > max:
#         max = Sum
# print("Maximum sum of two consecutive numbers in the given array is: " + str(max))
        

#Method 2
a = [0,-2,3,-4,5,6,-7]
b = []
for i in range(6):
    b.append(a[i] + a[i+1])

print("Maximum sum of two consecutive numbers in the given array is: " + str(max(sorted(b))))