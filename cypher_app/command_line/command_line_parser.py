valid_options = ['-d', '-e', '-f', '-out']


def start(args):
    print(args)
    proccesArgs(args)


def proccesArgs(args):
    for m in range(len(args)):
        if(m % 2 == 0):
            if(args[m] in valid_options):
                print("%s was passed in" % (args[m]))
            else:
                print("%s is not a valid option" % (args[m]))
                break
