"""
Merge in place is not really possible in Pandas.
That is because unless you explicitly program in-place numpy array reordering you'll need to copy the arrays.
It is possible to reduce the long term memory requirements with below, but it is not really in-place method.
"""

import numpy as np
import pandas as pd

df_1 = pd.DataFrame(dict(a=['1', '2', '3'], b=[10, 20, 30]))
df_2 = pd.DataFrame(dict(a=['1', '3', '2'], c=[10, 30, 20]))

expected_b = df_1['b'].values
expected_c = df_2['c'].values

a = df_2['a'].values
a_s = np.argsort(df_2['a'].values)
np.sort()

df_1.set_index('a', inplace=True)
df_2.set_index('a', inplace=True)

suffixes = ['_x', '_y']

for c in df_1.columns:
    df_1.rename(columns={c: c + suffixes[0]}, inplace=True)

for c in df_2.columns:
    df_1[c + suffixes[1]] = df_2[c]

df_1.reset_index(inplace=True)

# does not match. The arrays have to be rearranged. So copying will happen.
assert np.all(df_1['b_x'].values == expected_b)
assert np.all(df_1['c_y'].values == expected_c)
print(df_1)


