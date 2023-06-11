import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import io

st.title('Exploratory Data Analysis App')

st.sidebar.subheader('Created by Jacob Titcomb')
uploaded_file = st.sidebar.file_uploader("Choose your data")


if uploaded_file is None:
    st.subheader("Perform exploratory data analysis on a data set of your choice.")
    st.markdown("Please begin by inputting your data on the left.")


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file) # read in data frame
    numeric_cols = [col for col in df.columns if df[col].dtype in ['int64', 'float64']]
    category_cols = [col for col in df.columns if df[col].dtype in ['category', 'object']]
    bool_cols = [col for col in df.columns if df[col].dtype == 'bool']


    web_apps = st.sidebar.selectbox("Choose your analysis",
                                    ("--", "General EDA", "Univariate", "Multivariate"))
    
    if web_apps == "--":
       st.subheader("Perform exploratory data analysis on a data set of your choice.")
    else:
       st.header(f"Analysis type: {web_apps}")
       
    # Summaries of general features of data frame
    if web_apps == "General EDA":
       show_df = st.checkbox("Show data frame", key="disabled")

       if show_df:
         st.write(df)

       st.header("General features")
       st.subheader("Data frame dimensions")
       st.markdown(f"Rows: {df.shape[0]}")
       st.markdown(f"Columns: {df.shape[1]}")
       st.subheader("Column names")
       st.write(df.columns)
       st.subheader("Column data types")
       st.write(df.dtypes)
       st.subheader("Missing values in each column")
       st.write(df.isna().sum())

       # 5 number summary of numeric data
       st.subheader("Further analysis")
       num_sum = st.checkbox("Summary statistics of numeric variables")
       if num_sum:
          st.write(df.describe())

    # Univariate analysis

    existing_dtypes = [["Numerical", "Categorical", "Boolean"][i]
                       for i in range(3)
                       if (np.array((len(numeric_cols),
                                     len(category_cols),
                                     len(bool_cols))) > 0)[i]]
    
    # Univariate analysis
    if web_apps == "Univariate":
       st.subheader("Variable selection")
       var_type = st.selectbox('Select data type',
                               existing_dtypes)
       
       # === Numeric types =====================================
       if var_type == "Numerical":
        var1 = st.selectbox("Select column of interest",
                              numeric_cols)
          
        st.subheader("Summary statistics")
        st.table(df[var1].describe())

        # histogram
        st.subheader("Histogram")

        choose_color = st.color_picker('Pick a color', "#69b3a2")
        choose_opacity = st.slider(
             'Color opacity', min_value=0.0, max_value=1.0,
             step=0.05, value = 0.9)
        hist_bins = st.slider('Number of bins', min_value=5,
                            max_value=min([round(len(df[var1]) / 2), 75]),
                            value=20)
        hist_title = st.text_input('Set title', 'Histogram')
        hist_xtitle = st.text_input('Set x-axis title', var1)
        hist_mean = st.checkbox("Show mean")

        fig, ax = plt.subplots()
        ax.hist(df[var1], bins=hist_bins,
            edgecolor="black", color=choose_color, alpha=choose_opacity)
        ax.set_title(hist_title)
        ax.set_xlabel(hist_xtitle)
        ax.set_ylabel('Frequency')
        
        if hist_mean:
            plt.axvline(x=df[var1].mean(), color='red', ls='--')

        st.pyplot(fig)
        if len(hist_title) == 0:
            hist_title = "plot"
        filename = hist_title + ".png"
        filename = filename.replace(" ", "_")

        # Save the figure to a BytesIO object
        image_bytes = io.BytesIO()
        fig.savefig(image_bytes, format='png', dpi=300)
        plt.close(fig)

        # Display the download button
        st.download_button(
            label="Download image",
            data=image_bytes,
            file_name=filename,
            mime="image/png"
        )
        
             
       # === Categorical types =====================================
       if var_type == "Categorical":
          var1 = st.selectbox("Select column of interest",
                              category_cols)
          
          # table of proportions
          st.subheader("Proportions by category")
          st.table(df[var1].value_counts(normalize=True))


        #   # barplot
          st.subheader("Bar plot")
          choose_color = st.color_picker('Pick a color', "#69b3a2")
          choose_opacity = st.slider(
             'Color opacity', min_value=0.0, max_value=1.0,
             step=0.05, value = 0.9)
          bar_title = st.text_input('Set title', 'Bar plot')
          bar_xtitle = st.text_input('Set x-axis title', var1)
          bar_freq = st.checkbox("Frequency")
          if bar_freq:
             bar_data = df[var1].value_counts(normalize=False)
          else:
             bar_data = df[var1].value_counts(normalize=True)

          fig, ax = plt.subplots()
          ax.bar(x = bar_data.index,
                 height=bar_data,
                 edgecolor="black", color=choose_color, alpha=choose_opacity)
          ax.set_title(bar_title)
          ax.set_xlabel(bar_xtitle)
          if bar_freq:
             ax.set_ylabel('Frequency')
          else:
             ax.set_ylabel('Proportion')
          st.pyplot(fig)


          if len(bar_title) == 0:
             bar_title = "plot"
          filename = bar_title + ".png"
          filename = filename.replace(" ", "_")

          # Save the figure to a BytesIO object
          image_bytes = io.BytesIO()
          fig.savefig(image_bytes, format='png', dpi=300)
          plt.close(fig)
          
          # Display the download button
          st.download_button(
            label="Download image",
            data=image_bytes,
            file_name=filename,
            mime="image/png"
            ) 
          
       # === Boolean types =====================================
       if var_type == "Boolean":
          var1 = st.selectbox("Select column of interest",
                              bool_cols)
          
          # table of proportions
          st.subheader("Proportions")
          st.table(df[var1].value_counts(normalize=True))
          
          # Donut plot
          st.subheader("Donut plot")
          choose_color1 = st.color_picker('Pick color 1', "#9084E8")
          choose_color2 = st.color_picker('Pick color 2', "#E8D684")
          choose_opacity = st.slider(
             'Color Opacity', min_value=0.0, max_value=1.0,
             step=0.05, value = 0.9)
          don_title = st.text_input('Set title', 'Donut plot')
          don_xtitle = st.text_input('Set x-axis title', var1)
          don_data = df[var1].value_counts(normalize=False)

          fig, ax = plt.subplots()
          ax.pie(don_data,
                 colors = np.array([choose_color1, choose_color2]),
                 labels = ["True", "False"])
          ax.set_title(don_title)
          ax.set_xlabel(don_xtitle)
          # adding white circle inside
          add_circle = plt.Circle( (0,0), 0.7, color='white')
          donut = plt.gcf()
          donut.gca().add_artist(add_circle)
        
          st.pyplot(donut)


          if len(don_title) == 0:
             don_title = "plot"
          filename = don_title + ".png"
          filename = filename.replace(" ", "_")

          # Save the figure to a BytesIO object
          image_bytes = io.BytesIO()
          donut.savefig(image_bytes, format='png', dpi=300)
          plt.close(donut)
          
          # Display the download button
          st.download_button(
            label="Download image",
            data=image_bytes,
            file_name=filename,
            mime="image/png"
            ) 
             


    # Multivariate analysis
    if web_apps == "Multivariate":
       avail_numeric = numeric_cols
       st.subheader("Variable selection")

       var_X = st.selectbox('Select a numerical variable',
                               numeric_cols)
       avail_numeric = [value for value in avail_numeric if value != var_X]
       avail_dtypes = [["Numerical", "Categorical", "Boolean"][i]
                       for i in range(3)
                       if (np.array((len(avail_numeric),
                                     len(category_cols),
                                     len(bool_cols))) > 0)[i]]

       var_Y_type = st.selectbox("Select data type of secondary variable",
                                 avail_dtypes)
       
       # Non-numeric secondary variable
       if var_Y_type != "Numerical":
        if var_Y_type == "Categorical":
            var_Y = st.selectbox("Select secondary variable",
                                 category_cols)
        if var_Y_type == "Boolean":
           var_Y = st.selectbox("Select secondary variable",
                                bool_cols)
        
        st.subheader("Parameters for plotting")
        box_title = st.text_input('Set title', 'Box plots')
        box_xtitle = st.text_input('Set x-axis title', var_Y)
        box_ytitle = st.text_input('Set y-axis title', var_X)

        st.subheader("Box plot")
        fig, ax = plt.subplots()
        sns.boxplot(data=df, x=var_Y, y=var_X)
        ax.set_title(box_title)
        ax.set_xlabel(box_xtitle)
        ax.set_ylabel(box_ytitle)

        st.pyplot(fig)

        if len(box_title) == 0:
           box_title = "plot"
        filename = box_title + ".png"
        filename = filename.replace(" ", "_")

        # Save the figure to a BytesIO object
        image_bytes = io.BytesIO()
        fig.savefig(image_bytes, format='png', dpi=300)
        plt.close(fig)
          
        # Display the download button
        st.download_button(
           label="Download image",
           data=image_bytes,
           file_name=filename,
           mime="image/png"
           )
        

       # Numeric secondary variable
       if var_Y_type == "Numerical":
        var_Y = st.selectbox("Select secondary variable",
                             avail_numeric)
        avail_cols = [value for value in df.columns if value not in [var_X, var_Y]]
        var_Z_bool = st.checkbox("Include tertiary variable")
        if var_Z_bool:
           var_Z = st.selectbox("Select tertiary variable",
                                avail_cols)
           
        # scatterplot
        st.subheader("Parameters for plotting")

        if var_Z_bool == False:
           choose_color = st.color_picker('Pick a color', "#69b3a2")
        choose_opacity = st.slider(
            'Color opacity', min_value=0.0, max_value=1.0,
            step=0.05, value = 0.9)
        scat_title = st.text_input('Set title', 'Scatter plot')
        scat_xtitle = st.text_input('Set x-axis title', var_X)
        scat_ytitle = st.text_input('Set y-axis title', var_Y)
        if var_Z_bool:
           legend_bool = st.checkbox("Include legend")
           if legend_bool: st.markdown("*Sorry, but this functionality is not supported at this time.*")

        st.subheader("Scatter plot")
        fig, ax = plt.subplots()
        if var_Z_bool:
           sns.scatterplot(x=var_X, y=var_Y, hue = var_Z,
                           data=df,
                           alpha=choose_opacity, edgecolor="black")
        else:
           ax.scatter(x=var_X, y=var_Y, c=choose_color,
                      data=df,
                      alpha=choose_opacity, edgecolor="black")
        ax.set_title(scat_title)
        ax.set_xlabel(scat_xtitle)
        ax.set_ylabel(scat_ytitle)

        st.pyplot(fig)
        if len(scat_title) == 0:
            scat_title = "plot"
        filename = scat_title + ".png"
        filename = filename.replace(" ", "_")

        # Save the figure to a BytesIO object
        image_bytes = io.BytesIO()
        fig.savefig(image_bytes, format='png', dpi=300)
        plt.close(fig)

        # Display the download button
        st.download_button(
            label="Download image",
            data=image_bytes,
            file_name=filename,
            mime="image/png"
        )
