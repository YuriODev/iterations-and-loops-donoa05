# Your solution to Exercise 31
days=int(input("Enter the number of days:"))
temp=[]

for i in range (days):
  temperature=int(input(f"Enter the temperature for day {i+1}:"))
  temp.append(temperature)
temp.sort()
print(temp[0])

if temp[0]>-18:
  print("No")
else:
  print("Yes")
  
