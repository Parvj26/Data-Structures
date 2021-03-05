# Question 1
print("Question 1")
expenses=[2200,2350,2600,2130,2190]
print("Part 1 :",expenses[1]-expenses[0])
print("Part 2 :",expenses[0]+expenses[1]+expenses[2])
print("Part 3 :",2000 in expenses)
expenses.append(1980)
print("Part 4 :",expenses[5])
expenses[3] =- 200
print("Part 5 :",expenses[3])

# Question 2
print("\nQuestion 2")
heros=['spider man','thor','hulk','iron man','captain america']
print("Part 1 :",len(heros))
heros.append("black panther")
print("Part 2a :",heros[5])
heros.remove("black panther")
print("Part 2b :",heros)
heros.insert(3, "black panther")
print("Part 3 :",heros[3])
heros[1:3]=["doctor strange"]
print("Part 4 :",heros)
heros.sort()
print("Part 5 :",heros)

# Question 2
print("\nQuestion 2")
maxnum = int(input("Enter max number: "))
odd_num = []
for i in range(maxnum):
    if i%2 == 1:
        odd_num.append(i)
if maxnum%2 == 1:
    odd_num.append(maxnum)
print(odd_num)   
    