# Preprocess Class

## Simple Class to fillNa, normilize or rescale data

### Class Preprocessor

Parent Class that hold the __init__ function and main methods thar work for all children classes

> load_file method
> args:

> save_file method
> args:

> get_mean method calculates the mean of the data

> get_stdev method calculates the standard deviation for data
> args:  digits=6 the round digits of the result 
>       tipo='sample' or diffent from 'sample' to stdev of population calculation.  If tipo is sample subtract one to the length of data size

### Class fillNa

Classe that fill missing values (NAs)

methods

> fill_na_mean method to fill missed values with the mean of the valid values
> no args

> fill_na method to fill missed values with any float value
> args: desired NA replacement value

### Class rescale

Calss that rescale the data

> rescale_MinMax method divide all values by the distance between Max anda the min value
> no args

> rescale_Factor method divide all values by the any numeric choosen value
> args: desired factor

### Class normilize 

Classe that normilize the data 

> normalize method that calculates the value of each data point minus the mean divided by the standard deviation
> args: tipo='sample', the kind of calculation of the standard deviation.



