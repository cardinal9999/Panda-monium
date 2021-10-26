# Panda-monium

[![Inactively Maintained](https://img.shields.io/badge/Maintenance%20Level-Inactively%20Maintained-yellowgreen.svg)](https://gist.github.com/cheerfulstoic/d107229326a01ff0f333a1d3476e068d)

Panda-monium lets you serialize + compress Pandas DataFrames. It uses CSVs to serialize and [Goose](https://github.com/cardinal9999/goose) to compress DataFrames. So far, the only way to serialize DataFrames was to use pickle (which takes lots of space on your computer) and converting to CSV files (which can create the [Unnamed: 0 column](https://stackoverflow.com/questions/36519086/how-to-get-rid-of-unnamed-0-column-in-a-pandas-dataframe))

![](logo.png)


## Tutorial
Example:
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
Panda-monium works by converting DataFrames into CSV files and replacing substrings (such as a comma next to a number) into 1 character. The larger the data, the more likely it is for compression to work. It removes the annoying Unnamed: 0 column by removing it during decompression.
## Collisions
A collision is when one of the DataFrame's strings contains a Panda-monium "keyword" or the replacing character during compression (Panda-monium has been designed to prevent collisions by replacing a comma next to any number with a character that isn't on the keyboard. This makes it unlikely for collisions to happen).

Collisions can cause the DataFrame to become unstable and have weird dimensions, which can cause errors. 
### Preventing Collisions
Collisions can be prevented by using characters that the system can't show (such as )

However, there is a small chance that the symbol (that GitHub can't display) gets in the DataFrame. The solution? Escape characters. They will be added in future versions. 
