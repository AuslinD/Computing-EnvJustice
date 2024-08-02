
# Computing-EnvJustice

This repository contains the code and necessary files to generate helpful datasets and figures for my research on the environmental costs of data centers. To run a file, download or install the associated files and dependencies listed below. The files for the project are organized into three folders:
 - Data
 - PythonPrograms
 - ResearchPaper
<!-- -->

## Data

The Data folder contains the csv and shapefile files used in my research. It holds all the supplemental files that may be needed in order to run the programs in PythonPrograms. 

## PythonPrograms
The PythonPrograms folder contains runnable Python programs. Many of these programs require files from the Data folder. Be sure to check that you have downloaded the proper files indicated below before running these programs. When running the Python programs, be sure that the necessary files are moved into the same directory.


### filter2022.py
This file plots specifically the 2022 energy generation data of each state from the EIA on a choropleth map. It also generates a csv file with the data and saves it as 'filtered_generation_2022.csv'.

#### Necessary files
 - annual_generation_state.xlsx
 - filter2022.py

#### Dependencies

filter2022.py has the follwing dependencies:
 - plotly
 - pandas
 <!-- -->
These can be installed with the following, repectively

```bash
pip install plotly
```

```bash
pip install pandas
```

#### Running the Program

Navigate to the location of filter2022.py and run it using:

```bash
python3 filter2022.py
```

### ShapefileTesting.py 
This file is a work in progress to display the 8-digit Hydrologic Unit Codes of the US. These are used to distinguish between water subbasins.

#### Necessary Files
 - ShapefileTesting.py
 - WBDHU8.prj
 - WBDHU8.shp
 - WBDHU8.shx

#### Dependencies
ShapefileTesting.py has the follwing dependencies:
 - geopandas
 - pyshp
 - matplotlib
 <!-- -->
These can be installed with the following, repectively

```bash
pip install geopandas
```

```bash
pip install pyshp
```

```bash
pip install matplotlib
```

### Running the file

Navigate to the location of ShapefileTesting.py and run it using:

```bash
python3 ShapefileTesting.py
```


### StackedArea.py
This program generates a stacked area chart of Arizona's energy production from 2022.

#### Necessary Files
 - StackedArea.py
 - ArizonaOverTime.csv

#### Dependencies

StackedArea.py has the following dependencies:
 - matplotlib
 - pandas
 <!-- -->
 These can be installed with the following, respectively

```bash
pip install matplotlib
```

```bash
pip install pandas
```

#### Running the file

Navigate to the location of StackedArea.py and run it using

```bash
python3 StackedArea.py
```


### USStatesMap.py

This program will generate a chloropleth map of the Energy Generation Efficiency of states in the United States based on info from the EIA. 

#### Necessary Files

 - USStatesMap.py
 - combined.csv 

#### Dependencies

USStatesMap.py has the following dependencies:
 - plotly
 - pandas
<!-- -->
These can be installed with the following, respectively

```bash
pip install plotly
```

```bash
pip install pandas
```

#### Running the Program

Navigate to the location of USStatesMap.py and run it using:

```bash
python3 USStatesMap.py
```




## ResearchPaper

The ResearchPaper folder contains my research paper for this project as a LaTeX file. In order to compile this file and convert it to a pdf, follow the instructions listed further below. 




### AustinDeng_DataCenterSustainability.tex

This file is the LaTeX code for the research paper for this project.

#### Necessary Files

 - AustinDeng_DataCenterSustainability.tex
 - projection.png

#### Compiling and Creating PDF

Navigate to the location of AustinDeng_DataCenterSustainability.tex and compile using pdflatex:

```bash
pdflatex AustinDeng_DataCenterSustainability.tex
```


## The Project

The full main project has a broader scope, and is exploring the environmental costs of the increasing demand for data centers. There may be more files added depending on what kind of figures are needed or helpful for displaying the research done.

