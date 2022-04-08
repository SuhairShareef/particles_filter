import random
import numpy as np
from particle import *
from math import *


class ParticlesFilter:
    def __init__(self, path_length=100, no_of_particles=50, p_hit=0.8, p_miss=0.2, robot_init_postion=0):
        self.path_length = path_length
        self.no_of_particles = no_of_particles
        self.p_hit = p_hit
        self.p_miss = p_miss
        self.robot_init_postion = robot_init_postion

        self.particles = []
        self.path = [0] * self.path_length
        self.robot_curr_postion = robot_init_postion

        """ self.points = np.ones(10)  # Draw 3 points for each line
        self.text_style = dict(horizontalalignment='right', verticalalignment='center',
                               fontsize=12, fontdict={'family': 'monospace'})
        self.marker_style = dict(linestyle=':', color='0.8', markersize=15,
                                 mfc="C0", mec="C0") """

    def generate_random_particles(self):
        for _ in range(self.no_of_particles):
            weight = 1 / self.no_of_particles
            position = random.randint(0, self.path_length - 1)
            self.particles.append(Particle(weight, position))

    def generate_path(self, char_start, char_end):
        for i in range(self.path_length):
            self.path[i] = self.get_random_char(char_start, char_end)

    def get_random_char(self, char_1, char_2):
        rand = random.randint(ord(char_1), ord(char_2))
        return chr(rand)

    def move(self, steps):
        if self.robot_curr_postion >= self.path_length - 1:
            self.robot_curr_postion -= 1
        else:
            self.robot_curr_postion += steps

        print("robot:" + str(self.robot_curr_postion))

        for particle in self.particles:
            if particle.position >= self.path_length - 1:
                continue
            else:
                particle.position += steps

            distance = abs(self.robot_curr_postion - particle.position)
            hit = (self.path[self.robot_curr_postion] ==
                   self.path[particle.position])

            # if hit or miss
            if hit:
                particle.weight *= self.gaussian(distance,
                                                 self.p_hit, particle.position)
            else:
                particle.weight *= self.gaussian(distance,
                                                 self.p_miss, particle.position)

    def gaussian(self, mu, sigma, x):
        # calculates the probability of x for 1-dim Gaussian with mean mu and var. sigma
        return exp(- ((mu - x) ** 2) / (sigma ** 2) / 2.0) / sqrt(2.0 * pi * (sigma ** 2))

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

        # extract weights
        weights = []
        for particle in self.particles:
            weights.append(particle.weight)
        new_particles_indecies = np.random.choice([i for i in range(
            self.no_of_particles)], self.no_of_particles, p=weights).tolist()

        #print(weights, new_particles_indecies)
        for index in new_particles_indecies:
            new_particles.append(
                Particle(self.particles[index].weight, self.particles[index].position))

        self.particles = new_particles.copy()
        new_particles.clear()

    def get_random_index(self, weights):
        # print(weights)
        N = random.uniform(0, 1)

        for index, weight in enumerate(weights):
            if N <= weight:
                return index

        raise Exception("Sorry, no numbers below zero")

    def stop(self, threshold):
        for particle in self.particles:
            if abs(particle.position - self.robot_curr_postion) > threshold:
                return False
        return True

    """ def format_axes(self, ax):
        ax.margins(0.2)
        ax.set_axis_off()
        ax.invert_yaxis()

    def split_list(self, a_list):
        i_half = len(a_list) // 2
        return (a_list[:i_half], a_list[i_half:])

    def draw(self):
        pass """

    """ x = np.array([i for i in range(self.path_length)])
    my_xticks = self.path
    plt.xticks(x, my_xticks)

    ax = plt.subplot(111)
    ax.plot(x)

    # Hide the right and top spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # Only show ticks on the left and bottom spines
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

    plt.tick_params(axis='x', which='major', labelsize=3)

    plt.tight_layout()

    plt.show()

    # Set figure limits
    ax.set_xlim((0, self.path_length))
    ax.set_ylim((0, 1))

    # Show landmarks
    ax.scatter(map.landmarks[:, 0], map.landmarks[:, 1], marker='*', color='k', label='landmarks')

    # Show particles
    ax.scatter(particles[:, 0], particles[:, 1], marker='.', color='b', alpha=0.5, label='particles')

    # Show actual position
    ax.scatter(agent.x, agent.y, marker='o', color='g', label='gt position')

    # Show ground truth path
    p = np.asarray(path_gt)
    ax.plot(p[:, 0], p[:, 1], color='g', label='gt path')

    # Append estimated pose
    path_estimated.append(pos_e)

    # Show estimated pose
    ax.scatter(pos_e[0], pos_e[1], marker='o', color='m', alpha=0.5, label='predicted position')

    # Show estimated path
    p_hat = np.asarray(path_estimated)
    ax.plot(p_hat[:, 0], p_hat[:, 1], color='m', label='predicted path')

    ax.legend(loc='upper right')

    plt.pause(.5)
    plt.cla()
"""
    """ fig, ax = plt.subplots()
    fig.subplots_adjust(left=0.4)

    self.marker_style.update(mec="None", markersize=15)
    for y, marker in enumerate(self.path[:5]):
        # Escape dollars so that the text is written "as is", not as mathtext.
        ax.plot(y * self.points, marker='$' + marker + '$', **self.marker_style)
    self.format_axes(ax)
    fig.suptitle('Path', fontsize=14)

    plt.show() """
