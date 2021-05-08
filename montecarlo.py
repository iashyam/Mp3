from random import uniform

def monte_carlo(f,a,b):

    rand_max = 10000
    steps = 10000
    sums = 0

    for step in range(steps):
        x = uniform(a,b)
        sums += f(x)

    return sums*(b-a)/steps

def f(x):
    return x**2

print(monte_carlo(f,0,1))


