import re

username = input("What is your username?")
password = input("What is your password?")

x= re.findall("\d", username)
y= re.findall("[A-Z]", username)
a= re.search("[a-zA-Z]", password[0])
b= re.search("[a-zA-Z]", password[1])
c= re.search("[a-zA-Z]", password[2])
d= re.search("[a-zA-Z]", password[4])
e= re.search("[a-zA-Z]", password[5])
f= re.search("[a-zA-Z]", password[6])
g= re.search("[0-9a-z]", password[7])
h= re.search("[0-9a-z]", password[8])
i= re.search("[0-9a-z]", password[9])
j= re.search("[0-9a-z]", password[10])


if (x):
    print("FALSE, not the correct usename")
elif len(username)<=3 and len(username)>=5:
    print("FALSE, not the correct username")
elif (y):
    print("FALSE, not the correct username")
elif len(password)!=11:
    print("FALSE, not the correct password")
elif (password[3]!="-"):
    print("FALSE, not the correct password")
elif (a):
    print("FALSE, not the correct password")
elif (b):
    print("FALSE, not the correct password")
elif (c):
    print("FALSE, not the correct password")
elif (d):
    print("FALSE, not the correct password")
elif (e):
    print("FALSE, not the correct password")
elif (f):
    print("FALSE, not the correct password")
elif (g):
    print("FALSE, not the correct password")
elif (h):
    print("FALSE, not the correct password")
elif (i):
    print("FALSE, not the correct password")
elif (j):
    print("FALSE, not the correct password")
else:
    print("TRUE, Welcome" + username)