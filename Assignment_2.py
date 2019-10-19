### ALL CODE YOU SUBMIT SHOULD BE IN THIS FILE
### DO NO IMPORT AND USE ANY OTHER PACKAGES.


### Import the uniform and gauss (for normally distributed
### numbers) methods from the random pacakage
from random import uniform, gauss


### Representation of a dart, with X and Y coordinates.
class Dart:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def __str__(self):
        return "({0:.3f}..,{1:.3f}..)".format(self.x, self.y)

    def __repr__(self):
        return self.__str__()

### Euclidean distance of a given Dart object to the origin (0,0)
def distanceToOrigin(dart):
    return (dart.x**2 + dart.y**2) ** 0.5

### Generate and throw a dart in a uniform square from (-1,-1) to (1,1)
def throwUniformDart():
    return Dart(uniform(-1,1),uniform(-1,1))

### Generate and throw a dart normally distributed about the origin (std=0.6)
def throwNormalDart():
    mu = 0
    sigma = 0.6
    return Dart(gauss(mu,sigma),gauss(mu,sigma))


'''Function to throw as many darts as needed'''
def throwMultipleTimes(num, type = 'Unif'):
    sum_dist = 0 # Initialize the counter for the distances we are interested in
    for i in range(num):
        if type == 'Unif': # If we want uniform distributions
            throw = throwUniformDart() # Then throw uniform darts
        elif type == 'Norm': # If we want normal distributions
            throw = throwNormalDart() # Then throw normal darts
        dist = float(distanceToOrigin(throw)) # get the Euclidean distance from that throw to the origin
        if dist < 1:
            sum_dist=sum_dist+1 # Count the times the distance is lower than 1
    return sum_dist # Return number of times distances < 1


def getpi(num, type):
    sum_dist = throwMultipleTimes(num,type) # How many darts have a distance < 1
    return sum_dist/num*4 # Get pi by simplifying the equation area of circle / area of square

def getInterval(num,type):
    total_pi = [] # Initialize the list of estimations
    for i in range(num):
        pi = getpi(1000,type) # estimate pi from 1000 throws
        total_pi.append(pi) # store each estimation in the list
    mean = sum(total_pi)/len(total_pi) # compute the mean of all the estimations
    sq_diff = []
    for pi in total_pi:
        temp = (pi - mean)**2 # get the square difference from each estimation to the mean
        sq_diff.append(temp)

    sd = (sum(sq_diff)/len(total_pi))**0.5 # standard deviation
    upper = mean + 1.96 * sd/len(total_pi)**0.5 # upper limit of a normal distribution with alpha = 0.05
    lower = mean - 1.96 * sd/len(total_pi)**0.5 # lower limit of a normal distribution with alpha = 0.05
    return lower,upper

def unpaired_diff(num): # Unapired t-test as we are going to compare two independent estimations
    unif_pi = []
    norm_pi = []
    # Let's get multiple estimations from each distributions
    for i in range(num):
        pi_u = getpi(1000, 'Unif') # estimate pi from 1000 uniform throws
        pi_n = getpi(1000, 'Norm') # estimate pi from 1000 normal throws
        unif_pi.append(pi_u)
        norm_pi.append(pi_n)

    # Compute mean and sd both type of darts
    mean_u = sum(unif_pi)/len(unif_pi)  # mean of uniform distributed throws
    mean_n = sum(norm_pi) / len(norm_pi) # mean of normal distributed throws

    sq_diff_u = []
    for pi in unif_pi:
        temp = (pi - mean_u)**2
        sq_diff_u.append(temp)

    sd_u = (sum(sq_diff_u) / len(unif_pi))**0.5 # sd of uniform distributed throws

    sq_diff_n = []
    for pi in norm_pi:
        temp = (pi - mean_n)**2
        sq_diff_n.append(temp)

    sd_n = (sum(sq_diff_n) / len(norm_pi))**0.5 # sd of normal distributed throws

    '''Unpaired t-test'''
    return (mean_u - mean_n)/(sd_u**2/len(unif_pi) + sd_n**2/len(norm_pi))**0.5




if __name__ == "__main__":

    ### Throw and print a 'uniform' dart
    dart = throwUniformDart()
    print("Uniform dart's coordinates: {0}".format(dart))

    ### Compute and print the dart's distance to the origin
    distance = distanceToOrigin(dart)
    print("Distance of dart to origin: {0}".format(distance))

    dist = throwMultipleTimes(1000, 'Unif')
    print("a) Euclidean distances lower than 1: {0}".format(dist))

    # print(getpi(1000,'Unif'))
    x,y = getInterval(100,'Unif')
    print("b) The 95% confidence interval for pi is: {0} to {1}".format(x,y))

    # print(getpi(1000,'Norm'))
    dist_n = throwMultipleTimes(1000, 'Norm')
    diff = unpaired_diff(100)
    print("c) Euclidean distances lower than 1 (Normal distrib): {0}".format(dist_n))

    t_test = unpaired_diff(100)
    print("As t_N%,99 = {0}, we can say that they are significantly different with a confidence threshold of over 99%".format(t_test))