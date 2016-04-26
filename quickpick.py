import random
numList=[]
show=""
counter=0
check=True
user_input=int(input("How many quick picks?"))
for column in range(0,user_input):
    for i in range(0,6):
        randNum=random.randint(1,45)
        if i==0:
            numList.append(randNum)
        else:
            while check==True:
                for data in numList:
                    if randNum==data:
                        randNum=random.randint(1,45)
                numList.append(randNum)
                check=False
        check=True
    numList.sort()
    for j in numList:
        show+="{:4}".format(j)
        if counter==5:
            show+="\n"
        counter+=1
    counter=0
    numList=[]
print(show)