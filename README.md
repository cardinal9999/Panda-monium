# Panda-monium
Panda-monium lets you serialize + compress Pandas DataFrames. So far, the only way to serialize DataFrames was to use pickle (which takes lots of space on your computer) and converting to CSV files (which can create the [Unnamed: 0 column](https://stackoverflow.com/questions/36519086/how-to-get-rid-of-unnamed-0-column-in-a-pandas-dataframe))

![](logo.png)
## Tutorial
```py
import pandas as pd
import Pandamonium as pm #Keep the uppercase
data = pd.DataFrame({ ... }) #Add your data
file = "data.pdc"

# Compress
pm.compress(data, file) #Should return "Success!"

# Decompress
loaded = pm.decompress(file)
```
## How it works
Panda-monium works by converting DataFrames into CSV files and replacing substrings (such as a comma next to a number) into 1 character. The larger the data, the more likely it is for compression to work.
