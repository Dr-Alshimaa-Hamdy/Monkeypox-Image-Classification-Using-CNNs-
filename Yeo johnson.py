import numpy as np
import pandas as pd
from scipy.stats import yeojohnson


df = pd.DataFrame(data)



# Yeo-Johnson transform function
def yeojohnson_transform(column):
    """
    Applies the Yeo-Johnson transformation to a column.
    """
    # Apply Yeo-Johnson transformation
    transformed, _ = yeojohnson(column)  # The second value is lambda, which we ignore here
    return transformed

# Apply the Yeo-Johnson transformation to all columns
df_yeojohnson_transformed = df.apply(yeojohnson_transform)



