from cacti import cacti_number
from calc import calculator

def main():
    plot = [ [1, 0, 1, 0, 1]
            [0, 0, 0, 0, 0]
            [1, 0, 0, 0, 0] ]
    print(cacti_number(plot))
