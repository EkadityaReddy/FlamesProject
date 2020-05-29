name1 = input("ENTER FIRST NAME WITHOUT SPECIAL CHAR , NUMBERS , SPACES:")
name2 = input("ENTER SECOND NAME WITHOUT SPECIAL CHAR , NUMBERS , SPACES:")
name1 = name1.lower()
name2 = name2.lower()
for i in name1 :
    if i in name2:
        name1 = name1.replace(i,'',1)
        name2 = name2.replace(i,'',1)
print("NAMES after CANCELLING LETTERS COMMON : " , name1 ," , " , name2)
count = len(name1) + len(name2)
print("flames")
print("Number of letters remained after canceling : ",count)
flames = "FLAMES"
for i in range(1,6):
    x = count%len(flames)
    y = flames[x-1]
    flames = flames.replace(y,'',1)
    print(flames)
    print(len(flames))
if flames == 'F':
    print("FRIENDS")
elif flames == "L":
    print("LOVERS")
elif flames == "A":
    print("AFFECTION")
elif flames == "M":
    print("MARRAIGE")
elif flames == "E":
    print("ENEMIES")
else:
    print("SISTER")