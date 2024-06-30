# creating an isolated environment(recommended)

    $ python -m pip install -U virtualenv
    $ python -m virtualenv my_env
    $ source my_env/bin/activate

# deactivate can close the environment

    $ python -m  pip install -U jupyter matplotlib numpy pandas scikit-learn
    $ python -m ipykernel install --name=my_env
    $ jupyter notebook

# jupyter notebook file to .py file 
    $ jupyter nbconvert --to python notebook.ipynb 
