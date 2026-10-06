# COVID-19 Data Visualisation

## Overview

This project visualises COVID-19 data supplied as part of the assessment.

The Python script loads the supplied data, cleans the numerical values, converts the dates into a format suitable for analysis, and creates a dashboard containing four visualisations.

The resulting dashboard is saved as:

`covid_dashboard.png`

## Files

* `COVID.py` - Python source code used to process and visualise the data.
* `covid_data.txt` - Supplied COVID-19 dataset.
* `covid_dashboard.png` - Generated visualisation dashboard.

## Requirements

The project uses Python 3 and the following libraries:

* **pandas** - Used to create and manipulate the DataFrame and clean the supplied data.
* **matplotlib** - Used to create the graphs and save the resulting dashboard.
* **json** - Used to read the JSON-formatted data. This is part of Python's standard library and does not need to be installed separately.

## Installing the External Libraries

The external libraries can be installed using:

```bash
pip install pandas matplotlib
```

## How the Code Works

### 1. Importing the libraries

The script imports `json`, `pandas`, `matplotlib.pyplot`, and `matplotlib.dates`.

`json` is used to read the supplied data, pandas is used for data processing, and Matplotlib is used for creating the visualisations and formatting the date axis.

### 2. Loading the data

The script opens `covid_data.txt` using UTF-8 encoding and loads the contents as JSON.

The JSON data is then converted into a pandas DataFrame so that it can be processed and visualised.

### 3. Cleaning the numerical data

Some numerical values in the supplied data contain spaces as thousands separators, for example `"1 139"`.

A `clean_number` function removes these spaces and converts the values to numeric values.

The function uses `errors="coerce"` so that values that cannot be converted to numbers are represented as missing values rather than causing the program to stop.

The numerical columns cleaned by the script are:

* Total Confirmed Cases
* Total Deaths
* Total Recovered
* Active Cases
* Daily Confirmed Cases
* Daily deaths

### 4. Processing the dates

The `Date` column is converted from text into pandas datetime values.

The data is then sorted by date and the DataFrame index is reset. This ensures that the data is in chronological order before it is plotted.

### 5. Creating the visualisation

The script creates a dashboard containing four separate graphs.

#### Total Confirmed Cases

The first graph is a line chart showing how the total number of confirmed cases changed over time.

#### Daily New Cases

The second graph uses bars to show daily confirmed cases.

A seven-day rolling average is also calculated and displayed as a line. This helps show the general trend while reducing the effect of daily fluctuations.

#### Total Deaths

The third graph shows the cumulative number of reported deaths over time.

#### Active vs Recovered

The fourth graph compares active cases with recovered cases over time using two line charts.

### 6. Date formatting

The x-axis is formatted using Matplotlib's date functionality.

Monthly labels are displayed and the labels are rotated so that they remain readable.

Grid lines are also added to make the graphs easier to read.

### 7. Saving the result

The completed dashboard is saved as:

`covid_dashboard.png`

The image is saved at 150 DPI so that it can be viewed clearly.

## Running the Program

Place the following files in the same directory:

```text
COVID.py
covid_data.txt
```

Then run:

```bash
python COVID.py
```

The program will generate:

```text
covid_dashboard.png
```

The graph will also be displayed when the script runs.

## Output

The output is a four-panel dashboard showing different aspects of the supplied COVID-19 data, including confirmed cases, daily cases, deaths, active cases and recovered cases.
