from ParticlesFilter import *

if __name__ == "__main__":
    
    pf = ParticlesFilter()
    pf.generate_probability()
    pf.generate_path('a', 'z')
    pf.generate_random_particles()
    #print(pf.path)
    
    pf.draw()
    no_of_steps = 0
    #print(pf.particles)
    while not pf.stop(5):
        no_of_steps += 1
        pf.move(1)
        pf.normalize()
        pf.sample()
        pf.normalize()
        pf.draw()
        #print(pf.particles[0].pos)

    
    print(no_of_steps)