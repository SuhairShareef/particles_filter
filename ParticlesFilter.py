import random
from turtle import distance
from Particle import *
from matplotlib import pyplot as plt
from math import *
import string


class ParticlesFilter:
    """ A class that represents a particle filter applied on a robot with 1D movement
        The robot moves either forward or backward. The map is a 1D array that has 
        letters instead of actual barriers and walls so the robot can see if the position
        its at is similar to any other particle that has the same letter
    """

    def __init__(self, path_length=100, no_of_particles=50, robot_init_postion=0):
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
        self.robot = Particle(weight=1, position=robot_init_postion)    # The robot itself is a particle
        self.error_probability = dict.fromkeys(
            string.ascii_lowercase, 0)

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
            w = 1 / self.no_of_particles
            p = random.randint(0, self.path_length - 1)
            d = 'f' # Rondomizing the direction
            self.particles.append(Particle(weight=w, position=p, direction=d))



    def generate_path(self, char_start, char_end):
        """ Generates the path with random alphabits on each position

        Args:
            char_start (char): starting range of the desired letters
            char_end (char): ending range of the desired letters
        """
        for i in range(self.path_length // 5):
            char = self.get_random_char(char_start, char_end)
            for j in range(5 * i, i * 5 + 5):
                self.path[j] = char
    

    
    def generate_probability(self):
        for alpha in self.error_probability:
            self.error_probability[alpha] = random.uniform(0, 2)  
        print(self.error_probability)



    def get_random_char(self, char_1, char_2):
        rand = random.randint(ord(char_1), ord(char_2))
        return chr(rand)



    def move(self, steps):
        self.alpha_counter = dict.fromkeys(string.ascii_lowercase, 0)
        robot_prev_dir = self.robot.direction
        self.robot.move_particle(steps, 0, self.path_length)
        Z = self.path[self.robot.position]
        particle_pos = None

        # to check if the robot changed its direction
        change_direction = (robot_prev_dir != self.robot.direction)

        for i in range(len(self.particles)):
            if change_direction:
                if self.particles[i].direction == 'f':
                    self.particles[i].direction = 'b'
                else:
                    self.particles[i].direction = 'f'
            
            distance = abs(self.particles[i].position - self.robot.position)
            if distance == 0:
                distance = 1

            self.particles[i].move_particle(steps, 0, self.path_length)
            particle_pos = self.path[self.particles[i].position]

            hit = (Z == particle_pos)

            # if hit or miss
            if hit:
                self.particles[i].weight *= (1 - self.error_probability[Z]) 
            else:
                self.particles[i].weight *= self.error_probability[particle_pos] 
            
            self.particles[i].weight /= distance



    def normalize(self):
        norm_arr = []
        max_val = max(self.particles).weight
        min_val = min(self.particles).weight

        diff_arr = max_val - min_val

        for i in range(len(self.particles)):
            temp = 1.e-10
            if diff_arr != 0:
                temp = (self.particles[i].weight - min_val) / diff_arr

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
        for i in range(len(self.particles)):
            if abs(self.particles[i].position - self.robot.position) < 10:
                print(self.particles[i])
                
            if not weights:
                weights.append(self.particles[i].weight)
            else:
                weights.append(self.particles[i].weight + weights[-1])
        
        print(min(self.particles).weight, max(self.particles).weight)

        for _ in range(self.no_of_particles):
            index = self.get_random_index(weights)
            indexes.append(index)
            particle = Particle(self.particles[index].weight, self.particles[index].position,
                                self.particles[index].direction, self.particles[index].pos)
            new_particles.append(particle)

        self.particles = new_particles.copy()
        new_particles.clear()



    def get_random_index(self, weights):
        # print(weights)
        N = random.uniform(0, 1)

        for index, weight in enumerate(weights):
            if N <= weight:
                return index



    def stop(self, threshold):
        for i in range(len(self.particles)):
            if abs(self.particles[i].position - self.robot.position) > threshold:
                return False
        return True



    def draw(self):
        positions = [self.particles[i].position for i in range(
            len(self.particles))]
        y = []
        for i in range(self.no_of_particles):
            y.append(random.uniform(0, 0.5))

        plt.xlim(0, 100)
        plt.ylim(0, 2)
        plt.margins(x=1, y=0)
        plt.scatter(positions, y, marker="o")
        plt.plot([self.robot.position], [0.5], marker="o", markersize=10,
                 markeredgecolor="green", markerfacecolor="red")
        plt.xticks([i for i in range(self.path_length)], self.path)

        plt.draw()
        plt.pause(0.0001)
        plt.clf()
