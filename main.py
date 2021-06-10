import os
import requests
import random
import string

genEmail = True
providerEmail = ""
chars = string.ascii_letters + string.digits + ')(*&^%$£"!'
random.seed = (os.urandom(1024))        
url = 'scammer'

loop = True 
while (loop == True):
    names = random.randint(0, len(chars)-1)
    passwords = random.randint(0, len(chars)-1)
    check = random.randint(0, 1)

    if (genEmail == True):
        globe = random.randint(0, 2)
        globe = genEmail.domain(globe)
        providerEmail = globe

name_extra = ''.join(random.choice(string.digits))

username = chars + '@purelxw.me'
password = ''.join(random.choice(chars) for i in range(80))

requests.post(url, allow_redirects=False, data={
    'username': username,
    'password': password
})

print('Sending username [' + username + '] and password [' + password + ']') 