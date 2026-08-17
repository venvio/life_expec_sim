#Setup for all variables and functions
#Nicholas Norman
#March 2024

import random
from typing import List

#initial population of animals
initial_pop = 10

#initial life expectancy in years
initial_expec = 10

#inital mutatation constant
initial_mut = 0

#maximum years gained from one mutation
t_max = 2

#round count in years
round_count = 100

#amount of offspring from reproduction
offspring = random.randint(1,3)

#chance of death at time t
class Death:

    def __init__(self):
        pass

    #percent chance of death at age 0
    d_born = 10
    d_death = 100


    def __call__(self, age, lmax):
        return self.death_chance(age, lmax)

    @staticmethod
    def death_chance(age, lmax):
        #death = 4*Death.d*((age/lmax - 1/2)**2)
        #make linear
        m = (Death.d_death - Death.d_born)/(lmax)
        chance = m*age+Death.d_born
        #round to int
        chance = round(chance)
        
        return chance
    
    @staticmethod
    def isDead(age, lmax):
        # calculate random num 0-100
        rand = random.randint(0, 100)
        # calculate chance of death
        d_chance = Death.death_chance(age, lmax)
        # if num is higher than chance of death
        if (rand > d_chance):
            # baby survives
            return False
        else:
            return True

# animal object
class Animal:
    initPopEstablished = False
    
    def __init__(self, p1:int=initial_expec, p2:int=initial_expec):
        self._age = 0
        self._first = Animal.initPopEstablished
        self._mut_rate = self.calcMutRate()
        self._life_expec = self.calcLifeExpec(p1, p2)
    
    def __str__(self):
        return f"age: {self.age}, life expec: {self.life_expec}, mut rate: {self.mut_rate}"

    def calcLifeExpec(self, p1, p2):
        #(parent1 + parent2) / 2 + (mutation rate * max years gained)
        nature = (p1 + p2) / 2
        years = nature + (self._mut_rate * t_max)
        #round to nearest year
        years = years

        return years
    
    def calcMutRate(self):
        #mutation rate can be between 0 and 1
        if(self._first != True):
            return initial_mut
        else:
            rand = random.randint(-100,100) / 100
            return rand
        
    def incr_age(self, age=1):
        self._age += age

    def getAge(self):
        return self._age

    def getLifeExpectancy(self):
        return self._life_expec

    def getMutationRate(self):
        return self._mut_rate
    
    age =        property(getAge)
    life_expec = property(getLifeExpectancy)
    mut_rate =   property(getMutationRate)
        
def getAvgMut(population:List[Animal]):
    mutSum = 0
    for ani in population:
        mutSum += ani.mut_rate
    
    return mutSum / len(population)

def getAvgLE(population:List[Animal]):
    leSum = 0
    for ani in population:
        leSum += ani.life_expec
    
    return leSum / len(population)

def getAvgAge(population:List[Animal]):
    ageSum = 0
    for ani in population:
        ageSum += ani.age
    
    return ageSum / len(population)

#test
if __name__ == "__main__":
    d = Death()
    
    print(d(25, 100))

    a = Animal()
    b = Animal()
    
    print("a", a)
    print("b", b)

    print("adding a year")
    a.incr_age()
    b.incr_age()

    print("a", a)
    print("b", b)

    print("they are reproducing")
    Animal.initPopEstablished = True

    babies = []
    for i in range(0, 10):
        c = Animal(a.life_expec, b.life_expec)
        print(f"c[{i}]", c)
        c.incr_age(random.randint(1,100))
        babies.append(c)

    print("\ntime is dialating ...\n")

    for i in range(0, len(babies)):
        #death toll
        #calculate random num 0-100
        rand = random.randint(0, 100)
        #calculate chance of death
        d_chance = d(babies[i].age, babies[i].life_expec)
        #if num is higher than chance of death
        if (rand > d_chance):
            #baby survives
            print(f"++", babies[i].age, f"               {d_chance} vs {rand}")
        #else
        else:
            print(f"-- {babies[i].age}                {d_chance} vs {rand}")
            #dead
