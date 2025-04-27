import sys,os,math
import datetime
import random
import numpy as np


def calculate_area(radius): area=math.pi*radius**2; return area
def random_choice(lst):return random.choice(lst)
def get_current_time( ):
 now=datetime.datetime.now(); return now.strftime('%Y-%m-%d %H:%M:%S')


def main( ):
    r=5
    area=calculate_area(r)
    fruits=['apple','banana','cherry','date']
 fruit=random_choice(fruits)
    print("area of circle with radius",r,"is",area)
    print("Random fruit selected is", fruit )
    print("Current time is:", get_current_time())


if __name__=="__main__":
 main()
