## Setup and Activate Virtual Environment

```
python -m venv .venv
source .venv/bin/activate
```

## Upgrade PIP
```
pip install --upgrade pip
```

## Install Requirements

```
pip install -r requirements.txt
```

## Train the Model with additional data.
> Make sure data.csv is updated inside `training` csv.

```
python training/training_model.py
```

## Package the Module

```
pip install wheel twine
python setup.py sdist bdist_wheel
```

## Test in Edit mode.

```
pip install -e .
``

## Publish through `Twine`

```
twine upload dist/* --verbose
```
