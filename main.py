#main.py
#Nicholas Norman
#March 2024

from typing import List
from setup import Animal
from setup import D
import setup
import random

initial_pop = setup.initial_pop
round_count = setup.round_count

def customValues(initial_pop, round_count):
    #take in input
    val = input(f"Initial Population (Default: {initial_pop}): ")
    if(val != ""):
        #hit enter to keep default
        val = int(val)
        initial_pop = val
    
    val = input(f"# of Rounds (Default: {round_count}): ")
    if(val != ""):
        #hit enter to keep default
        val = int(val)
        round_count = val

    return [initial_pop, round_count]
    
[initial_pop, round_count] = customValues(initial_pop, round_count)

#show simulation variables
print("--------------------------------------")
print("SIMULATION STARTING WITH...")
print("--------------------------------------")
print(f"Intial Population:              {initial_pop}")
print(f"Number of years:                {round_count}")
print(f"Intial Life Expectancy:         {setup.initial_expec}")
print(f"Intial Mutation Coeff:          {setup.initial_mut}")
print(f"Max years gained from Mutation: {setup.t_max}")
print(f"Offspring per Pregnancy:        {setup.offspring}")
print(f"Chance of death at birth:       {setup.Death.d_born}%")
print(f"Chance of death at max age:     {setup.Death.d_death}%")
print(f"Chance of death modeled:        linear")
print("--------------------------------------")

#setup initial population
pop: List[Animal] = []

#if pop is dead, dont print any longer
isExtinct:bool = False

for i in range(initial_pop):
    pop.append(Animal())

#establish starter
Animal.initPopEstablished = True

#run rounds (years)
for year in range(1,round_count+1):
    
    length = len(pop)
    i = 0
    while (i < length):
        #increase age by one
        pop[i].incr_age()
        #check if dead
        if(Death.isDead(pop[i].age, pop[i].life_expec)):
            #kill animal
            pop.pop(i)
            i -= 1
            length -= 1

        i += 1

    adults = len(pop)
    children = len(pop) // 2
    
    ###mating

    #randomly move around
    random.shuffle(pop)

    length = len(pop)
    if (length % 2 != 0):
        length -= 1
    j = 0
    while (j < length):
        #take two parents and create a child,
        child = Animal(pop[j].life_expec, pop[j+1].life_expec)
        
        #add child to general population
        pop.append(child)

        #skip by 2
        j += 2

    if(len(pop) != 0):
        print(f"year: {year} | Adults: {adults} + Children: {children} | Avg Age: {setup.getAvgAge(pop):.2f} | Avg Life Expec {setup.getAvgLE(pop):.2f} | Avg Mutation {setup.getAvgMut(pop):.3f}")
    else:
        if(isExtinct == False):
            print("All Animals have gone exctinct")
        isExtinct = True
        break


if (isExtinct == False):
    print(f"Life Expectancy Increase: {setup.getAvgLE(pop) - setup.initial_expec:.2f}")

dummy = input()
