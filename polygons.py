import matplotlib.pyplot as plt
from math import sin,cos,pi

class polygon:
    def __init__(self,*points):
        self.points = points

    def show(self):
        x = [x for (x,y) in self.points]
        y = [y for (x,y) in self.points]
        plt.plot(x,y,'o')
        plt.show()
   
    def plot_with_lines(self):    
        x = [x for (x,y) in self.points]
        y = [y for (x,y) in self.points]
        x.append(self.points[0][0])
        y.append(self.points[0][1])
        plt.plot(x,y) 
        
    def plot_points(self):
        x = [x for (x,y) in self.points]
        y = [y for (x,y) in self.points]
        plt.plot(x,y,'o')

def plot_polygons_lines(*polygons):
    for shape in polygons:
        shape.plot_with_lines()
    plt.show()

def plot_polygons_points(*polygons):
    for shape in polygons:
        shape.plot_points()
    plt.show()

def generate_polygon_regular(x,y,r,n):
    points = [(x+r*sin(i*2*pi/n),y+r*cos(i*2*pi/n)) for i in range(n)]
    return polygon(*points)


