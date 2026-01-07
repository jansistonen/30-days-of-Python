class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
    def person_info(self):
        return f'{self.name} is {self.age} old. {self.name} is from {self.location}'


p = Person('Jan', 31, 'Joensuu')
print(p.person_info())
print(p.name)

# 1 - Python has the module called statistics and we can use this module to do all the statistical calculations.
#  However, to learn how to make function and reuse function let us try to develop a program, which calculates 
# the measure of central tendency of a sample (mean, median, mode) and measure of variability 
# (range, variance, standard deviation). 
# In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. 
# You can create a class called Statistics and create all the functions that do statistical calculations as methods 
# for the Statistics class. Check the output below.

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        sum = 0
        for i in self.data:
            sum = sum + i
        return sum

    def min(self):
        self.data.sort()
        return self.data[0]

    def max(self):
        self.data.sort()
        return self.data[-1]
    
    def range(self):
        self.data.sort()
        range = self.data[-1] - self.data[0]
        return range
    def mean(self):
        sum = sum(self)
        divisor = len(self.data)
        mean = sum / divisor
        return mean
    def mode(self):
        mode = max(set(self.data), key=self.data.count)
        return mode
    def median(self):
        med_index = int(len(self.data) / 2)
        if med_index & 2 == 0:
            return self.data[med_index]
        else:
            return [self.data[med_index -1], self.data[med_index]]


        
    
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

call = Statistics(ages)

print(call.sum())
#print(call.min())
#print(call.max())
#print(call.mode())
print(call.median())