import random
from Particle import *
from matplotlib import pyplot as plt
from math import *


class ParticlesFilter:
    """ A class that represents a particle filter applied on a robot with 1D movement
        The robot moves either forward or backward. The map is a 1D array that has 
        letters instead of actual barriers and walls so the robot can see if the position
        its at is similar to any other particle that has the same letter
    """
    
    
    def __init__(self, path_length=100, no_of_particles=50, p_hit=0.8, p_miss=0.6, robot_init_postion=0):
        """ The constructor

        Args:
            path_length (int): The length of the path for the map. Defaults to 100.
            no_of_particles (int): Defaults to 50.
            p_hit (float): Used to decrease weight when the sensed data doesn't equal the actual data
                           Defaults to 0.8.
            p_miss (float): used to increase weight when the sensed data doesn't equal the actual data
                           Defaults to 0.6.
            robot_init_postion (int): The initial location of the robot. Defaults to 0.
        """
        self.path_length = path_length
        self.no_of_particles = no_of_particles
        self.p_hit = p_hit
        self.p_miss = p_miss
        self.robot = Particle(1, robot_init_postion)    # The robot itself is a particle

        self.particles = []
        self.path = [0] * self.path_length
        
        plt.ion()
        plt.rcParams["figure.figsize"] = [20.00, 3.50]
        plt.rcParams["figure.autolayout"] = True

    def generate_random_particles(self):
        """ Generates particles with random postion in the path and random direction. 
            The weights assigned is equal to 1 / number of particles
        """
        for _ in range(self.no_of_particles):
            weight = 1 / self.no_of_particles
            position = random.randint(0, self.path_length - 1)
            direction = random.choice(['f', 'b'])   # Rondomizing the direction
            self.particles.append(Particle(weight, position, direction))

    def generate_path(self, char_start, char_end):
        """ Generates the path with random alphabits on each position

        Args:
            char_start (char): starting range of the desired letters
            char_end (char): ending range of the desired letters
        """
        for i in range(self.path_length):
            self.path[i] = self.get_random_char(char_start, char_end)

    def get_random_char(self, char_1, char_2):
        rand = random.randint(ord(char_1), ord(char_2))
        return chr(rand)

    def move(self, steps):
        robot_prev_dir = self.robot.direction
        self.robot.move(steps, 0, self.path_length)
        # to check if the robot changed its direction
        change_direction = robot_prev_dir == self.robot.direction

        for particle in self.particles:
            if change_direction:
                if particle.direction == 'f':
                    particle.direction = 'b'
                else:
                    particle.direction = 'f'

            particle.move(steps, 0, self.path_length)

            distance = abs(self.robot.position - particle.position)
            if distance == 0:
                distance = 10e-9
            hit = (self.path[self.robot.position] ==
                   self.path[particle.position])

            # if hit or miss
            if hit:
                particle.weight = (self.p_hit * sqrt(distance))
            else:
                particle.weight = (self.p_miss / sqrt(distance))

    def normalize(self):
        norm_arr = []
        max_val = max(self.particles).weight
        min_val = min(self.particles).weight

        diff_arr = max_val - min_val

        for particle in self.particles:
            temp = 1.e-10
            if diff_arr != 0:
                temp = (particle.weight - min_val) / diff_arr

            norm_arr.append(temp)

        sum_of_weights = sum(norm_arr)
        ssum = 0

        for i in range(self.no_of_particles):
            self.particles[i].weight = norm_arr[i] / sum_of_weights
            ssum += self.particles[i].weight

    def sample(self):
        new_particles = []
        indexes = []

        # extract weights
        weights = []
        for particle in self.particles:
            if not weights:
                weights.append(particle.weight)
            else:
                weights.append(particle.weight + weights[-1])
            # print('{:.20f}'.format(weights[-1]))

        for _ in range(self.no_of_particles):
            index = self.get_random_index(weights)
            indexes.append(index)
            new_particles.append(self.particles[index])

        print(indexes)

        self.particles = new_particles.copy()
        new_particles.clear()

    def get_random_index(self, weights):
        # print(weights)
        N = random.uniform(0, 1)

        for index, weight in enumerate(weights):
            if N <= weight:
                return index

    def stop(self, threshold):
        for particle in self.particles:
            if abs(particle.position - self.robot.position) > threshold:
                return False
        return True

    def draw(self):
        positions = [particle.position for particle in self.particles]
        y = []
        for i in range(self.no_of_particles):
            y.append(random.uniform(0,0.5))

        plt.xlim(0, 100)
        plt.ylim(0, 2)
        plt.margins(x=1, y=0)
        plt.scatter(positions, y, marker="o")
        plt.plot([self.robot.position], [0.5], marker="o", markersize=10,
                markeredgecolor="green", markerfacecolor="red")
        plt.xticks([i for i in range(self.path_length)], self.path)
        plt.yticks(y)
        plt.draw()
        plt.pause(0.0001)
        plt.clf()