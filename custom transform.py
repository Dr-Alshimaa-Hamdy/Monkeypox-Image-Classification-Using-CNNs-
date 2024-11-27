import numpy as np
import pandas as pd


df = pd.DataFrame(data)


# Define a custom transformation function
def custom_transform(column):
    """
    Applies a custom transformation to a column.
    Example: f(x) = x^2 + 2x + 1 (quadratic transformation)
    """
    return column**2 + 2 * column + 1

# Apply the custom transformation to all columns
df_custom_transformed = df.apply(custom_transform)



