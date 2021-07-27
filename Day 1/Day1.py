a = input("please enter the values : ")
x = [int(i) for i in a.split()]
x.sort()
x.reverse()
print("The descending order for the sequence is:",x)