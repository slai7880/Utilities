from PlottingUtil import *
from Util import *
from MathUtil import *
import numpy as np

def plotting():
    data = np.absolute(np.random.rand(5, 8))
    colors = ["r", "b", "g", "m", "k"]
    title = "Stacked Bar Plot Example"
    labels = ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5"]
    print(data)
    fig, ax = makeMultibarPlot(data, colors[:data.shape[0]], title, labels[:data.shape[0]], width = 0.1)
    plt.show()
    
def math():
    n = 0
    print(countSquares(n))

def misc():
    print(integerBreak(2))

misc()