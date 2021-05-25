from tkinter import *

import numpy as np, numpy.random
X=0

import simuPOP as sim

from simuPOP.utils import export

import os



def runsimbby():
    Pop = int(poop.get())
    Gen = int(gen.get())
    Rep = int(rep.get())
    Fre = [0]
    Fre.extend([float(y) for y in (fre.get()).split(",")])

    print("rep is: ", Rep)

    dir = os.path.dirname(__file__)

    filename = os.path.join(dir, '/Data_csv')

    newpath = dir + '/Data_csv'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    for X in range (0,Rep):
        +X

        pop = sim.Population(Pop, ploidy=2,loci=[1])
        sim.initSex(pop)

        sim.initGenotype(pop, freq=Fre, loci=0)
        export(pop, format='CSV' ,affectionFormatter={False: X, True: X}, output = dir + filename + "/simSTART%d.csv" % (X))

        pop.evolve(	
	        	matingScheme=sim.RandomMating(),
		    gen=Gen
		)


        export(pop, format='CSV' , affectionFormatter={False: X, True: X} ,output= dir + filename + "/simEND%d.csv" % (X))


    fout=open(dir + "/simStartTotal.csv","a")

    for line in open(dir + filename + "/simSTART1.csv"):
	    fout.write(line)
	   
    for num in range(2,Rep+1):
        f = open(dir + filename + "/simSTART"+str(num)+".csv")
        f.next()
        for line in f:
            fout.write(line)
        f.close()
    fout.close()

    fout=open(dir + "/simEndTotal.csv","a")

    for line in open(dir + filename + "/simEND1.csv"):
	    fout.write(line)
	   
    for num in range(2,Rep+1):
        f = open(dir + filename + "/simEND"+str(num)+".csv")
        f.next()
        for line in f:
            fout.write(line)
        f.close()
    fout.close()


main = Tk()
main.geometry('{}x{}'.format(300, 150))
main.wm_title("Gabe's SimuPOP simulation")
label = Label(main, text = "Population Size")
label.pack()
poop = Entry(master = main)
poop.pack()
label = Label(main, text = "Number of genarations")
label.pack()
gen = Entry(master = main)
gen.pack()
label = Label(main, text = "Number of Replicates")
label.pack()
rep = Entry(master = main)
rep.pack()
label = Label(main, text = "Allele Frequencies")
label.pack()
fre = Entry(master = main)
fre.pack()
submitGuess = Button(master = main, text = "Run simulation", command = runsimbby)
submitGuess.pack()


main.mainloop()


