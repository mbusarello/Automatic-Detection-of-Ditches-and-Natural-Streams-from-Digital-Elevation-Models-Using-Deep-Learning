# -*- coding: utf-8 -*-
"""
@author: Mariana Busarello, 2024
"""


import os
import random
import argparse


def train_and_test(training_path,testing_path):
    cc = []

    for folders in sorted(os.listdir(training_path)):
        if os.path.isdir(folders):
            os.mkdir(os.path.join(testing_path,folders))
    
    for chips in os.listdir(os.path.join(training_path,os.listdir(training_path)[0])):
        if chips.endswith('.tif'):
            cc.append(chips)
        
    testList = random.sample(cc,int(len(cc)*0.2)) 
    print(int(len(cc)*0.2), ' chips will be stored for testing of the model')

    for tis in os.listdir(training_path):
        tipath = os.path.join(training_path,tis)
        for test_chips in testList:
            os.rename(os.path.join(tipath,test_chips),os.path.join(os.replace(training_path,testing_path),test_chips))

if __name__ == '__main__':   
    parser = argparse.ArgumentParser(description='separates the input data between testing (20%) and training (80%), moving the testing data to a different folder',
                                     add_help=True,formatter_class=argparse.HelpFormatter)
    parser.add_argument('training_path', help='path to the location of the folder, with labels and topographic indices')
    parser.add_argument('testing_path', help='destination path to the testing data')
    args = vars(parser.parse_args())
    train_and_test(**args)
