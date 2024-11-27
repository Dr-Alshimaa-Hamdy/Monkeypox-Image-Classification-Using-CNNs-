import numpy as np
import pandas as pd

df = pd.DataFrame(data)

def log_transform(column):
    """Applies log transform to a column, handling zeros and negative values."""
    column = np.where(column > 0, np.log(column), np.nan)  # Replace non-positive values with NaN
    return column

df_log_transformed = df.apply(log_transform)



