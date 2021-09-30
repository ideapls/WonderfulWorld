import matplotlib.pyplot as plt
from knapsack import KnapsackSolver
from superGraphics import TestApp

number_generations = 6
sg = TestApp()
knps = KnapsackSolver(elite_size=2, mutation_probability=0.2, crossover_probability=0.9, number_genes=6,
                      population_size=6, load_capacity=30)
population = knps.create_population()

sg.run()
knps.infos()

elite = [None] * len(population)
elite = knps.sort_population(population)[(len(population) - knps.elite_size):]
print('Elite inicial:\n')
for i in elite:
    print('Indivíduo: {} | Valor: {} | Peso: {}\n'.format(
        i, knps.fitness(i), knps.calculate_load(i)))
print('Realizando o crossover e mutação para {} gerações...\n'.format(
    number_generations))
generations = []
generation_fitness = []
for i in range(number_generations):
    generations.append(i + 1)
    generation_fitness.append(
        knps.fitness(knps.sort_population(population)[knps.population_size - 1]))
    population = knps.selection_and_crossover(population)
    population = knps.mutation(population)
print('Elite final:\n')
elite = knps.sort_population(population)[(len(population) - knps.elite_size):]
for i in elite:
    print('Indivíduo: {} | Valor: {} | Peso: {}\n'.format(
        i, knps.fitness(i), knps.calculate_load(i)))

plt.plot(generations, generation_fitness)
plt.title('Evolução do fitness')
plt.xlabel('Gerações')
plt.ylabel('Fitness')
plt.show()
