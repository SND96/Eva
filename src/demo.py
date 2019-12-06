# import unittest
import sys, os
sys.path.append('../')
from PIL import Image
import glob
import random
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.pyplot import imshow

from src.query_parser.eva_parser import EvaFrameQLParser
# from src.query_parser.eva_statement import EvaStatement
# from src.query_parser.eva_statement import StatementType
# from src.query_parser.select_statement import SelectStatement
# from src.expression.abstract_expression import ExpressionType
# from src.query_parser.table_ref import TableRef

from cmd import Cmd

class EVADemo(Cmd):

    def default(self, args):
        """Takes in SQL query and generates the output"""

        # Type exit 
        if(args == "exit" or args == "EXIT"):
            raise SystemExit

        if len(args) == 0:
            
            query = 'Unknown'
        else:
            #### Read Input Videos #####
            input_video = []
            for filename in glob.glob('../data/sample_video/*.jpg'):
                im=Image.open(filename)
                im_copy = im.copy()## too handle 'too many open files' error
                input_video.append(im_copy)
                im.close()

            #### Connect and Query from Eva #####
            parser = EvaFrameQLParser()
            eva_statement = parser.parse(args)
            query = args
            print(eva_statement)
            select_stmt = eva_statement[0]
            print("Result from the parser:")
            print(select_stmt)
            print('\n')


            #### Write Output to final folder #####

            ouput_frames = random.sample(input_video, 50)
            output_folder = "../data/sample_output/"

            for i in range(len(ouput_frames)):
                frame_name = output_folder + "output" + str(i) + ".jpg"
                op = ouput_frames[i].save(frame_name) 

            print("Refer pop-up for a sample of the output")
            ouput_frames[0].show()
                    
        

    def do_quit(self, args):
        """Quits the program."""
        print ("Quitting.")
        raise SystemExit


if __name__ == '__main__': 
    prompt = EVADemo()
    prompt.prompt = '> '
    prompt.cmdloop('Starting EVA...')
