import pandas as p
import random as r
import matplotlib.pyplot as plt

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


def main():
    print("start")
    L = generateFloats(x = 100,y=2)
    for i in L:
        print(i)
    
    #df = p.DataFrame(L[0],L[1],columns = ["x","y"])
    df = p.DataFrame(L,columns = ["x","y"])
    ax1 = df.plot.scatter(x = "x",y = "y")
    plt.show()


    print("end")
main()