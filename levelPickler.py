import config, cPickle, os

# inventory class for the first level

class Level():
    """This class is a template for any level you want to create. Add and modify attributes to create a level layout.
    Remember: if you add any new attributes you will need to ammend the methods of the Level_creator class in the classes
    module accordingly - otherwise the attributes will go unrecognized and only take up memory in the namespace. This is
    something of a lowly level editor. Sorry, no GUI for this mofo. C programming Master Race gives a thubms up (their asses)."""

    __module__ = os.path.splitext(os.path.basename(__file__))[0] # bug workaround, look in the changelog for details

    def __init__(self):
        self.objects = {}
        self.music = '02.wav'
        self.background = None
        self.spawners = [config.classes.Spawn("Peon", (config.res_x/1.5, config.res_y/3), 50, 50)]
        self.misc = {}

Level1 = Level()

def main():
    # create instance to pickle
    ogur = Level1
    print ogur.music # debug print
    print
    # this is the part for the levelPickler module
    directory = os.getcwd()
    cwdDirList = os.listdir(directory)
    if 'Levels' in cwdDirList:
        print "Detected a level dir, moving on..."
        pass
    else:
        outputPath = directory + "/" + "Levels"
        os.makedirs(outputPath)

        with open(outputPath + "/" + "level1ogur.txt",'wb') as output_file:
            cPickle.dump(ogur, output_file)

    # this is the part for the level loading function of the main game module
    """with open(r'/Levels/Level1/ogur.txt', 'rb') as input_file:
        new_ogur = cPickle.load(input_file)"""

if __name__ == '__main__':
    main()
