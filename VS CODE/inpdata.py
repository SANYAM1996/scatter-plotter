import numpy as numpy 
import matplotlib.pyplot as plt
from pandas_datareader import data,wb
df = data.DataReader('TSLA','yahoo')
df
def graph_data(stock):
    df = data.DataReader(stock,'yahoo')
    plt.plot_date(df.index,df.Close,'-')
    plt.xlabel('date')
    plt.ylabel('price')
    plt.title('intresting graph')
    plt.legend()
    plt.savefig('inp.png')
    plt.show()
    
graph_data('TSLA')