## Fashion MNIST dataset analysis and deep learning experimentation project

This project contains
- Basic analysis of the Fashion MNIST dataset [EDA analysis](src/fashion_mnist_eda.ipynb)
- Deep learning experimentation with the dataset [DL experiments](src/fashion_mnist_expts.ipynb)
- Documentation on CI/CD plan for the project [deployment plan](src/deployment_plan.md)
- SQL query to retrieve the data from the database as specified in the project requirements [SQL query](src/sql_query.md)
- [Applying custom labels function and label mapping dictionary](src/custom_labels.py)

# Local installation

[**Pipenv**](https://pipenv-es.readthedocs.io/es/latest/) is used to manage the script dependencies. In order to run the script locally, use:

```
pipenv install --dev
pipenv shell
pipenv run jupyter notebook
```
