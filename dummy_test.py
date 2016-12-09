import config
from inspect import getmembers
from config import *

def main():
    quit_flag = False
    fpsClock = pygame.time.Clock()
    FPS = 10

    print "Here's the key list:"
    print "q = move one frame ahead, update objects, peons, flip display"
    print "w = call helpers.new_game()"
    print "e = print list of objects and peons"
    print "a = print active status for objects"
    print "s = use the for loop in dummy_test to change the active attr"
    print "d = print the stack using inspect"

    # create the main Surface
    EKRAN = helpers.displayer()


    # main loop
    while quit_flag == False:

        EKRAN.fill(config.WHITE)

        """This is the 'main menu' part of the main module code. It can be
        pickled once as a special level instance and loaded on boot to slim down
        the code of main."""

        event_list = config.pygame.event.get()

        for event in event_list:
            if event.type == pygame.KEYDOWN and \
            event.key == pygame.K_q:
                Object_list.update()
                Peon_list.update()
                fpsClock.tick(FPS)
                pygame.display.flip()
            elif event.type == pygame.KEYDOWN and \
            event.key == pygame.K_w:
                loaded_level = helpers.new_game()
                """print loaded_level
                list_of_members = getmembers(loaded_level)
                for line in list_of_members:
                    print str(line) + "\n"""
            elif event.type == pygame.KEYDOWN and \
            event.key == pygame.K_e:
                print
                print "The object list is: " + str(config.Object_list)
                print
                print "Peon list is: " + str(config.Peon_list)
                for o in config.Object_list:
                    print o.__dict__
            elif event.type == pygame.KEYDOWN and \
            event.key == pygame.K_a:
                for obj in config.Object_list:
                    print str(obj) + " " + str(obj.active)
            elif event.type == pygame.KEYDOWN and \
            event.key == pygame.K_s:
                for obj in config.Object_list:
                    obj.active = True
            elif event.type == pygame.QUIT or \
            (event.type == config.pygame.KEYUP and \
            event.key == config.pygame.K_ESCAPE):
                config.quitter()

if __name__ == '__main__':
    main()
