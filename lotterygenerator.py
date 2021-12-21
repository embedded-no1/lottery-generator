from random import *
import numpy as np
import sys
numlotterynumbers=int(input("How many numbers are in your lottery?"))
maxnumber=int(input("What is your max lottery number?"))
powerballmaxnumber=int(input("What is your max powerball number?"))
numberofplays=int(input("How many plays are we playing today?"))

print (numlotterynumbers,maxnumber,powerballmaxnumber)
#lotterynumbers=randint(1,maxnumber)
#lotterynumbers = np.random.sample(range(maxnumber+1),numlotterynumbers)
data = []
powerball = []
sys.stdout.close()
def unique_rand(inicial, limit, total):

        data = []

        i = 0

        while i < total:
            number = randint(inicial, limit)
            if number not in data:
                data.append(number)
                i += 1

        return data
j=1
while j <= numberofplays:
    data = unique_rand(1,maxnumber,numlotterynumbers)
    powerball = unique_rand(1,powerballmaxnumber,1)
    sys.stdout = open("lottery.txt","a+")
    print (data,("powerball"),powerball)

    j=j+1
    
sys.stdout.close()