import random
import pandas as pd

objects = pd.read_csv('objetos.txt', sep=';')
number_genes = len(objects)


class KnapsackSolver:

    def __init__(self, elite_size, mutation_probability, crossover_probability, number_genes,
                 population_size, load_capacity):
        self.elite_size = elite_size
        self.mutation_probability = mutation_probability
        self.crossover_probability = crossover_probability
        self.number_genes = number_genes
        self.population_size = population_size
        self.load_capacity = load_capacity

    def individual(self):
        individual = [random.randint(0, 1) for i in range(number_genes)]
        self.validate(individual)
        return individual

    def validate(self, individual):
        load = self.calculate_load(individual)
        less_position = 0
        values = sorted(objects['valor'])
        while load > self.load_capacity:
            load = 0
            less = values[less_position]
            index = objects['valor'].values.tolist().index(less)
            individual[index] = 0
            less_position += 1
            load = self.calculate_load(individual)

    def create_population(self):
        return [self.individual() for i in range(self.population_size)]

    def fitness(self, individual):
        fitness = 0
        for i in range(len(individual)):
            if individual[i] == 1:
                fitness += objects.at[i, 'valor']
        return fitness

    def calculate_load(self, individual):
        load = 0
        for i in range(len(individual)):
            if individual[i] == 1:
                load += objects.at[i, 'peso']
        return load

    def selection_and_crossover(self, population):
        scored = self.sort_population(population)
        population = scored
        elite = population[(len(population) - self.elite_size):]
        for i in range(len(population) - self.elite_size):
            if random.random() <= self.crossover_probability:
                point = random.randint(1, number_genes - 1)
                parents = random.sample(elite, 2)
                population[i][:point] = parents[0][:point]
                population[i][point:] = parents[1][point:]
                self.validate(population[i])
        return population

    def mutation(self, population):
        for i in range(len(population) - self.elite_size):
            if random.random() <= self.mutation_probability:
                point = random.randint(0, number_genes - 1)
                new_value = random.randint(0, 1)
                while new_value == population[i][point]:
                    new_value = random.randint(0, 1)
                population[i][point] = new_value
                self.validate(population[i])
        return population

    def sort_population(self, population):
        return [i[1] for i in sorted([(self.fitness(j), j) for j in population])]

    def infos(self):
        print('-' * 45)
        print('Algoritmo da Mochila')
        print('-' * 45)
        print('Número de genes dos indivíduos: {}\n'.format(number_genes))
        print('Taxa de crossover: {}%\n'.format(self.crossover_probability * 100))
        print('Taxa de mutação: {}%\n'.format(self.mutation_probability * 100))
        print('Tamanho da população: {} indivíduos\n'.format(self.population_size))
        print('Elitismo: {} indivíduos\n'.format(self.elite_size))
        print('Peso máximo suportado pela mochila: {}'.format(self.load_capacity))
        print('-' * 45)
        print('\n')
