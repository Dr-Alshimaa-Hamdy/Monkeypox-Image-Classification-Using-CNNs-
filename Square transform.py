import numpy as np
import pandas as pd

df = pd.DataFrame(data)

def square_transform(column):
    """Applies square transformation to a column."""
    return np.square(column)  # Squares each value

df_square_transformed = df.apply(square_transform)


