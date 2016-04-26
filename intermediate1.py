num=[]
total=0
for i in range(0,5):
    num_input=int(input("Number:"))
    num.append(num_input)
    total+=num_input
average=total/5
print("The first number is ",num[0])
print("The last number is ",num[-1])
print("The smallest number is ", min(num))
print("The largest number is ",max(num))
print("The average of the numbers is ", average)