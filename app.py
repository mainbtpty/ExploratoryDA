import streamlit as st
import pandas as pd
import plotly.express as px

import functions

# Configure Streamlit page
st.set_page_config(layout="wide", page_icon='logo.png', page_title='EDA')



# Define functions for different pages


def main_page():
    
    st.header("🎨Exploratory Data Analysis Tool for Data Science Projects")
    st.write('<p style="font-size:160%">You will be able to✅:</p>', unsafe_allow_html=True)
    # List other functionalities...
    st.write('<p style="font-size:100%">&nbsp 1. See the whole dataset</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:100%">&nbsp 2. Get column names, data types info</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:100%">&nbsp 3. Get the count and percentage of NA values</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:100%">&nbsp 4. Get descriptive analysis </p>', unsafe_allow_html=True)
    st.write('<p style="font-size:100%">&nbsp 5. Check inbalance or distribution of target variable:</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:100%">&nbsp 6. See distribution of numerical columns</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:100%">&nbsp 7. See count plot of categorical columns</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:100%">&nbsp 8. Get outlier analysis with box plots</p>', unsafe_allow_html=True)
    st.write('<p style="font-size:100%">&nbsp 9. Obtain info of target value variance with categorical columns</p>', unsafe_allow_html=True)

    st.write(""" 
    [![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee--yellow.svg?logo=buy-me-a-coffee&logoColor=orange&style=social)](https://www.buymeacoffee.com/charlion) """)  # Adjust the URL as needed



    
    # Add the Hit Counters at the end of the main page
    st.markdown("""
        <!-- Histats.com  START (html only)-->
        <a href="/" alt="page hit counter" target="_blank" >
        <embed src="//s10.histats.com/13.swf"  flashvars="jver=1&acsid=4861133&domi=4"  quality="high"  width="180" height="50" name="13.swf"  align="middle" type="application/x-shockwave-flash" pluginspage="//www.macromedia.com/go/getflashplayer" wmode="transparent" /></a>
        <img  src="//sstatic1.histats.com/0.gif?4861133&101" alt="site stats free" border="0">
        <!-- Histats.com  END  -->
    """, unsafe_allow_html=True)




# Adding Buy Me A Coffee button to the sidebar
st.sidebar.write(""" 
    [![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee--yellow.svg?logo=buy-me-a-coffee&logoColor=orange&style=social)](https://www.buymeacoffee.com/charlion) """)  # Adjust the URL as needed




functions.space()
st.write('<p style="font-size:130%">EDA Tool for Data Science Projects</p>', unsafe_allow_html=True)
st.write('<p style="font-size:130%">Import Dataset</p>', unsafe_allow_html=True)

file_format = st.radio('Select file format:', ('csv', 'excel'), key='file_format')
dataset = st.file_uploader(label = '')

use_defo = st.checkbox('Use example Dataset')
if use_defo:
    dataset = 'CarPrice_Assignment.csv'

st.sidebar.header('Import Dataset to Use Available Features: 👉')
st.sidebar.write("Build By Charles K Oni")

if dataset:
    if file_format == 'csv' or use_defo:
        df = pd.read_csv(dataset)
    else:
        df = pd.read_excel(dataset)
    
    st.subheader('Dataframe:')
    n, m = df.shape
    st.write(f'<p style="font-size:130%">Dataset contains {n} rows and {m} columns.</p>', unsafe_allow_html=True)   
    st.dataframe(df)


    all_vizuals = ['Info', 'NA Info', 'Descriptive Analysis', 'Target Analysis', 
                   'Distribution of Numerical Columns', 'Count Plots of Categorical Columns', 
                   'Box Plots', 'Outlier Analysis', 'Variance of Target with Categorical Columns']
    functions.sidebar_space(3)         
    vizuals = st.sidebar.multiselect("Choose which visualizations you want to see 👇", all_vizuals)

    if 'Info' in vizuals:
        st.subheader('Info:')
        c1, c2, c3 = st.columns([1, 2, 1])
        c2.dataframe(functions.df_info(df))

    if 'NA Info' in vizuals:
        st.subheader('NA Value Information:')
        if df.isnull().sum().sum() == 0:
            st.write('There is not any NA value in your dataset.')
        else:
            c1, c2, c3 = st.columns([0.5, 2, 0.5])
            c2.dataframe(functions.df_isnull(df), width=1500)
            functions.space(2)
            

    if 'Descriptive Analysis' in vizuals:
        st.subheader('Descriptive Analysis:')
        st.dataframe(df.describe())
        
    if 'Target Analysis' in vizuals:
        st.subheader("Select target column:")    
        target_column = st.selectbox("", df.columns, index = len(df.columns) - 1)
    
        st.subheader("Histogram of target column")
        fig = px.histogram(df, x = target_column)
        c1, c2, c3 = st.columns([0.5, 2, 0.5])
        c2.plotly_chart(fig)


    num_columns = df.select_dtypes(exclude = 'object').columns
    cat_columns = df.select_dtypes(include = 'object').columns

    if 'Distribution of Numerical Columns' in vizuals:

        if len(num_columns) == 0:
            st.write('There is no numerical columns in the data.')
        else:
            selected_num_cols = functions.sidebar_multiselect_container('Choose columns for Distribution plots:', num_columns, 'Distribution')
            st.subheader('Distribution of numerical columns')
            i = 0
            while (i < len(selected_num_cols)):
                c1, c2 = st.columns(2)
                for j in [c1, c2]:

                    if (i >= len(selected_num_cols)):
                        break

                    fig = px.histogram(df, x = selected_num_cols[i])
                    j.plotly_chart(fig, use_container_width = True)
                    i += 1

    if 'Count Plots of Categorical Columns' in vizuals:

        if len(cat_columns) == 0:
            st.write('There is no categorical columns in the data.')
        else:
            selected_cat_cols = functions.sidebar_multiselect_container('Choose columns for Count plots:', cat_columns, 'Count')
            st.subheader('Count plots of categorical columns')
            i = 0
            while (i < len(selected_cat_cols)):
                c1, c2 = st.columns(2)
                for j in [c1, c2]:

                    if (i >= len(selected_cat_cols)):
                        break

                    fig = px.histogram(df, x = selected_cat_cols[i], color_discrete_sequence=['indianred'])
                    j.plotly_chart(fig)
                    i += 1

    if 'Box Plots' in vizuals:
        if len(num_columns) == 0:
            st.write('There is no numerical columns in the data.')
        else:
            selected_num_cols = functions.sidebar_multiselect_container('Choose columns for Box plots:', num_columns, 'Box')
            st.subheader('Box plots')
            i = 0
            while (i < len(selected_num_cols)):
                c1, c2 = st.columns(2)
                for j in [c1, c2]:
                    
                    if (i >= len(selected_num_cols)):
                        break
                    
                    fig = px.box(df, y = selected_num_cols[i])
                    j.plotly_chart(fig, use_container_width = True)
                    i += 1

    if 'Outlier Analysis' in vizuals:
        st.subheader('Outlier Analysis')
        c1, c2, c3 = st.columns([1, 2, 1])
        c2.dataframe(functions.number_of_outliers(df))

    if 'Variance of Target with Categorical Columns' in vizuals:
        
        
        df_1 = df.dropna()
        
        high_cardi_columns = []
        normal_cardi_columns = []

        for i in cat_columns:
            if (df[i].nunique() > df.shape[0] / 10):
                high_cardi_columns.append(i)
            else:
                normal_cardi_columns.append(i)


        if len(normal_cardi_columns) == 0:
            st.write('There is no categorical columns with normal cardinality in the data.')
        else:
        
            st.subheader('Variance of target variable with categorical columns')
            model_type = st.radio('Select Problem Type:', ('Regression', 'Classification'), key = 'model_type')
            selected_cat_cols = functions.sidebar_multiselect_container('Choose columns for Category Colored plots:', normal_cardi_columns, 'Category')
            
            if 'Target Analysis' not in vizuals:   
                target_column = st.selectbox("Select target column:", df.columns, index = len(df.columns) - 1)
            
            i = 0
            while (i < len(selected_cat_cols)):
                
                
            
                if model_type == 'Regression':
                    fig = px.box(df_1, y = target_column, color = selected_cat_cols[i])
                else:
                    fig = px.histogram(df_1, color = selected_cat_cols[i], x = target_column)

                st.plotly_chart(fig, use_container_width = True)
                i += 1

            if high_cardi_columns:
                if len(high_cardi_columns) == 1:
                    st.subheader('The following column has high cardinality, that is why its boxplot was not plotted:')
                else:
                    st.subheader('The following columns have high cardinality, that is why its boxplot was not plotted:')
                for i in high_cardi_columns:
                    st.write(i)
                
                st.write('<p style="font-size:140%">Do you want to plot anyway?</p>', unsafe_allow_html=True)    
                answer = st.selectbox("", ('No', 'Yes'))

                if answer == 'Yes':
                    for i in high_cardi_columns:
                        fig = px.box(df_1, y = target_column, color = i)
                        st.plotly_chart(fig, use_container_width = True)
                        # Create a sidebar navigation menu




def contact_us_page():
    st.markdown("<h2 style='text-align: center;'>Contact The Developer</h1>", unsafe_allow_html=True)
    st.write("Use the form below to get in touch with us.")
    st.write('<iframe src="https://formsubmit.co/el/jidexe" width="800" height="600"></iframe>', unsafe_allow_html=True)
    st.write(""" 
    [![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee--yellow.svg?logo=buy-me-a-coffee&logoColor=orange&style=social)](https://www.buymeacoffee.com/charlion) """)  # Adjust the URL as needed

    # Add the Hit Counters at the beginning
    st.markdown("""
        <!-- Histats.com  START (html only)-->
        <a href="/" alt="page hit counter" target="_blank" >
        <embed src="//s10.histats.com/13.swf"  flashvars="jver=1&acsid=4861133&domi=4"  quality="high"  width="180" height="50" name="13.swf"  align="middle" type="application/x-shockwave-flash" pluginspage="//www.macromedia.com/go/getflashplayer" wmode="transparent" /></a>
        <img  src="//sstatic1.histats.com/0.gif?4861133&101" alt="site stats free" border="0">
        <!-- Histats.com  END  -->
    """, unsafe_allow_html=True)




    st.sidebar.write(""" 
    [![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee--yellow.svg?logo=buy-me-a-coffee&logoColor=orange&style=social)](https://www.buymeacoffee.com/charlion) """)  # Adjust the URL as needed





# Create sidebar navigation menu
menu = st.sidebar.radio("Navigation", ["Home", "Contact Us", ])

# Display different pages based on user selection
if menu == "Home":
    main_page()
elif menu == "Contact Us":
    contact_us_page()
