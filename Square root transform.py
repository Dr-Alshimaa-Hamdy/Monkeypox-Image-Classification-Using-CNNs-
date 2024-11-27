import numpy as np
import pandas as pd

df = pd.DataFrame(data)

def square_root_transform(column):
    """Applies square root transformation to a column."""
    return np.sqrt(column)  # Takes the square root of each value

df_sqrt_transformed = df.apply(square_root_transform)


