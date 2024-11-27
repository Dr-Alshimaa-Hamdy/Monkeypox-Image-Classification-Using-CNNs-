import numpy as np
import pandas as pd
from scipy.stats import boxcox


df = pd.DataFrame(data)



# Box-Cox transform function
def boxcox_transform(column):
    """
    Applies the Box-Cox transformation to a column.
    """
    # Ensure the data is positive
    if (column <= 0).any():
        raise ValueError("Box-Cox transformation requires all values to be positive.")
    
    # Apply Box-Cox transformation
    transformed, _ = boxcox(column)  # The second value is lambda, which we ignore here
    return transformed

# Apply the Box-Cox transformation to all columns
df_boxcox_transformed = df.apply(boxcox_transform)


