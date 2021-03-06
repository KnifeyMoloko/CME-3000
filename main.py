"""This is to be the main module, consolidating and managing all other modules.
This module needs to be opened first as __main__. It's designed to launch the
main menu screen and then handle all input/output, loading levles etc. It's
supposed to be as lean as possible, but will have to contain at least these
elements:
- config imort and all other imports if necessary
- track record keeping via save/load
- new game/load game logic
- main game logic
- mechanics for object interactions? (might be better to move to a separate
module and import at boot)

//based on the simplePythonTest.py template"""

import config
from config import *

def main():
    quit_flag = False
    # create the main Surface
    EKRAN = helpers.displayer()

    # create a Clock instance for updates and FPS management
    fpsClock = pygame.time.Clock()
    FPS = 60

    # create I/O handler

    EventHandler = config.classes.Event()

    # draw menu buttons for "New Game" and "Quit"
    # moved this outside of the main loop to avoid drawing over the levels

    NewGameButton = config.classes.GUI_BUTTON("new_game.png", \
    (config.res_x/2-200, config.res_y/2-100), config.helpers.new_game, EventHandler, 185, 150)

    QuitButton = config.classes.GUI_BUTTON("happy_baton.png", \
    (config.res_x/2+150, config.res_y/2+75), config.helpers.quitter, EventHandler, 279, 274)

    # draw walls - MOVE TO a class def or helper def

    wall_array_x = config.res_x / config.wall_size[0]
    wall_array_y = config.res_y / config.wall_size[1]
    wall_array_list = []

    for n in range(1, wall_array_y):
        """This for loop creates n-number of wall objects to cover the sides of
        the screen. With a bit of work this could provie a basic and rather
        unsexy wall array generator. Good for testing tho."""

        wall = classes.Environment_Wall()
        posx = 0
        posy = config.res_y - config.wall_size[1] * n
        wall.set_pos((posx, posy))
        wall_array_list.append(wall)


    # main loop
    while quit_flag == False:

        # reset the Surface for clean redrawing
        EKRAN.fill(config.WHITE)

        # retrieve events - IMPORTANT: main I/O output, don't add other handlers
        EventHandler.get_events()

        #retrieve collisions and process them
        EventHandler.get_collisions()
        EventHandler.process_collisions()
        EventHandler.get_delta()

        # finalise the loop
        Object_list.update()
        GUI_list.update()
        Enviro_list.draw(EKRAN)
        GUI_list.draw(EKRAN)
        Peon_list.update()
        Peon_list.draw(EKRAN)
        Spawner_list.update()
        fpsClock.tick(FPS)
        pygame.display.flip()

if __name__ == '__main__':
    main()
