[![N|Solid](http://www.philipkalinda.com/uploads/8/6/5/4/86541022/untitled-1.png)][MyWebsite]
# GeneticFS

GeneticFS is a library for feature selection in Machine Learning using a Genetic Algorithm as an optimisation method.
More about the development and tests related to the package are explained [HERE](http://www.philipkalinda.com/ds8)

[![Build Status](https://travis-ci.org/philipkalinda/GeneticFS.svg?branch=master)](https://travis-ci.org/philipkalinda/GeneticFS)

[![PyPI version](https://badge.fury.io/py/geneticfs.svg)](https://badge.fury.io/py/geneticfs)


# New Features!

  - Replaced accuracy score for classification models with F1 score
  - Added hyperparameter descriptions to improve ease of use

### Tech

GeneticFS uses a number of open source projects to work properly:

* Sci-Kit Learn
* Numpy
* Matplotlib


And of course GeneticFS itself is open source with a [public repository][GeneticFS]
 on GitHub.

### Installation
Install the dependencies

```sh
$ pip install numpy
$ pip install matplotlib
$ pip install sklearn
```

Install the package

```sh
$ pip install geneticfs
```

#### How to Use
Regression Model:
```py
from geneticfs import GeneticFS
from sklearn.linear_model import LinearRegression

lin_model = LinearRegression()
gfs = GeneticFS()

# fit the optimizer
gfs.fit(model=lin_model, _type='regression', X=X, y=y) # regression model

# get results output
binary_output_of_optimal_variables, indicies_of_optimal_variables = gfs.results()

# plot results of progress
gfs.plot_progress()
```

Classification Model:
```py
from geneticfs import GeneticFS
from sklearn.linear_model import LogisticRegression

log_model = LogisticRegression()
gfs = GeneticFS()

# fit the optimizer
gfs.fit(model=log_model, _type='classification', X=X, y=y) # classification model

# get results output
binary_output_of_optimal_variables, indicies_of_optimal_variables = gfs.results()

# plot results of progress
gfs.plot_progress()
```
### Todos

 - Write more Tests
 - Add more flexibility in use

License
----

MIT


[//]: # 


   [GeneticFS]: <https://github.com/philipkalinda/GeneticFS>
   [MyWebsite]: <http://philipkalinda.com>
   
