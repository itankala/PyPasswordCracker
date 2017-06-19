import hashlib
import time
import itertools # all of these imports are the needed libraries, hashlib for hashing, time for time features, itertools for getting the combinations
hashes = []
file = open("hashes.txt", "r")
for i in range(0, 8):
    hashes.append(file.readline()[:-1])  #puts all of the password hashes in an array
for i in range(0,7):   #cracks passwords up to length 8
    start = time.clock() #begins timing for each hash
    combinations=itertools.combinations_with_replacement(' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-+=`~\|]}[{;:/?.>,<', i) #function used to create a massive list of all combinations of the characters, i defines the size of the combinations generated
    for word in combinations:  #checks each combination
        if hashlib.md5(''.join(word).encode(encoding='UTF-8', errors='strict')).hexdigest() in hashes: #hashes the combination and checks if in the array
            print "Password: " , (''.join(word))
            print "Solved in " ,    time.clock()-start , "seconds"

