Simulation

what are we testing? How does life expectancy change in a population.

Independent Variable:
Chance of Death, D

Dependent Variable:
Life Expectancy, L

D(t) = 4*d(t/lmax - 1/2)^2 = Chance of Death at a given age

where t is age of the animal
and d is max percent of death at birth & death
and lmax is the max age of an animal (life excpectancy)

How will the simulation be conducted?
Animal A, is composed of a life expectancy lmax, age t, and a mutation rate of k
There will be an inital population of an animal, A1
Rounds will be conducted by year, i.e. t = # of years since 0
Every year, animals will form into pairs and mate to create N offspring
When a new child is born they will start at age 0
They will have a life expectancy equal to (parent1 + parent2)/2 + (k*tmax) where tmax is max years gained from mutation
after all births, the death function is run, and animals are eliminated
if an animal lives to max age, then they will die the next round