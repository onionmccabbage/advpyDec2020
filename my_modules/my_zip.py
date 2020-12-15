# using Python zip (not what you might think)
# zip here means combining separate strucures into new structures

l = [1, 7, 11, 22]
t = (10, 20 ,30, 40, 50)

z = list( zip(t, l) ) # stops when one of the collections is exhausted

print( z )