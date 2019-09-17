# =============================================================================
# This is the module file. There are better ways to write modules and functions 
# it contains. I have written it in a very short time so have not followed the 
# best practices. But there are better ways to write functions and it is 
# expected from you that you will learn them and implement yourself.
#
# The only purpose of this function is to show you how to write functions I 
# repeat there are few things which are still incorrect for example dataset 
# columns have not been converted to the suitable datatype.
# =============================================================================

import pandas as pd
import seaborn as sns
# import argparse
import time

# parser = argparse.ArgumentParser()
# parser.add_argument("--input", help = "input filename")
# parser.add_argument("--output", help = "output filename")
# args = parser.parse_args()

# print(" Input csv file location is" + args.input)
# print(" Output csv file location is" + args.output)


# df = pd.read_csv(args.input)
# print(df.head())
# box_plt = sns.boxplot(x = df["Age"])
# fig_= box_plt.get_figure()
# t = time.localtime()
# timestmp_ = time.strftime('%b-%d-%Y_%H%M%S', t)
# fig_.savefig(args.output + "op" + timestmp_ + ".png")


def read_n_plt(inptfile, otptfile):
    df = pd.read_csv(inptfile)
    print("Numerical cols list " + 
          str(list(df._get_numeric_data().columns.values)))
    cl_name = input("Type the column name for boxplot:")
    box_plt = sns.boxplot(x = df[cl_name])
    fig_= box_plt.get_figure()
    t = time.localtime()
    timestmp_ = time.strftime('%b-%d-%Y_%H%M%S', t)
    fig_.savefig(otptfile + "op" + timestmp_ + ".png")
    

if __name__ == '__main__':
    read_n_plt()