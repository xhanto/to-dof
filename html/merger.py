import pandas as pd
import pickle

f = raw_input('Enter 1st file name: ')
#g = raw_input('Enter 2nd file name: ')
df1 = pd.read_pickle(f + ".pickle")
#df2 = pd.read_pickle(g + ".pickle")
print df1
#df1 = df1.append(df2)

#pd.to_pickle(df1,f + "_full.pickle")
