import numpy as np
import pandas as pd
from sklearn.preprocessing import QuantileTransformer


df = pd.DataFrame(data)



# Initialize the QuantileTransformer
quantile_transformer = QuantileTransformer(output_distribution='uniform', random_state=42)

# Fit and transform the data
df_quantile_transformed = quantile_transformer.fit_transform(df)

# Convert the transformed data back into a DataFrame
df_quantile_transformed = pd.DataFrame(df_quantile_transformed, columns=df.columns)


