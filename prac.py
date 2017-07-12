# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 18:21:44 2017

@author: ayushc
"""

import numpy
import csv
import pandas as pd



def error_for_given_points(b,m,dict_list):
    #total_num=len(dict_list)
    total_error=0
    for i in range(0,len(dict_list)):
        row=dict_list[i]
        hp=float(row['hp'])
        w=float(row['weight'])
        y=float(row['a'])
        
        total_error+=(y-(m*x+b))**2 
    
    return total_error/len(dict_list)

def step_gradient(b_current,m_current,dict_list,learningRate):
    b_gradient = 0
    m_gradient=0
    n=len(dict_list)
    for i in range(0,len(dict_list)):
        x=dict_list[i]['hp']/dict_list[i]['weight']
        y=dict_list[i]['acceleration']    
        b_gradient+=(2/n)*(y-(m_current*x +b_current))
        m_gradient+=(2/n)*x*(y-(m_current*x-b_current))
        new_b=b_current-(b_gradient * learningRate)
        new_m=m_current-(m_gradient * learningRate)
    return [new_b,new_m]

def gradient_descent_runner(dict_list,starting_b,starting_m,learningRate,num_of_iteration):
    b=starting_b
    m=starting_m 
    
    for i in range(learningRate):
        b,m=step_gradient(b,m,dict_list,learningRate)
    return [b,m]    



def main():

    dict_list=[]    
    learning_rate=.001
    num_of_itr=1000
    initial_b=0
    initial_m=0
    '''
    with open('auto-mpg.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            
            print('reader length',type(reader))
            for row in reader:
                data_dict={}
                
                acceleration=row['acceleration']
                hp=int(row['horsepower'])
                weight=row['weight']
                data_dict['a']=float(acceleration)
                data_dict['hp']=float(hp)
                data_dict['weight']=float(weight)
                dict_list.append(data_dict)
    
    '''
    reader=pd.read_csv('auto-mpg.csv')
    for row in reader:
                data_dict={}
                
                acceleration=row['acceleration']
                hp=int(row['horsepower'])
                weight=row['weight']
                data_dict['a']=float(acceleration)
                data_dict['hp']=float(hp)
                data_dict['weight']=float(weight)
                dict_list.append(data_dict)
    
    print(len(dict_list))
    print ("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, error_for_given_points(initial_b, initial_m, dict_list)))
    print ("Running...")
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_of_itr)
    print ("After {0} iterations b = {1}, m = {2}, error = {3}".format(num_of_itr, b, m, error_for_given_points(b, m,dict_list)))
           # print(acceleration,hp,weight)
if __name__== '__main__':
    main()
    
