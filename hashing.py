__author__ = 'Azi'
import hashlib

def hash_password(password):
    salt = 'Azimuthal'
    return hashlib.sha256(salt.encode() + password.encode()+salt.encode()).hexdigest()

flag=0
new_pass = input('Please enter a username: ')

try:
    f = open('foo.txt', 'r')
except Exception:
    f=open('foo.txt','w')
    f.close;
    f=open('foo.txt','r')
for line in f:
    li=line.split()
    if li[0]==new_pass:
        flag=1
        print(li[1])
        break
f.close()
if flag==0:
    hashed_password = hash_password(new_pass)
    print('The string to store in the db is: ' + hashed_password[0:11])
    old_pass = input('Now please enter the username again to check: ')
    if new_pass==old_pass:
        f=open('foo.txt','a')
        f.writelines(new_pass+' '+hashed_password[0:11]+'\n')
        f.close()
    else:
        print('I am sorry but the password does not match')
