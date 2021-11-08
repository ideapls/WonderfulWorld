import matplotlib.pyplot as plt
from knapsack import KnapsackSolver
from superGraphics import TestApp

sg = TestApp()
knps = KnapsackSolver(elite_size=2, mutation_probability=0.2, crossover_probability=0.9, number_genes=6,
                      population_size=6, load_capacity=30)
population = knps.create_population()
generations_and_gfitness = knps.solve(population, knps.number_genes)
generations = generations_and_gfitness[0:1]
gfitness = generations_and_gfitness[1:]

knps.infos()

plt.scatter(*generations, *gfitness)

#plt.plot(generations, generation_fitness)
plt.title('Evolução do fitness')
plt.xlabel('Gerações')
plt.ylabel('Fitness')
plt.show()

sg.run()
