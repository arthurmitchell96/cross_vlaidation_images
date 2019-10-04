#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 12:33:07 2019

@author: socs-dual-boot
"""
import os
import numpy as np
import random
from shutil import copy
def create_cross_folds():
    instar_dir = ['../cleaned_dataset/instar_1/','../cleaned_dataset/instar_2/','../cleaned_dataset/instar_3/','../cleaned_dataset/instar_4/','../cleaned_dataset/instar_5/','../cleaned_dataset/instar_6/']
    #bad_dir = 'bad/'
    instars = ['instar_1','instar_2','instar_3','instar_4','instar_5','instar_6',]
    nb_folds = 5
    train_test_splits = [0.75, 0.25]

    def get_file_list(direc):
        file_list = list()
        for file in os.listdir(direc):
            if file.endswith(".jpg"):
                file_list.append(file)
        return file_list
   
    def make_folders():
        os.mkdir('folds')
        os.mkdir( 'test')
        for  i in instars:
            os.mkdir('test/'+ i)
        for index in range(1,nb_folds+1):
            
            dir_name = "folds/fold_"+str(index)
            os.mkdir(dir_name)
            os.mkdir(dir_name +'/' + 'train' +'/')
            os.mkdir(dir_name +'/' + 'validation/' )
            for  i in instars:
#                os.mkdir('test/'+ i)
                
                
                os.mkdir(dir_name +'/' + 'train' +'/'+ i )
                
                os.mkdir(dir_name +'/' + 'validation' +'/'+ i )
                #os.mkdir(dir_name  + '/' + 'validation/'+ i )
                
#                os.mkdir(dir_name + i+ '/' + 'test/good')
#                os.mkdir(dir_name + '/' + 'test/bad')
#                
#                os.mkdir(dir_name + '/' + 'train/good')
#                os.mkdir(dir_name + '/' + 'train/bad')
#                
#                os.mkdir(dir_name + '/' + 'validation/good')
#                os.mkdir(dir_name + '/' + 'validation/bad')
    def write_test_direc(files,instar):
#        for c in range(1,nb_folds):
#            for t in instars:
        for i in files:
            copy(instar_dir[instar]+i, 'test/'+instars[instar]+'/')
                    
                    
    def write_direc(files, fold, instar, tov):
        fold += 1
        for f in files:
           copy(instar_dir[instar]+f, 'folds/' + 'fold_'+ str(fold) + '/' + tov +'/' + instars[instar] + '/')
    make_folders()
    #test = list() 

    

    
    for instar_number, i in enumerate(instar_dir):
        files = []
        files = get_file_list(i) 
        
#        bad_files = get_file_list(bad_dir)
        rand_files = []
        rand_files = files.copy()
        random.shuffle(rand_files)
#    rand_bad_files = bad_files
#    random.shuffle(rand_bad_files)
        lists = []
        for p in range(nb_folds):
            fold_name  = 'fold' + str(p+1)
            fold_name = list()
            lists.append(fold_name)


      
               
        #train_test_splits.reverse()
        test = []
        for x in range(0,int(len(rand_files)*train_test_splits[-1])):
                file = random.choice(rand_files)
                test.append(file)
                rand_files.remove(file)
                
        write_test_direc(test, instar_number)
       
        fold_size =int(len(rand_files)*(train_test_splits[0]/nb_folds))
        
        
        for count, m in enumerate(lists):
            validation = []
            for x in range(count*fold_size,(count+1)*fold_size):
                
                write_files = rand_files.copy()
                
                file = write_files[x]
                validation.append(file)
                write_files.remove(file)
            m = write_files
                
            print(m)
            print(count)
            write_direc(m, count, instar_number, 'train')
            write_direc(validation, count, instar_number, 'validation')
            

create_cross_folds()