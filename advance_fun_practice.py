# this is a challenge
# define a function taking any num of list containing number
# example-[1,2,3],[2,5,6],[2,3,4]....
# return average like
# (1+2+2/3),(2+5+6/3)....
# try to do this in lambda
#Normal process 
def average_fun(*args):
    both=[]
    for i in zip(*args):
        both.append(sum(i)/len(i))
    return both
print(average_fun([1,2,3],[2,5,6],[4,7,8]))   
#With lambda function
average_list=lambda *args:[round(sum(i)/len(i),4) for i in zip(*args)]
print(average_list([1,2,3],[2,5,6],[4,7,8]))