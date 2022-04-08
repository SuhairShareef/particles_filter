from ParticlesFilter import *

if __name__ == "__main__":
    
    pf = ParticlesFilter()
    pf.generate_random_particles()
    pf.generate_path('a', 'c')
    print(pf.path)
    #pf.draw()
    no_of_steps = 0
    print(pf.particles)
    while not pf.stop(20):
        no_of_steps += 1
        pf.move(1)
        pf.normalize()
        pf.sample()
        pf.normalize()
        #print(pf.particles[-1])

    
    print(no_of_steps)