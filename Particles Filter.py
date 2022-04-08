'''
* localizer.py
* Author: Mohammad Altaleb
* e-mail: mohammadaltaleb@gmail.com
* the localizer is responsible for localizing a robot in a world,
* by doing sensing and moving operations and taking some measurements
* this apprroach is called monte carlo filter
'''

p = []			# probability distribution
n = 5			# number of cells in the world

# initializing a uniform distribution
for i in range(n):
    p.append(1.0 / n)

world = ['green', 'red', 'red', 'green', 'green']			# the world to operate in
pHit = 0.6                  # multiply the probability by pHit if it correspond to the measurement
pMiss = 0.2                 # multiply the probability by pMiss if it does not correspond to the measurement
pExact = 0.8                # multuply the probability by pExact if the robot performed an exact motion
pOvershoot = 0.1            # multuply the probability by pOvershoot if the robot performed an inexact motion and it overshooted
pUnershoot = 0.1            # multuply the probability by pUnershoot if the robot performed an inexact motion and it undershooted

# this function takes the probability distribution and a measurement of the world
# then it returns a new probability distribution that is more accurate based on the given measurement
# if the cell corresponds to the measurement, it is multiplied by pHit
# if the cell does not corresponds to the measurement, it is multiplied by pMiss
# after the multiplication process, the values in the new probability distribution is normalized
def sense (p, Z):
    q = []			# new probability distribution
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append( p[i] * (hit * pHit + (1 - hit) * pMiss) )
        # if Z == world[i]:
        #     q.append( p[i] * pHit )
        # else:
        #     q.append( p[i] * pMiss )
    # normalization
    s = sum(q)
    for i in range(len(q)):
        q[i] /= s
    return q

# this function takes the probapility distribution and the needed amount of motion
# and returns a new probability distribution with shifted probabilities, considering the 
# inexact motion cases(Overshoot and Undershoot) 
def move(p, U):
    q = []		# new probability distribution
	# inexact (inaccurate) motion
    for i in range(len(p)):
        s = pExact * p[(i - U) % len(p)]
        s += pOvershoot * p[(i - U - 1) % len(p)]
        s+= pUnershoot * p[(i - U + 1) % len(p)]
        q.append(s)
    return q

# testing the functions
measurements = ['red', 'green']     # an arbitrary set of measurements by the robot
motions = [1, 1]                    # set of motions to be achieved by the robot
for i in range(len(motions)):
    p = sense(p, measurements[i])
    p = move(p, motions[i])
for i in range(len(p)):
    p[i] = round(p[i], 2)
print (p)