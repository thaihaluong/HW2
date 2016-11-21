#1.1
color_list=["Blue","Red","Black","Pink","Brown","Yellow","Green","Violet"]
print(color_list)
l = len(color_list)
#1.2
print(color_list[3])
#1.3
n=int(input("Enter a number: 0 - 8 "))
print("Your color is : {0}".format(color_list[n]))
#1.4
print("First way:")
print(color_list)
print("Second way:")

for i in range (0,l):
    print(color_list[i])
#1.5

user_color = input("What is your favorite color? ")
if color_list.count(user_color)> 0:
    print("Your color is at index",color_list.index(user_color),"in my list")
else:
    print("Sorry, I could not find your color")
