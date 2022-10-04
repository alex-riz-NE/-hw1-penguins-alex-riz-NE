# HW 1

The first homework assignment where we learn how to make graphs usng various plotting techniques and how to interface git.

## Clone the repo

First clone it and navigate to directory

```
git clone https://github.com/alex-riz-NE/hw1-penguins-alex-riz-NE.git

cd hw1-penguins-alex-riz-NE
```

### Reproducibility

Download the source CSV with the following command

```
make data
```

### Presenting results

Here's The Figure from the data set

<img src="figs/penguin.png" width=500>

Recreate this chart with
```
make app
```

## requirements

I created the requirements.txt by first running this command

```
conda list -e > requirements.txt
```

Then I edited it to include only the modules that I imported in my code, along with the python version.
```
conda list -e > requirements.txt
```

You can use the requirements.txt to create a conda environment and run code as follows:
```
conda create --name demo --file requirements.txt
conda activate demo
make app
conda deactivate
```
