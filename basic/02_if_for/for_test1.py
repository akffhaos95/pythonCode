test_str = "abcdefghijklmnopqrstuvwxyz"
test_list = ['one', 'two', 'three']
test_tuple = (1,2,3,4,5,6,7,8,9)
test_dict = {"one" : 1, "two" : 2, "three" : 3}
test_set = {1,2,3,4,5,6,7,8,9}
for i in test_str:
    print(i, end=",")
print("\n")
for i in test_list:
    print(i, end=",")
print("\n")
for i in test_tuple:
    print(i, end=",")
print("\n")
for i,j in test_dict.items():
    print(i,"~~~~~~~~~~",j, end=",")
print("\n")
for i in test_set:
    print(i, end=",")
print("\n")
for i in range(10):
    print(i, end=",")
print("\n")
for i in range(1, 10):
    for j in range(2, 10):
        print(j,"x",i,"=",i*j, end=", ")
    print("\n")

a = [1,2,3,4,5]
result = [num*3 for num in a if num%2 == 0]
print(result)

result = [x*y for x in range(2,10) for y in range(1,10)]
print(result)
