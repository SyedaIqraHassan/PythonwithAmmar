# # while loop
x=0
while (x<=5):
    print(x)
    x=x+1

# for loops
for x in range(3,8):
     print(x)

# #array
days=["MON","TUE","WED","THURS","FRI","SAT","SUN"]
for d in days:
        print(d)

#array
days=["MON","TUE","WED","THURS","FRI","SAT","SUN"]
for d in days:
    if(d=="FRI"):break
    print(d)

#array
days=["MON","TUE","WED","THURS","FRI","SAT","SUN"]
for d in days:
    if(d=="FRI"):continue
    print(d)