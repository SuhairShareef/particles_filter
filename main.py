from ParticlesFilter import *
#import keyboard

if __name__ == "__main__":
    
    pf = ParticlesFilter()
    pf.generate_path()
    pf.generate_random_particles()
    
    pf.draw()
    no_of_steps = 0
    while not pf.stop(5):
        no_of_steps += 1
        pf.move(1)
        pf.update()
        pf.normalize()
        pf.sample()
        pf.normalize()
        pf.draw()
        """ if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('exit')
            break """
    
    print("The number of steps it took me to find my position is: ", no_of_steps, "I'm at position: ", pf.robot.position)
