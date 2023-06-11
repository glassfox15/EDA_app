# Simple EDA Streamlit Application

[Streamlit app](https://glassfox15-streamlit-project-app-x1gp3t.streamlit.app/) for Stats 21, Spring 2023 at UCLA
 > https://glassfox15-streamlit-project-app-x1gp3t.streamlit.app/

This streamlit application was created by Jacob Titcomb. It (hopefully) performs a simple exploratory data analysis (EDA) of a provided data set.

*Please enjoy!*

## Structure of Application

First you will be prompted to input a `csv` file into the sidebar on the left. Once a `csv` file is uploaded you can choose between 3 data analysis options.
* The lowest complexity level is "General EDA"
* The middle complexity level is "Univariate"
* The highest complexity level is "Multivariate"

For most graphs, you will have the freedom to choose customization parameters such as color, opacity, bin-width (for histograms), etc.

Below each of the graphs there is a button labeled `Download image`. Clicking it will download the graphic as is onto your personal device.

## General EDA

Here we give basic information about the data set such as...

* The dimensions
* The column names
* The column data types
* The number of missing values in each column
* Optional summary statistics for all the numerical variables

## Univariate

This option dives into the behavior of a single variable of your choice.

* Numeric variables will generate summary statistics and a histogram
    + There is an option to include a line on the graph indicating where the mean lies
* Categorical variables will generate a bar graph based on the categories
    + You can choose between frequency and proportion
* Boolean variables will generate a donut plot
    + You can select both colors that go into the plot

## Multivariate

For each of these analyses, you will be prompted to choose a numerical variable as the first variable being studied. However, the second (and third!) variables can be different.

* Numerical second variable
    + This option generates a scatterplot
    + You have the option to also select a third variable of interest
        + This will choose a color scheme for the points and accommodates numerical, categorical, and boolean data types
* Categorical and boolean second variables
    + Both of these options will generate a set of box plots based on how the secondary variable partitions the primary (numerical) variable






