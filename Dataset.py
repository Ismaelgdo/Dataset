#Dataset.py
#Ismael Garrido
#09/28/2016
#Creating a Class to compute simple operations on a dataset.

import math
class Dataset(object):
    '''Dataset is a collection of numbers from which simple
    descriptive statistics can be computed.'''

    def __init__(self):
        '''post: self is an empty Dataset'''

        self._sum = 0
        self._max  = None
        self._min = None
        self._size = 0
        self._average = 0
        self._sum_squares = 0
       

    def add(self, num):
        '''add num to the data set
        keep track of the sum of squares and size of the input
        post: num is added to the data set'''
        self._sum += num
        self._size += 1
        self._sum_squares += (num)**2
        self._average = (self._sum) / (self._size)
        
        if self._min is None or num < self._min:
            self._min = num 
        if self._max is None or num > self._max:
            self._max = num
            
            
    def size(self):
        '''compute the lenght of the list
        pre: size of self >=0
        post: returns the lenght of the list'''
        return self._size 

    def min(self):
        '''find the minimum
        pre: size of self >= 1
        post: returns smallest number in self'''
        if self.size() < 1 or self._min == None:
            raise ValueError
        return self._min

    def max(self):
        '''find the minimum
        pre: size of self >= 1
        post: returns smallest number in self'''
        if self.size() < 1 or self._max == None:
            raise ValueError
        return self._max

    def average(self):
        '''calculate the mean
        pre: size of self >= 1
        post: returns the mean of the values in self'''
        if self.size() < 1:
            raise ValueError
        return self._average

    def sum_squares(self):
        '''compute the sum of squares
        pre: soze of self >= 1
        post: return the sum of squares'''
        if self.size() < 1:
            raise ValueError
        return self._sum_squares

    def std_deviation(self):
        '''calculate the standard deviation
        pre: size of self >= 2
        post: returns the standard deviation of the values in self'''
        if self._size  < 2:
            raise ValueError("Minimun two values needed to compute standard deviation")
        self._std_dev = math.sqrt(( self._sum_squares - (self._sum**2/self._size)) / (self._size-1))
        return self._std_dev

if __name__ == '__main__':
 
    while True:
        data = Dataset()
        print('This is program computes the min, max, mean and')
        print('standard deviation for a set of numbers.\n')
        while True:
            xStr = input('Enter a number (<Enter> to quit): ')
            if xStr == '':
                break
            try:
                x = float(xStr)
            except ValueError:
                print('Invalid Entry Ignored: Input was not a number')
                continue
            data.add(x)
        print('Summary of', data.size(), 'scores.')
        print('Min:', data.min())
        print('Max:', data.max())
        print('Mean:', data.average())
        print('Standard Deviation:', data.std_deviation())
        print()
        print()










                    

