import pandas as p
import random as r
import matplotlib.pyplot as plt


def op1():
        #generate random floats and give each a color
    L = generateFloats(x = 1000,y=3)
    for i in L:
        print(i)
    df = p.DataFrame(L,columns = ["x","y","c"])
    ax1 = df.plot.scatter(x = "x",y = "y",c="c",colormap="viridis")
    plt.show()

def op2():
    L = generateFlips(x = 1000,y=100)
    dist = [0]*(len(L[0])+1)
    for i in range(len(L)):
        #print(L[i])
        dist[sum(L[i])] += 1
    print(dist)
    df = p.DataFrame(dist)
    ax = df.plot.bar(rot = 0)
    plt.show()

def generateFloats(x = 10,y = 2):
    #x: 1st deminsion of floats
    #y: 2nd deminsion of floats // fix spelling
    L = []
    for i in range(x):
        sub = []
        for j in range(y):
            sub.append(r.random())
        L.append(sub)
    return L

def generateFlips(x = 100, y = 10):
    #x = number of senerios to run
    #y = collection of coinflips // reword
    L = []
    for i in range(x):
        sub = []
        for j in range(y):
            sub.append(r.randint(0,1))
        L.append(sub)
    return L


def main():
    print("start")
    #op1()
    op2()


    print("end")
main()