import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    stack = [ tmp ]
    tmps = []
    screen = new_screen()
        
    for command in commands:
        
        #print command

        if command[0] == 'line':
            add_edge( tmps, command[1], command[2], command[3], command[4], command[5], command[6] )
            matrix_mult(stack[-1], tmps)
            draw_lines(tmps, screen, color)
            tmps=[]

        elif command[0] == 'box':
            add_box( tmps, command[1], command[2], command[3], command[4], command[5], command[6] )
            matrix_mult(stack[-1], tmps)
            draw_polygons(tmps, screen, color)
            tmps=[]

        elif command[0] == 'sphere':
            add_sphere( tmps, command[1], command[2], command[3], command[4], command[5], 5 )
            matrix_mult(stack[-1], tmps)
            draw_polygons(tmps, screen, color)
            tmps=[]

        elif command[0] == 'torus':
            add_torus( tmps, command[1], command[2], command[3], command[4], command[5], 5 )
            matrix_mult(stack[-1], tmps)
            draw_polygons(tmps, screen, color)
            tmps=[]

        elif command[0] == 'scale':
            #

        elif command[0] == 'translate':
            #

        elif command[0] == 'rotate':
            #

        elif command[0] == 'push':
            #

        elif command[0] == 'pop':
            #

        elif command[0] == 'save':
            #

        elif command[0] == 'display':
            #

        elif command[0] == 'translate':
            #

        elif command[0] == 'rotate':
            #
