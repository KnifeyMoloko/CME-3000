# CME-3000

##Corpo Masses Eater 3000
### Update: Almost There Alpha Version

This small project is meant to blow minds and reshape the universe. Besides that it is a training project for us. The game could be done in Game Maker or Unity, but that would take a lot of the fundamentals out of the project, so right now we're sticking to Python 2.7.6.

The first slice of the game will have the following characteristics:
* *DONE* game code written in Pyton 2.7.6
*  *DONE* modular code architecture i.e. separate modules for classes, helper functions, config - it's like introducing all the linking problems of a C/C++ project into a Python project! Yay! Yet at this point it works really well, though the final thing might need refactoring the architercture to cut down on duplicating namespaces.
* *DONE* two initial classes: the Peon and the Head
* *DONE* simple randomised behaviour for the Peon - essentially walking randomly
* *DROPPED* simple keyboard controlled behaviour for the Head
* a basic interaction for the Peon being eaten

###Optional features:
- a gridline for the Peon to walk on
- *DONE* some simple collision mechanic i.e. bouncing the Peon of the border of the screen
- simple sounds
- *DONE* music background
- *YES YOU ARE* just testing here if I'm doing anything......

UPDATE June 2017:

* Nice changelog introduced along the way, look it up to see all the glory and hardships
* Peon class developed to some extent: randomized moving, timestamps, collsions all implemented, new animation works ongoing
* Head class still underdeveloped, need to be prioritized with animations
* Spawners introduced with a slightly awkward RNG-based spawning, might need reworking
* Level generation and serialization of complete level objects introduced with Pickle
* Simple menu + loading a level on "New Game" selection introduced
* Current asset wokr focued on adding animations, music
* Current programming work focused on delivering a more easy to use Level Editor (using TKinter)
* General design and aesthetic mostly locked down, excluding music 
