import numpy as np
import pandas as pd


df = pd.DataFrame(data)


# Reciprocal transform function
def reciprocal_transform(column):
    """Applies reciprocal transformation to a column."""
    # Handle zero or near-zero values to avoid division by zero
    column = np.where(column != 0, 1 / column, np.nan)  # Replace 0 with NaN
    return column

# Apply the reciprocal transform to all columns
df_reciprocal_transformed = df.apply(reciprocal_transform)


