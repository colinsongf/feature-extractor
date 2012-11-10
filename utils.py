'''
Created on Nov 10, 2012

@author: gofrendi
'''

import random

randomizer = random.Random(10)

def bin_to_dec(binary):
    '''
    decimal form of binary
    '''
    return int(binary,2)

def dec_to_bin(decimal):
    '''
    binary form of decimal
    '''
    return str(bin(decimal)[2:])

def bin_digit_needed(decimal):
    '''
    binary digit needed to represent decimal number
    '''
    return len(dec_to_bin(decimal))

def execute(self, expr, record):
    '''
    execute string as python program, give tuple(result, error) as return value
    '''
    result = 0
    error = False
    # get result and error state
    try:
        sandbox={}
        # initialize features
        for i in xrange(len(self._variables)):
            feature = self._variables[i]       
            exec(feature+' = '+str(record[i])) in sandbox 
        # execute expr, and get the result         
        exec('__result = '+expr) in sandbox                      
        result = sandbox['__result']
    except:
        error = True    
    return result, error

def plus(num_1, num_2):
    return num_1 + num_2

def minus(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    return num_1/num_2
