#For requirements file
#!pip install -r requirements.txt
#pip install matplotlib
#pip install scikit-learn
#pip install seaborn

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
import seaborn as sns
#to help download the dataset
import os
#to help open the dataset from Kaggle
import opendatasets as od
import plotly.graph_objects as go
import plotly.figure_factory as ff


#STREAMLIT APP
st.title("**Welcome to Healthy Moves**")
# Rhythm and Burn, Healthy Moves, Healthy Steps, Rhythm Revive Repeat, 
st.header("Let's Start Your Dance Journey!")
#st.image('/Users/kendallandrews/Downloads/groupdance.jpg')
st.image('groupdance.jpg')

#Datasets
df = pd.read_csv('/Users/kendallandrews/Downloads/dances/dance data.csv', encoding='latin-1')
df2 = pd.read_csv("/Users/kendallandrews/Downloads/calories-burned-during-exercise-and-activities/exercise_dataset.csv")
d3 = df2.drop(['130 lb', '155 lb', '180 lb', '205 lb'], axis=1)
d3 = d3.iloc[[29, 34, 35, 36],:]
df3 = pd.read_csv("/Users/kendallandrews/Downloads/CVD_cleaned.csv")

#Tabs -> Sidebar
pages = st.sidebar.radio("Pages:", ['Home Page', 'Profile', 'Library', 'Background', "FAQ's", 'Data Science Work'])
# -> DS Sections - ['IDA', 'Data EDA', 'Cleaning', 'Encoding', 'Imputing', 'Modeling'])

#st.write("Click on the Profile tab in the left hand corner to start creating your Profile ")

if pages == 'Profile':
    st.subheader("**Profile**")

    name_input = st.text_input("Name:")
    age_input = st.number_input("Age:")
    weight_input = st.number_input("Weight:")
    birthday_input = st.date_input("Birthday (MM/DD/YYYY):", format="MM/DD/YYYY")

    #if st.text_input:
       # st.write("You Name: ", name)
    st.divider()
    

    st.subheader("Question 1: What is your favorite dance type?") #dance type in df

    dance_types = sorted(list(set(df['Dance Type'].tolist())))
    
    # Create a select box with unique dance types
    ans1 = st.selectbox("Dance Type", dance_types)
    st.write(f"**Great! You've selected: {ans1}**")

    st.divider() 

    #Question 2
    st.subheader("Question 2: What is your favorite dance style?") #dance style in df
    dance_styles = sorted(list(set(df['Dance style'].tolist())))
    ans2 = st.selectbox("Dance Style", dance_styles)
    st.write(f"**Great! You've selected: {ans2}**")

    #Special text for this Did you know section
    st.write(f":red[*Did you know that **{ans1} {ans2}**, can provide health benefits?*]")

    st.divider() 

    #Question 3
    st.subheader("Question 3: What health problems do you want to focus on? ")

    #Health Benefits Matrix Code
    health_benefits_split = df['Health Benefits'].str.split(",")
    my_list = health_benefits_split.tolist()

    #Create an empty list of each health benefit

    Improved_cardiovascular_health = []
    for i in range(len(my_list)):
        if 'Improved cardiovascular health' in my_list[i]:
            Improved_cardiovascular_health.append(1)
        elif 'Improved cardiov' in my_list[i]:
            Improved_cardiovascular_health.append(1)
        elif 'Improved cardiovascular health and increased physical fitness' in my_list[i]:
            Improved_cardiovascular_health.append(1)
        elif 'Cardiovascular health' in my_list[i]:
            Improved_cardiovascular_health.append(1)
        elif 'Positive effects on cardiovascular health' in my_list[i]:
            Improved_cardiovascular_health.append(1)
        elif 'Moderate cardiovascular workout' in my_list[i]:
            Improved_cardiovascular_health.append(1)
        elif ' such as improved cardiovascular' in my_list[i]:
            Improved_cardiovascular_health.append(1)
        else:
            Improved_cardiovascular_health.append(0)

    Improved_flexibility = []
    for i in range(len(my_list)):
        if " Improved flexibility" in my_list[i]:
            Improved_flexibility.append(1)
        elif " and Improved flexibility." in my_list[i]:
            Improved_flexibility.append(1)
        elif ' and Improved flexibility' in my_list[i]:
            Improved_flexibility.append(1)
        elif " and improved flexibility" in my_list[i]:
            Improved_flexibility.append(1)
        elif 'Improved flexibility and strength' in my_list[i]:
            Improved_flexibility.append(1)
        elif 'Improved strength and flexibility' in my_list[i]:
            Improved_flexibility.append(1)
        elif ' Flexibility' in my_list[i]:
            Improved_flexibility.append(1)
        else:
            Improved_flexibility.append(0)

    Stress_relief = []
    for i in range(len(my_list)):
        if " Stress relief" in my_list[i]:
            Stress_relief.append(1)
        elif "Stress relief" in my_list[i]:
            Stress_relief.append(1)
        elif ' stress relief' in my_list[i]:
            Stress_relief.append(1)
        elif 'Reduces stress' in my_list[i]:
            Stress_relief.append(1)
        elif 'Stress relief and improved mood' in my_list[i]:
            Stress_relief.append(1)
        elif 'Reduces stress and anxiety'  in my_list[i]:
            Stress_relief.append(1)
        else:
            Stress_relief.append(0)

    Confidence = []
    for i in range(len(my_list)):
        if " and Increased self-confidence" in my_list[i]:
            Confidence.append(1)
        elif " Increased self-confidence" in my_list[i]:
            Confidence.append(1)
        elif "Increased self-confidence" in my_list[i]:
            Confidence.append(1)
        elif ' Improved self-confidence' in my_list[i]:
            Confidence.append(1)
        elif ' Increased self-esteem' in my_list[i]:
            Confidence.append(1)
        elif ' and Increased self-' in my_list[i]:
            Confidence.append(1)
        else:
            Confidence.append(0)

    Physical_fitness = []
    for i in range(len(my_list)):
        if " and increased physical fitness" in my_list[i]:
            Physical_fitness.append(1)
        elif " Increased physical fitness" in my_list[i]:
            Physical_fitness.append(1)
        elif "Improved physical fitness" in my_list[i]:
            Physical_fitness.append(1)
        elif " Improved physical fitness" in my_list[i]:
            Physical_fitness.append(1)
        elif '  Increased physical activity' in my_list[i]:
            Physical_fitness.append(1)
        elif ' and Muscle' in my_list[i]:
            Physical_fitness.append(1)
        elif ' Enhanced physical fitness' in my_list[i]:
            Physical_fitness.append(1)
        elif ' Weight loss' in my_list[i]:
            Physical_fitness.append(1)
        elif ' Burning calories and losing' in my_list[i]:
            Physical_fitness.append(1)
        elif 'Potential physical or mental health benefits associated with performing the dance. This describes' in my_list[i]:
            Physical_fitness.append(1)
        elif 'Increased physical activity and exercise' in my_list[i]:
            Physical_fitness.append(1)
        else:
            Physical_fitness.append(0)

    Social_connection = []
    for i in range(len(my_list)):
        if " and Social connection" in my_list[i]:
            Social_connection.append(1)
        elif "Social connection" in my_list[i]:
            Social_connection.append(1)
        elif " Social connections" in my_list[i]:
            Social_connection.append(1)
        elif " and social connection" in my_list[i]:
            Social_connection.append(1)
        elif ' and Improved social skills' in my_list[i]:
            Social_connection.append(1)
        else:
            Social_connection.append(0)

    Mental_health = []
    for i in range(len(my_list)):
        if " and improves mental health" in my_list[i]:
            Mental_health.append(1)
        elif "Improves mental health" in my_list[i]:
            Mental_health.append(1)
        elif " Improves mental health" in my_list[i]:
            Mental_health.append(1)
        elif 'Reduces stress and improves mental health' in my_list[i]:
            Mental_health.append(1)
        elif 'Dancing can offer physical and mental health benefits' in my_list[i]:
            Mental_health.append(1)
        elif 'The Zapateado dance has the potential to offer numerous physical and mental health' in my_list[i]:
            Mental_health.append(1)
        elif 'Potential physical or mental health benefits associated with performing the dance. This describes' in my_list[i]:
            Mental_health.append(1)
        elif 'potential_physical_mental_health_benefits' in my_list[i]:
            Mental_health.append(1)
        else:
            Mental_health.append(0)

    Strength = []
    for i in range(len(my_list)):
        if "Improved flexibility and strength" in my_list[i]:
            Strength.append(1)
        elif "Improved strength and flexibility" in my_list[i]:
            Strength.append(1)
        else:
            Strength.append(0)

    Community = []
    for i in range(len(my_list)):
        if " A sense of community and belonging" in my_list[i]:
            Community.append(1)
        else:
            Community.append(0)

    Boost = []
    for i in range(len(my_list)):
        if " Boost" in my_list[i]:
            Boost.append(1)
        elif "Boost" in my_list[i]:
            Boost.append(1)
        elif 'Stress relief and improved mood' in my_list[i]:
            Boost.append(1)
        elif ' Boosted mood'in my_list[i]:
            Boost.append(1)
        elif ' and Increased energy' in my_list[i]:
            Boost.append(1)
        elif ' Increased energy levels' in my_list[i]:
            Boost.append(1)
        elif '55]: Increased happiness and well-being'in my_list[i]:
            Boost.append(1)
        else:
            Boost.append(0)

    Cerebellum = []
    for i in range(len(my_list)):
        if " Improved balance" in my_list[i]:
            Cerebellum.append(1)
        elif "Improved balance" in my_list[i]:
            Cerebellum.append(1)
        elif ' and improved coordination' in my_list[i]:
            Cerebellum.append(1)
        elif ' Improved coordination' in my_list[i]:
            Cerebellum.append(1)
        elif ' Improved balance and coordination' in my_list[i]:
            Cerebellum.append(1)
        elif ' Improved cognitive function' in my_list[i]:
            Cerebellum.append(1)
        elif ' Improved posture' in my_list[i]:
            Cerebellum.append(1)
        elif ' Improved balance and' in my_list[i]:
            Cerebellum.append(1)
        elif ' Improved balance and coord' in my_list[i]:
            Cerebellum.append(1)
        elif ' Improved posture' in my_list[i]:
            Cerebellum.append(1)
        elif 'Improved posture' in my_list[i]:
            Cerebellum.append(1)
        else:
            Cerebellum.append(0)

    #Create a matrix for each health benefit
    #health_benefits_matrix = pd.DataFrame([Improved_cardiovascular_health, Improved_flexibility, Stress_relief, confidence, physical_fitness,social_connection, mental_health, strength, community, boost, cerebellum])
    #print(type(health_benefits_matrix))
    health_benefits_matrix = pd.DataFrame({
        'Improved_cardiovascular_health': Improved_cardiovascular_health,
        'Improved_flexibility': Improved_flexibility,
        'Stress_relief': Stress_relief,
        'Confidence': Confidence,
        'Physical_fitness': Physical_fitness,
        'Social_connection': Social_connection,
        'Mental_health': Mental_health,
        'Strength': Strength,
        'Community': Community, 
        'Boost': Boost,
        'Cerebellum': Cerebellum
    })

    dance_names = df['Dance style'].tolist()  # Convert dance styles to a list

    # Iterate over the DataFrame by rows and columns to replace 1s
    for col in health_benefits_matrix.columns:  # Iterate over each column
        for row in range(len(health_benefits_matrix)):  # Iterate over each row
            if health_benefits_matrix.at[row, col] == 1:  # Access element by row and column
                health_benefits_matrix.at[row, col] = dance_names[row]  # Replace 1 with the dance name

    #health_benefits = (sorted(health_benefits_matrix.columns.str.replace("_", " ")))
    health_benefits = (sorted(health_benefits_matrix.columns))

    ans3 = st.selectbox("Health Problems", health_benefits)
    st.write(f"**Great! You've selected: {ans3}**")
 

    # Dictionary to store which dances are associated with each health benefit
    dance_in_columns = {}

    # Iterate over each column to check for dance names
    for col in health_benefits_matrix.columns:
        dances_in_col = health_benefits_matrix[col].unique()  # Get unique values in the column
        dances_in_col = [dance for dance in dances_in_col if pd.notna(dance) and dance != 0]  # Exclude NaNs and zeros
        dance_in_columns[col] = dances_in_col

    if ans2 in dance_in_columns[ans3]:
        st.write(f":red[*Did you know doing {ans2} helps you with {ans3}?*]")
    else:
        st.write(f"{ans2} may not directly help with {ans3}, but there are other dances that do!")

    st.divider() 

    st.subheader("Lets practice some dancing to improve your health!!!")

if pages == 'Library':
    st.subheader("**Library**")
    st.write("Collection of Dances")

    #Filter data
    filter = st.selectbox("Dance Type", df["Dance style"].unique())
    filtered = df[df["Dance style"]  == filter]
    st.write(filtered)

    st.write("Loading...")

if pages == 'Background':
    st.subheader("**Background Data**")

    st.write("With the dances in our database, we have the most information of the health benefits of **Improved cardiovascular health**, **Stress relief**, and **Flexibility**")
    
    #Plot
    #Health Benefits Matrix Code
    health_benefits_split = df['Health Benefits'].str.split(",")
    my_list = health_benefits_split.tolist()

    #Create an empty list of each health benefit
    Improved_cardiovascular_health = []
    for i in range(len(my_list)):
        if 'Improved cardiovascular health' in my_list[i]:
            Improved_cardiovascular_health.append(1)
        elif 'Improved cardiov' in my_list[i]:
            Improved_cardiovascular_health.append(1)
        elif 'Improved cardiovascular health and increased physical fitness' in my_list[i]:
            Improved_cardiovascular_health.append(1)
        elif 'Cardiovascular health' in my_list[i]:
            Improved_cardiovascular_health.append(1)
        elif 'Positive effects on cardiovascular health' in my_list[i]:
            Improved_cardiovascular_health.append(1)
        elif 'Moderate cardiovascular workout' in my_list[i]:
            Improved_cardiovascular_health.append(1)
        elif ' such as improved cardiovascular' in my_list[i]:
            Improved_cardiovascular_health.append(1)
        else:
            Improved_cardiovascular_health.append(0)

    Improved_flexibility = []
    for i in range(len(my_list)):
        if " Improved flexibility" in my_list[i]:
            Improved_flexibility.append(1)
        elif " and Improved flexibility." in my_list[i]:
            Improved_flexibility.append(1)
        elif ' and Improved flexibility' in my_list[i]:
            Improved_flexibility.append(1)
        elif " and improved flexibility" in my_list[i]:
            Improved_flexibility.append(1)
        elif 'Improved flexibility and strength' in my_list[i]:
            Improved_flexibility.append(1)
        elif 'Improved strength and flexibility' in my_list[i]:
            Improved_flexibility.append(1)
        elif ' Flexibility' in my_list[i]:
            Improved_flexibility.append(1)
        else:
            Improved_flexibility.append(0)

    Stress_relief = []
    for i in range(len(my_list)):
        if " Stress relief" in my_list[i]:
            Stress_relief.append(1)
        elif "Stress relief" in my_list[i]:
            Stress_relief.append(1)
        elif ' stress relief' in my_list[i]:
            Stress_relief.append(1)
        elif 'Reduces stress' in my_list[i]:
            Stress_relief.append(1)
        elif 'Stress relief and improved mood' in my_list[i]:
            Stress_relief.append(1)
        elif 'Reduces stress and anxiety'  in my_list[i]:
            Stress_relief.append(1)
        else:
            Stress_relief.append(0)

    Confidence = []
    for i in range(len(my_list)):
        if " and Increased self-confidence" in my_list[i]:
            Confidence.append(1)
        elif " Increased self-confidence" in my_list[i]:
            Confidence.append(1)
        elif "Increased self-confidence" in my_list[i]:
            Confidence.append(1)
        elif ' Improved self-confidence' in my_list[i]:
            Confidence.append(1)
        elif ' Increased self-esteem' in my_list[i]:
            Confidence.append(1)
        elif ' and Increased self-' in my_list[i]:
            Confidence.append(1)
        else:
            Confidence.append(0)

    Physical_fitness = []
    for i in range(len(my_list)):
        if " and increased physical fitness" in my_list[i]:
            Physical_fitness.append(1)
        elif " Increased physical fitness" in my_list[i]:
            Physical_fitness.append(1)
        elif "Improved physical fitness" in my_list[i]:
            Physical_fitness.append(1)
        elif " Improved physical fitness" in my_list[i]:
            Physical_fitness.append(1)
        elif '  Increased physical activity' in my_list[i]:
            Physical_fitness.append(1)
        elif ' and Muscle' in my_list[i]:
            Physical_fitness.append(1)
        elif ' Enhanced physical fitness' in my_list[i]:
            Physical_fitness.append(1)
        elif ' Weight loss' in my_list[i]:
            Physical_fitness.append(1)
        elif ' Burning calories and losing' in my_list[i]:
            Physical_fitness.append(1)
        elif 'Potential physical or mental health benefits associated with performing the dance. This describes' in my_list[i]:
            Physical_fitness.append(1)
        elif 'Increased physical activity and exercise' in my_list[i]:
            Physical_fitness.append(1)
        else:
            Physical_fitness.append(0)

    Social_connection = []
    for i in range(len(my_list)):
        if " and Social connection" in my_list[i]:
            Social_connection.append(1)
        elif "Social connection" in my_list[i]:
            Social_connection.append(1)
        elif " Social connections" in my_list[i]:
            Social_connection.append(1)
        elif " and social connection" in my_list[i]:
            Social_connection.append(1)
        elif ' and Improved social skills' in my_list[i]:
            Social_connection.append(1)
        else:
            Social_connection.append(0)

    Mental_health = []
    for i in range(len(my_list)):
        if " and improves mental health" in my_list[i]:
            Mental_health.append(1)
        elif "Improves mental health" in my_list[i]:
            Mental_health.append(1)
        elif " Improves mental health" in my_list[i]:
            Mental_health.append(1)
        elif 'Reduces stress and improves mental health' in my_list[i]:
            Mental_health.append(1)
        elif 'Dancing can offer physical and mental health benefits' in my_list[i]:
            Mental_health.append(1)
        elif 'The Zapateado dance has the potential to offer numerous physical and mental health' in my_list[i]:
            Mental_health.append(1)
        elif 'Potential physical or mental health benefits associated with performing the dance. This describes' in my_list[i]:
            Mental_health.append(1)
        elif 'potential_physical_mental_health_benefits' in my_list[i]:
            Mental_health.append(1)
        else:
            Mental_health.append(0)

    Strength = []
    for i in range(len(my_list)):
        if "Improved flexibility and strength" in my_list[i]:
            Strength.append(1)
        elif "Improved strength and flexibility" in my_list[i]:
            Strength.append(1)
        else:
            Strength.append(0)

    Community = []
    for i in range(len(my_list)):
        if " A sense of community and belonging" in my_list[i]:
            Community.append(1)
        else:
            Community.append(0)

    Boost = []
    for i in range(len(my_list)):
        if " Boost" in my_list[i]:
            Boost.append(1)
        elif "Boost" in my_list[i]:
            Boost.append(1)
        elif 'Stress relief and improved mood' in my_list[i]:
            Boost.append(1)
        elif ' Boosted mood'in my_list[i]:
            Boost.append(1)
        elif ' and Increased energy' in my_list[i]:
            Boost.append(1)
        elif ' Increased energy levels' in my_list[i]:
            Boost.append(1)
        elif '55]: Increased happiness and well-being'in my_list[i]:
            Boost.append(1)
        else:
            Boost.append(0)

    Cerebellum = []
    for i in range(len(my_list)):
        if " Improved balance" in my_list[i]:
            Cerebellum.append(1)
        elif "Improved balance" in my_list[i]:
            Cerebellum.append(1)
        elif ' and improved coordination' in my_list[i]:
            Cerebellum.append(1)
        elif ' Improved coordination' in my_list[i]:
            Cerebellum.append(1)
        elif ' Improved balance and coordination' in my_list[i]:
            Cerebellum.append(1)
        elif ' Improved cognitive function' in my_list[i]:
            Cerebellum.append(1)
        elif ' Improved posture' in my_list[i]:
            Cerebellum.append(1)
        elif ' Improved balance and' in my_list[i]:
            Cerebellum.append(1)
        elif ' Improved balance and coord' in my_list[i]:
            Cerebellum.append(1)
        elif ' Improved posture' in my_list[i]:
            Cerebellum.append(1)
        elif 'Improved posture' in my_list[i]:
            Cerebellum.append(1)
        else:
            Cerebellum.append(0)

    #Create a matrix for each health benefit
    #health_benefits_matrix = pd.DataFrame([Improved_cardiovascular_health, Improved_flexibility, Stress_relief, confidence, physical_fitness,social_connection, mental_health, strength, community, boost, cerebellum])
    #print(type(health_benefits_matrix))
    health_benefits_matrix = pd.DataFrame({
        'Improved_cardiovascular_health': Improved_cardiovascular_health,
        'Improved_flexibility': Improved_flexibility,
        'Stress_relief': Stress_relief,
        'Confidence': Confidence,
        'Physical_fitness': Physical_fitness,
        'Social_connection': Social_connection,
        'Mental_health': Mental_health,
        'Strength': Strength,
        'Community': Community, 
        'Boost': Boost,
        'Cerebellum': Cerebellum
    })

    st.title("Heatmap for Health Benefits Matrix")
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(health_benefits_matrix, annot=True, cmap='coolwarm')
    st.pyplot(fig)
    
    st.subheader("Let's start with **Improved cardiovascular health**!")

    st.write("Cardivascular health can by your sex, age,height, weight, BMI. Other diseases may impact heart diesease such as: diabetes, arthiris, smoking, and depression. ")
    #Depression, **Diabetes**, **Arthiritis**, Sex, Age, Height, Weight, BMI, **Smoking**
    
    
    ##Code for Evidence:
    #IDA Step 2: Data cleaning and preprocessing - Handle missing values - Remove duplicates - Correct data types - Standardize formats
    #  Cardiovascular dataset
    import sklearn
    from sklearn.preprocessing import OrdinalEncoder, LabelEncoder, OneHotEncoder
    from scipy.stats import zscore

    le = LabelEncoder()
    #oe = OrdinalEncoder(categories=[['Poor','Fair','Good','Very Good','Excellent']])
    df3['General_Health']= le.fit_transform(df3['General_Health'])
    #Poor - 0 ', 'Fair - 1','Good- 2', 'Very Good - 3', 'Excellent - 4']) 

    # Fit and transform the data
    df3['Exercise'] = le.fit_transform(df3['Exercise'])
    #print(Exercise)
    #N - 0, Y - 1

    df3['Heart_Disease'] = le.fit_transform(df3['Heart_Disease'])
    #rint(heart_d)
    #N - 0, Y - 1

    df3['Depression']= le.fit_transform(df3['Depression'])
    #print(depression)
    #N - 0, Y - 1

    df3['Diabetes'] = le.fit_transform(df3['Diabetes'])
    #print(diabetes)
    #N - 0, Y - 1

    df3['Arthritis'] = le.fit_transform(df3['Arthritis'])
    #print(arth)
    #N - 0, Y - 1

    df3['Sex']= le.fit_transform(df3['Sex'])
    #print(sex)
    #F - 0, M - 1

    df3['Smoking_History'] = le.fit_transform(df3['Smoking_History'])
    #print(smoke)
    #N - 0, Y - 1

    oe = OrdinalEncoder(categories=[['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80+']])
    #print(df3['Age_Category'])
    #df3['General_Health']= le.fit_transform(df3['General_Health'])
    df3['Age_Category'] = le.fit_transform(df3['Age_Category'])

    #dropped new le columns because they are returning copies into the overall dataset instead of overwritting 
    #df3.drop(['Age_Category1'], axis=1, inplace=True)

    #Standardize formats
    numeric_cols_df3 = df3.select_dtypes(include=[np.number]).columns
    z3 = df3[numeric_cols_df3].apply(zscore)

    #Plot

    # Streamlit display
    st.title("Correlation Heatmap Example")
    st.write("This is the correlation heatmap showing the relationships between various metrics in cardiovascular dataset")

    # Create the heatmap using seaborn
    corr_matrix = df3[numeric_cols_df3].corr()
    fig, ax = plt.subplots(figsize=(20, 16))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)

    # Display the heatmap in Streamlit
    st.pyplot(fig)

    st.write("In order to keep good cardiovascular health you should keep a **heart-healthy diet**, **stay active**, **keep a health weight**, **Do not partake in smoking and drink alcohol in moderation**.")
    st.write("To help you stay active, the dances you can do to prevent heart disease are as follows:")

    #Create own dataset
    dance_names = df['Dance style'].tolist()  # Convert dance styles to a list

    # Iterate over the DataFrame by rows and columns to replace 1s
    for col in health_benefits_matrix.columns:  # Iterate over each column
        for row in range(len(health_benefits_matrix)):  # Iterate over each row
            if health_benefits_matrix.at[row, col] == 1:  # Access element by row and column
                health_benefits_matrix.at[row, col] = dance_names[row]  # Replace 1 with the dance name

    st.title("Dance and Health Benefits")
    st.write("This table shows different dances and the associated health benefits:")

    #st.write(pd.DataFrame([health_benefits_matrix['Improved_cardiovascular_health']]))

    # Drop columns where all values are 0
    health_benefits_matrix = health_benefits_matrix.loc[:, (health_benefits_matrix != 0).any(axis=0)]

    # Display the DataFrame without the columns that had all 0 values
    st.write(health_benefits_matrix['Improved_cardiovascular_health'])

    st.subheader("Let's look into **Stress Relief**")
    st.write("Loading...")

    st.subheader("Let's tackle **Flexibility**")
    st.write("Loading...")

if pages == "FAQ's":
    st.subheader("**Frequently Asked Questions**")
    st.image('hangintherebaby.jpg')
    st.write("This page is currently under construction!")
    st.write("Sorry for the inconvience :(")

if pages == 'Data Science Work':
    st.header("Data Science Work")
    #IDA, EDA, cleaning, encoding, imputing, modeling, etc.
    tab1, tab2, tab3, tab4 = st.tabs(["Dance", "Health Benefits", "Calories", "Cardiovascular"])
    with tab1:
        st.header("Dance Styles and Genres")

        df = pd.read_csv('/Users/kendallandrews/Downloads/dances/dance data.csv', encoding='latin-1')
        st.write("Dance Styles and Genres Dataset")
        st.dataframe(df)

        st.subheader("IDA")

    #Filter data
        #filter = st.selectbox("Dance Type", df["Dance style"].unique())
        #filtered = df[df["Dance style"]  == filter]
        #st.write(filtered)

        st.write("Missing Values")
        code = '''
    for i in df.isnull().sum():
    if i > 0:
        print(df.isnull().sum())
    else:
        pass
        '''
        st.code(code, language="python")

    #Duplicates - Show code breakdown
        st.write("Duplicates")
        code='''
    duplicate_rows = df.duplicated()

# print duplicate rows
for i in duplicate_rows:
    if i == True:
        print(duplicate_rows)
    else:
        pass
    '''
        st.code(code, language="python")    

    #Correct data types
        st.write("Data Types")
        st.write("The data types was mostly categorical and the main variables I worked with which were numerical or later turned numerical was **Hardness Ratio, Tempo (BPM), Learning Difficulty, Health Benefits, Age Group**")
    
        st.write("This is an example of how I changes the health benefits variable from catergorical - textual to categorical - ordinal")
        code='''
    df["Health Benefits"]
df["health_count"] = df["Health Benefits"].str.split(",").apply(len)
print(df[["Health Benefits", "health_count"]])
    '''
        st.code(code, language="python") 

    #Encoding 
        st.write("Encoding")
        code='''
    from sklearn.preprocessing import OrdinalEncoder
#LabelEncoder, OneHotEncode
oe = OrdinalEncoder(categories=[[ 'Very easy','Easy', 'Moderate', 'Hard', 'Difficult']])
df['difficulty'] = oe.fit_transform(df[['Learning Difficulty']])
print(df[['Learning Difficulty', 'difficulty']])

#ages - object (all ages, teens and young adults, Adults, children and adults) - can change to numerical (CHECK)
#not sure if age is relevant yet
df["Age Group"]
# replace error in age column to the correct label
df['Age Group'].replace('574]: All ages]', 'All ages', inplace=True)
#'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)'
oe = OrdinalEncoder(categories=[['Children','Teens and young adults', 'Children and Adults', 'Teens and young adults, Adults','Adults', 'All ages']])
df['ages'] = oe.fit_transform(df[['Age Group']])
print(df[['Age Group', 'ages']])
    
    '''
        st.code(code, language="python")

        #Mean, Median, Mode
        st.write("Mean, Median, and Mode")
        code='''
    print("\nMEAN:\n",df[numeric_cols_df].mean())
    #MEDIAN
    print("\nMEDIAN:\n",df[numeric_cols_df].median())
    #MODE
    print("\nMODE:\n",df[numeric_cols_df].mode())
   
    '''
        st.code(code, language="python")

        #Range, Variance, Standard Deviation
        st.write("Range (Min and Max), Variance, Standard Deviation")
        code='''

        def range(column):
            m1 = df[column].max()
            m2 = df[column].min()
            range = m1-m2
            print("min:",m1)
            print("max:",m2)
            print("range:",range)

        print("\nHardness Ratio")
        range("Hardness Ratio")

        print("\nTempo (BPM)") 
        range("Tempo (BPM)")  

        print("\nHealth Count")
        range("health_count")

        print("\nDifficulty")
        range("difficulty")

        print("\nAges")
        range("ages")

        #VARIANCE
        print("\nVARIANCE: ", df[numeric_cols_df].var())

        #STANDARD DEVIATION
        print("\nSTANDARD DEVIATION: ", df[numeric_cols_df].std())  

    '''
        st.code(code, language="python")


    #Standarized the data
        st.write("Standarized the data")
        code='''
    #Standardize formats
numeric_cols_df = df.select_dtypes(include=[np.number]).columns
z1= df[numeric_cols_df].apply(zscore)
print(z1)
    '''
        
        st.code(code, language="python")


        #Quantify missing data
        st.write("Quantify missing data")
        code='''
        # plotly.figure_factory - module contains dedicated functions for creating very specific types of plots that were at the time of their creation difficult to create with graph objects and prior to the existence of Plotly Express.
    import plotly.figure_factory as ff

    # Correlation Heatmap (Interactive)
    selected_features = ['Hardness Ratio', 'Tempo (BPM)', 'health_count', 'difficulty', 'ages']  # Focus on these variables
    #.corr() - Compute pairwise correlation of columns, excluding NA/null values.
    #.values - used to return a new view object that contains a list of all the values associated with the keys in the dictionary.
    correlation_matrix = df[selected_features].corr().values
    #create_annotated_heatmap() - Function that creates annotated heatmaps 
    fig_heatmap = ff.create_annotated_heatmap(
        #z- z matrix to create heatmap.
        z=correlation_matrix,
        #x - x-axis
        x=selected_features,
        #y - y-axis
        y=selected_features,
        # colorscale - heatmap colorscale -> Viridis - Use the color scales in this package to make plots that are pretty, 
        #better represent your data, easier to read by those with colorblindness, and print well in gray scale.
        colorscale='Viridis'
    )
    fig_heatmap.update_layout(
        #heatmap title
        title="Correlation Heatmap of Dance Dataset (Interactive)",
        #heatmap x-axis title
        xaxis_title="Features",
        #heatmap y-axis title
        yaxis_title="Features"
    )
    #print visualization
    fig_heatmap.show()
        '''
        st.code(code, language="python")

        code='''
        plt.figure(figsize=(4,8))
        sns.heatmap(df.isna(), cmap="magma")
        plt.title("Heatmap of Missingness in Dance Dataset")
    '''
        st.code(code, language="python")

        st.write("Identify outliers")
        code ='''
    def outlier(column):
        z = np.abs(stats.zscore(df[column]))
        # Identify outliers as students with a z-score greater than 3
        threshold = 3
        outliers = df[z > threshold]
        # Print the outliers
        print("****************")
        print("Outliers for", column, ":", outliers)
        print("*****************")
    outlier('Hardness Ratio') #ceremonial dance (worship dance), disco soul dance (boogaloo and electric boogaloo, and fly), novelty and fad dances (swin), social dace (square dance), other(lyrical dance)
    outlier('Tempo (BPM)') #latin dance rhythm (samba - brazilian dance, pasodoble)
    outlier('health_count') #no outliers
    outlier('difficulty') #cceremonial dance (rejang dance)
    outlier('ages') #no outliers

    #Assess impact of outliers
    #Create a histogram

    plt.subplot(2,3,1)
    plt.hist('Hardness Ratio')
    plt.title("Hardness Outlier")

    plt.subplot(2,3,2)
    plt.hist('Tempo (BPM)')
    plt.title("Tempo Outlier")

    plt.subplot(2,3,3)
    plt.hist('difficulty')
    plt.title("Difficulty Outlier")
        '''
        st.code(code, language="python")

        st.divider()

        st.subheader("EDA")
        st.write("Univariate analysis - Histograms")

        code='''
        sns.countplot(x='health_count', data=df)
        plt.title("Health Count")

        sns.countplot(x='ages', data=df)
        plt.title("Ages")

        '''
        st.code(code, language="python")

        st.write("Univariate analysis - Box plots")
        code='''
    fig = plt.figure(figsize =(10, 7))

    # Creating plot
    plt.subplot(2,3,1)
    plt.boxplot(df['Hardness Ratio'])
    plt.title("Hardness")

    plt.subplot(2,3,2)
    plt.boxplot(df['Tempo (BPM)'])
    plt.title("Tempo")

    plt.subplot(2,3,3)
    plt.boxplot(df['difficulty'])
    plt.title("Difficulty")

    plt.subplot(2,3,4)
    plt.boxplot(df['health_count'])
    plt.title("Health Count")

    plt.subplot(2,3,5)
    plt.boxplot(df['ages'])
    plt.title("Ages")


    # show plot
    plt.show()

        '''
        st.code(code, language="python")

        st.write("Bar plots - Categorical variables")
        code = '''
    fig = plt.figure(figsize =(10, 7))

    # Hardness vs. Difficulty
    plt.subplot(2,3,1)
    plt.bar(df['Hardness Ratio'], df['difficulty'])
    plt.title('Hardness vs. Difficulty')
    plt.xlabel('Hardness')
    plt.ylabel('Difficulty')

    # Hardness vs. Health Count
    plt.subplot(2,3,2)
    plt.bar(df['Hardness Ratio'], df['health_count'])
    plt.title('Hardness vs. Health Count')
    plt.xlabel('Hardness')
    plt.ylabel('Health')

    # Difficulty vs. Health Count
    plt.subplot(2,3,3)
    plt.bar(df['difficulty'], df['health_count'])
    plt.title('Difficulty vs. Health Count')
    plt.xlabel('Difficulty')
    plt.ylabel('Health')

    plt.show()

    '''
        st.code(code, language="python")

        st.write("Interactive Bar Plots")
        code = '''
    #Interactive Bar Plot -  # Hardness vs. Difficulty
    import plotly.express as px
    fig = px.bar(df, x='Hardness Ratio', y='difficulty', title='Hardness vs. Difficulty')
    fig.show()

    import plotly.express as px
    fig = px.bar(df, x='Hardness Ratio', y='health_count', title='Hardness vs. Health Count')
    fig.show()

    import plotly.express as px
    fig = px.bar(df, x='difficulty', y='health_count', title='Difficulty vs. Health Count')
    fig.show()

    '''
        st.code(code, language="python")

        st.write("Bivariate analysis - Scatter plots")
        code='''
    import plotly.graph_objects as go
    #!pip install plotly

    # Put the data into a pandas df
    dataF = pd.DataFrame({'x': df['Hardness Ratio'],
                    'y': df['Tempo (BPM)']})

    #Create the figure (for the moment: a blank graph)
    fig = go.Figure()

    # Add the scatter trace
    fig.add_trace(go.Scatter( 
        x=dataF['x'], # Variable in the x-axis
        y=dataF['y'], # Variable in the y-axis
        mode='markers', # This explicitly states that we want our observations to be represented by points
        
        # Properties associated with points 
        marker=dict(
            size=12, # Size
            color='#cb1dd1', # Color
            opacity=0.8, # Point transparency 
            line=dict(width=1, color='black') # Properties of the edges
        ),
    ))

    # Customize the layout
    fig.update_layout(
        title='Interactive Scatter Plot of the Hardness vs. the Tempo of the Dances', # Title
        xaxis_title='Hardness', # x-axis name
        yaxis_title='Tempo', # y-axis name
        width=800,  # Set the width of the figure to 800 pixels
        height=600,  # Set the height of the figure to 600 pixels
    )
    '''
        st.code(code, language="python")

        st.write("Multivariate analysis - Pair plots")

        code='''
        sns.pairplot(df)
    '''
        st.code(code, language="python")

        st.write("Dimensionality assessment")
        code='''

    from sklearn.preprocessing import StandardScaler  # to standardize the features
    from sklearn.decomposition import PCA  # to apply PCA

    #Standardize the features
    #Create an object of StandardScaler which is present in sklearn.preprocessing
    scalar = StandardScaler() 
    scaled_data = pd.DataFrame(scalar.fit_transform(df[numeric_cols_df])) #scaling the data
    scaled_data

    #Check the Co-relation between features without PCA
    sns.heatmap(scaled_data.corr())

    #Applying PCA
    #Taking no. of Principal Components as 3
    pca = PCA(n_components = 3)
    pca.fit(scaled_data)
    data_pca = pca.transform(scaled_data)
    data_pca = pd.DataFrame(data_pca,columns=['PC1','PC2','PC3'])
    data_pca.head()

    #Checking Co-relation between features after PCA
    sns.heatmap(data_pca.corr())

    '''
        st.code(code, language='python')

        st.write("Pattern and trend identification")
        code='''
    from sklearn.model_selection import train_test_split
    from pandas.core.common import random_state
    from sklearn.linear_model import LinearRegression
    plt.title('Tempo Distribution Plot')
    sns.distplot(df['Tempo (BPM)'])
    #sns.distplot(df['health_count'])
    plt.show()

    plt.scatter(df['health_count'], df['Tempo (BPM)'], color = 'lightcoral')
    plt.title('Health Benefits vs Tempo')
    plt.xlabel('Health Count')
    plt.ylabel('Tempo')
    plt.box(False)
    plt.show()
    '''
        st.code(code, language='python')

        st.divider()

        st.subheader("Cleaning")
        code='''
    #identify missing values
    for i in df.isnull().sum():
        if i > 0:
            print(df.isnull().sum())
        else:
            pass
    #no missing values

    #identify duplicates
    duplicate_rows = df.duplicated()

    # print duplicate rows
    for i in duplicate_rows:
        if i == True:
            print(duplicate_rows)
        else:
            pass
    #no duplicates

    #Correct data types
    df.dtypes
    #hardness = float (0.5, 0.7, 1.0, 1.3, 1.5, 2.0) (CHECK)
    df["Hardness Ratio"]
    #tempo (bpm) = int (80,120,125,130,150,180) (CHECK)
    df["Tempo (BPM)"]
    #dance style - object (fella shake, tap dancing, stepping, jazz, moonwalk, ballet, dougie, hip hop dance, catdaddy, jerkin, popping, litefeet, house dance, locking, krumping, kpop, lyrical, pole dance, etc.)
    #keep as objects/strings - names of the dances (CHECK)
    df["Dance style"] 
    #health benefits - object (Improved cardiovascular health, Stress relief, improved physical health, Increased self-esteem, Improved social skills, Improved flexibility, etc.)
    #can count the number of benefits to make the column numerical (CHECK)
    df["Health Benefits"]
    df["health_count"] = df["Health Benefits"].str.split(",").apply(len)
    print(df[["Health Benefits", "health_count"]])

    #learning difficulty - object (easy, moderate, hard) - can change to numerical (CHECK)
    from sklearn.preprocessing import OrdinalEncoder
    #LabelEncoder, OneHotEncode
    oe = OrdinalEncoder(categories=[[ 'Very easy','Easy', 'Moderate', 'Hard', 'Difficult']])
    df['difficulty'] = oe.fit_transform(df[['Learning Difficulty']])
    print(df[['Learning Difficulty', 'difficulty']])

    #ages - object (all ages, teens and young adults, Adults, children and adults) - can change to numerical (CHECK)
    #not sure if age is relevant yet
    df["Age Group"]
    # replace error in age column to the correct label
    df['Age Group'].replace('574]: All ages]', 'All ages', inplace=True)
    #'df[col].method(value, inplace=True)', try using 'df.method(..., inplace=True)'
    oe = OrdinalEncoder(categories=[['Children','Teens and young adults', 'Children and Adults', 'Teens and young adults, Adults','Adults', 'All ages']])
    df['ages'] = oe.fit_transform(df[['Age Group']])
    print(df[['Age Group', 'ages']])

    #df.columns

    #'Dance Type', 'Dance style', 'Origin', 'Time Period',
        #'Cultural Significance', 'Notable Characteristics', 'Instrumental',
        # 'Hardness Ratio', 'Dance Formation', 'Costume', 'Tempo (BPM)',
        #'Famous Practitioners', 'Events and Festivals', 'Modern Adaptations',
        # 'Associated Music Genre', 'Learning Difficulty', 'Health Benefits',
        #'Age Group'

    #Standardize formats
    numeric_cols_df = df.select_dtypes(include=[np.number]).columns
    z1= df[numeric_cols_df].apply(zscore)
    print(z1)
    '''
        st.code(code, language='python')

        st.divider()

        st.subheader("Encoding")
        code='''
    #learning difficulty - object (easy, moderate, hard) - can change to numerical (CHECK)
    from sklearn.preprocessing import OrdinalEncoder
    #LabelEncoder, OneHotEncode
    oe = OrdinalEncoder(categories=[[ 'Very easy','Easy', 'Moderate', 'Hard', 'Difficult']])
    df['difficulty'] = oe.fit_transform(df[['Learning Difficulty']])
    print(df[['Learning Difficulty', 'difficulty']])

    #ages - object (all ages, teens and young adults, Adults, children and adults) - can change to numerical (CHECK)
    #not sure if age is relevant yet
    df["Age Group"]
    # replace error in age column to the correct label
    df['Age Group'].replace('574]: All ages]', 'All ages', inplace=True)
    #'df[col].method(value, inplace=True)', try using 'df.method()..., inplace=True)'
    oe = OrdinalEncoder(categories=[['Children','Teens and young adults', 'Children and Adults', 'Teens and young adults, Adults','Adults', 'All ages']])
    df['ages'] = oe.fit_transform(df[['Age Group']])
    print(df[['Age Group', 'ages']])
    '''
        st.code(code, language='python')

        st.divider()

        st.subheader("Imputing")
        st.write("N/A")

        st.divider()

        st.subheader("Modeling")
        st.write("Loading...")


    with tab2:
        st.header("Health Benefits")

        health_benefits_split = df['Health Benefits'].str.split(",")
        #dtype_before2 = type(health_benefits_split)
        my_list = health_benefits_split.tolist()
        #dtype_after = type(my_list)
        #print(my_list)

        #Create an empty list of each health benefit
        #If the health benefit is prevalent in that dance add a 1 to the list 'health benefit' if not add a 0

        Improved_cardiovascular_health = []
        for i in range(len(my_list)):
            if 'Improved cardiovascular health' in my_list[i]:
                Improved_cardiovascular_health.append(1)
            elif 'Improved cardiov' in my_list[i]:
                Improved_cardiovascular_health.append(1)
            elif 'Improved cardiovascular health and increased physical fitness' in my_list[i]:
                Improved_cardiovascular_health.append(1)
            elif 'Cardiovascular health' in my_list[i]:
                Improved_cardiovascular_health.append(1)
            elif 'Positive effects on cardiovascular health' in my_list[i]:
                Improved_cardiovascular_health.append(1)
            elif 'Moderate cardiovascular workout' in my_list[i]:
                Improved_cardiovascular_health.append(1)
            elif ' such as improved cardiovascular' in my_list[i]:
                Improved_cardiovascular_health.append(1)
            else:
                Improved_cardiovascular_health.append(0)
        print(Improved_cardiovascular_health)

        Improved_flexibility = []
        for i in range(len(my_list)):
            if " Improved flexibility" in my_list[i]:
                Improved_flexibility.append(1)
            elif " and Improved flexibility." in my_list[i]:
                Improved_flexibility.append(1)
            elif ' and Improved flexibility' in my_list[i]:
                Improved_flexibility.append(1)
            elif " and improved flexibility" in my_list[i]:
                Improved_flexibility.append(1)
            elif 'Improved flexibility and strength' in my_list[i]:
                Improved_flexibility.append(1)
            elif 'Improved strength and flexibility' in my_list[i]:
                Improved_flexibility.append(1)
            elif ' Flexibility' in my_list[i]:
                Improved_flexibility.append(1)
            else:
                Improved_flexibility.append(0)
        print(Improved_flexibility)

        Stress_relief = []
        for i in range(len(my_list)):
            if " Stress relief" in my_list[i]:
                Stress_relief.append(1)
            elif "Stress relief" in my_list[i]:
                Stress_relief.append(1)
            elif ' stress relief' in my_list[i]:
                Stress_relief.append(1)
            elif 'Reduces stress' in my_list[i]:
                Stress_relief.append(1)
            elif 'Stress relief and improved mood' in my_list[i]:
                Stress_relief.append(1)
            elif 'Reduces stress and anxiety'  in my_list[i]:
                Stress_relief.append(1)
            else:
                Stress_relief.append(0)
        print(Stress_relief)

        #added to cerebellum
        Improved_posture = []
        for i in range(len(my_list)):
            if " Improved posture" in my_list[i]:
                Improved_posture.append(1)
            elif "Improved posture" in my_list[i]:
                Improved_posture.append(1)
            else:
                Improved_posture.append(0)
        print(Improved_posture)

        Confidence = []
        for i in range(len(my_list)):
            if " and Increased self-confidence" in my_list[i]:
                Confidence.append(1)
            elif " Increased self-confidence" in my_list[i]:
                Confidence.append(1)
            elif "Increased self-confidence" in my_list[i]:
                Confidence.append(1)
            elif ' Improved self-confidence' in my_list[i]:
                Confidence.append(1)
            elif ' Increased self-esteem' in my_list[i]:
                Confidence.append(1)
            elif ' and Increased self-' in my_list[i]:
                Confidence.append(1)
            else:
                Confidence.append(0)
        print(Confidence)

        Physical_fitness = []
        for i in range(len(my_list)):
            if " and increased physical fitness" in my_list[i]:
                Physical_fitness.append(1)
            elif " Increased physical fitness" in my_list[i]:
                Physical_fitness.append(1)
            elif "Improved physical fitness" in my_list[i]:
                Physical_fitness.append(1)
            elif " Improved physical fitness" in my_list[i]:
                Physical_fitness.append(1)
            elif '  Increased physical activity' in my_list[i]:
                Physical_fitness.append(1)
            elif ' and Muscle' in my_list[i]:
                Physical_fitness.append(1)
            elif ' Enhanced physical fitness' in my_list[i]:
                Physical_fitness.append(1)
            elif ' Weight loss' in my_list[i]:
                Physical_fitness.append(1)
            elif ' Burning calories and losing' in my_list[i]:
                Physical_fitness.append(1)
            elif 'Potential physical or mental health benefits associated with performing the dance. This describes' in my_list[i]:
                Physical_fitness.append(1)
            elif 'Increased physical activity and exercise' in my_list[i]:
                Physical_fitness.append(1)
            else:
                Physical_fitness.append(0)
        print(Physical_fitness)

        Social_connection = []
        for i in range(len(my_list)):
            if " and Social connection" in my_list[i]:
                Social_connection.append(1)
            elif "Social connection" in my_list[i]:
                Social_connection.append(1)
            elif " Social connections" in my_list[i]:
                Social_connection.append(1)
            elif " and social connection" in my_list[i]:
                Social_connection.append(1)
            elif ' and Improved social skills' in my_list[i]:
                Social_connection.append(1)
            else:
                Social_connection.append(0)
        print(Social_connection)

        Mental_health = []
        for i in range(len(my_list)):
            if " and improves mental health" in my_list[i]:
                Mental_health.append(1)
            elif "Improves mental health" in my_list[i]:
                Mental_health.append(1)
            elif " Improves mental health" in my_list[i]:
                Mental_health.append(1)
            elif 'Reduces stress and improves mental health' in my_list[i]:
                Mental_health.append(1)
            elif 'Dancing can offer physical and mental health benefits' in my_list[i]:
                Mental_health.append(1)
            elif 'The Zapateado dance has the potential to offer numerous physical and mental health' in my_list[i]:
                Mental_health.append(1)
            elif 'Potential physical or mental health benefits associated with performing the dance. This describes' in my_list[i]:
                Mental_health.append(1)
            elif 'potential_physical_mental_health_benefits' in my_list[i]:
                Mental_health.append(1)
            else:
                Mental_health.append(0)
        print(Mental_health)

        Strength = []
        for i in range(len(my_list)):
            if "Improved flexibility and strength" in my_list[i]:
                Strength.append(1)
            elif "Improved strength and flexibility" in my_list[i]:
                Strength.append(1)
            else:
                Strength.append(0)
        print(Strength)

        Community = []
        for i in range(len(my_list)):
            if " A sense of community and belonging" in my_list[i]:
                Community.append(1)
            else:
                Community.append(0)
        print(Community)

        Boost = []
        for i in range(len(my_list)):
            if " Boost" in my_list[i]:
                Boost.append(1)
            elif "Boost" in my_list[i]:
                Boost.append(1)
            elif 'Stress relief and improved mood' in my_list[i]:
                Boost.append(1)
            elif ' Boosted mood'in my_list[i]:
                Boost.append(1)
            elif ' and Increased energy' in my_list[i]:
                Boost.append(1)
            elif ' Increased energy levels' in my_list[i]:
                Boost.append(1)
            elif '55]: Increased happiness and well-being'in my_list[i]:
                Boost.append(1)
            else:
                Boost.append(0)
        print(Boost)

        Cerebellum = []
        for i in range(len(my_list)):
            if " Improved balance" in my_list[i]:
                Cerebellum.append(1)
            elif "Improved balance" in my_list[i]:
                Cerebellum.append(1)
            elif ' and improved coordination' in my_list[i]:
                Cerebellum.append(1)
            elif ' Improved coordination' in my_list[i]:
                Cerebellum.append(1)
            elif ' Improved balance and coordination' in my_list[i]:
                Cerebellum.append(1)
            elif ' Improved cognitive function' in my_list[i]:
                Cerebellum.append(1)
            elif ' Improved posture' in my_list[i]:
                Cerebellum.append(1)
            elif ' Improved balance and' in my_list[i]:
                Cerebellum.append(1)
            elif ' Improved balance and coord' in my_list[i]:
                Cerebellum.append(1)
            elif ' Improved posture' in my_list[i]:
                Cerebellum.append(1)
            elif 'Improved posture' in my_list[i]:
                Cerebellum.append(1)
            else:
                Cerebellum.append(0)
        print(Cerebellum)

        #Create a matrix for each health benefit
        #health_benefits_matrix = pd.DataFrame([Improved_cardiovascular_health, Improved_flexibility, Stress_relief, confidence, physical_fitness,social_connection, mental_health, strength, community, boost, cerebellum])
        #print(type(health_benefits_matrix))
        health_benefits_matrix = pd.DataFrame({
            'Improved_cardiovascular_health': Improved_cardiovascular_health,
            'Improved_flexibility': Improved_flexibility,
            'Stress_relief': Stress_relief,
            'Confidence': Confidence,
            'Physical_fitness': Physical_fitness,
            'Social_connection': Social_connection,
            'Mental_health': Mental_health,
            'Strength': Strength,
            'Community': Community, 
            'Boost': Boost,
            'Cerebellum': Cerebellum
        })

        dance_names = df['Dance style'].tolist()  # Convert dance styles to a list

        # Iterate over the DataFrame by rows and columns to replace 1s
        for col in health_benefits_matrix.columns:  # Iterate over each column
            for row in range(len(health_benefits_matrix)):  # Iterate over each row
                if health_benefits_matrix.at[row, col] == 1:  # Access element by row and column
                    health_benefits_matrix.at[row, col] = dance_names[row]  # Replace 1 with the dance name


        st.write("Health Benefits Dataset")
        st.dataframe(health_benefits_matrix)

        st.subheader("IDA")
        code='''
        health_benefits_split = df['Health Benefits'].str.split(",")
        #dtype_before2 = type(health_benefits_split)
        my_list = health_benefits_split.tolist()
        #dtype_after = type(my_list)
        #print(my_list)

        #Create an empty list of each health benefit
        #If the health benefit is prevalent in that dance add a 1 to the list 'health benefit' if not add a 0

        Improved_cardiovascular_health = []
        for i in range(len(my_list)):
            if 'Improved cardiovascular health' in my_list[i]:
                Improved_cardiovascular_health.append(1)
            elif 'Improved cardiov' in my_list[i]:
                Improved_cardiovascular_health.append(1)
            elif 'Improved cardiovascular health and increased physical fitness' in my_list[i]:
                Improved_cardiovascular_health.append(1)
            elif 'Cardiovascular health' in my_list[i]:
                Improved_cardiovascular_health.append(1)
            elif 'Positive effects on cardiovascular health' in my_list[i]:
                Improved_cardiovascular_health.append(1)
            elif 'Moderate cardiovascular workout' in my_list[i]:
                Improved_cardiovascular_health.append(1)
            elif ' such as improved cardiovascular' in my_list[i]:
                Improved_cardiovascular_health.append(1)
            else:
                Improved_cardiovascular_health.append(0)
        print(Improved_cardiovascular_health)

        Improved_flexibility = []
        for i in range(len(my_list)):
            if " Improved flexibility" in my_list[i]:
                Improved_flexibility.append(1)
            elif " and Improved flexibility." in my_list[i]:
                Improved_flexibility.append(1)
            elif ' and Improved flexibility' in my_list[i]:
                Improved_flexibility.append(1)
            elif " and improved flexibility" in my_list[i]:
                Improved_flexibility.append(1)
            elif 'Improved flexibility and strength' in my_list[i]:
                Improved_flexibility.append(1)
            elif 'Improved strength and flexibility' in my_list[i]:
                Improved_flexibility.append(1)
            elif ' Flexibility' in my_list[i]:
                Improved_flexibility.append(1)
            else:
                Improved_flexibility.append(0)
        print(Improved_flexibility)

        Stress_relief = []
        for i in range(len(my_list)):
            if " Stress relief" in my_list[i]:
                Stress_relief.append(1)
            elif "Stress relief" in my_list[i]:
                Stress_relief.append(1)
            elif ' stress relief' in my_list[i]:
                Stress_relief.append(1)
            elif 'Reduces stress' in my_list[i]:
                Stress_relief.append(1)
            elif 'Stress relief and improved mood' in my_list[i]:
                Stress_relief.append(1)
            elif 'Reduces stress and anxiety'  in my_list[i]:
                Stress_relief.append(1)
            else:
                Stress_relief.append(0)
        print(Stress_relief)

        #added to cerebellum
        Improved_posture = []
        for i in range(len(my_list)):
            if " Improved posture" in my_list[i]:
                Improved_posture.append(1)
            elif "Improved posture" in my_list[i]:
                Improved_posture.append(1)
            else:
                Improved_posture.append(0)
        print(Improved_posture)

        Confidence = []
        for i in range(len(my_list)):
            if " and Increased self-confidence" in my_list[i]:
                Confidence.append(1)
            elif " Increased self-confidence" in my_list[i]:
                Confidence.append(1)
            elif "Increased self-confidence" in my_list[i]:
                Confidence.append(1)
            elif ' Improved self-confidence' in my_list[i]:
                Confidence.append(1)
            elif ' Increased self-esteem' in my_list[i]:
                Confidence.append(1)
            elif ' and Increased self-' in my_list[i]:
                Confidence.append(1)
            else:
                Confidence.append(0)
        print(Confidence)

        Physical_fitness = []
        for i in range(len(my_list)):
            if " and increased physical fitness" in my_list[i]:
                Physical_fitness.append(1)
            elif " Increased physical fitness" in my_list[i]:
                Physical_fitness.append(1)
            elif "Improved physical fitness" in my_list[i]:
                Physical_fitness.append(1)
            elif " Improved physical fitness" in my_list[i]:
                Physical_fitness.append(1)
            elif '  Increased physical activity' in my_list[i]:
                Physical_fitness.append(1)
            elif ' and Muscle' in my_list[i]:
                Physical_fitness.append(1)
            elif ' Enhanced physical fitness' in my_list[i]:
                Physical_fitness.append(1)
            elif ' Weight loss' in my_list[i]:
                Physical_fitness.append(1)
            elif ' Burning calories and losing' in my_list[i]:
                Physical_fitness.append(1)
            elif 'Potential physical or mental health benefits associated with performing the dance. This describes' in my_list[i]:
                Physical_fitness.append(1)
            elif 'Increased physical activity and exercise' in my_list[i]:
                Physical_fitness.append(1)
            else:
                Physical_fitness.append(0)
        print(Physical_fitness)

        Social_connection = []
        for i in range(len(my_list)):
            if " and Social connection" in my_list[i]:
                Social_connection.append(1)
            elif "Social connection" in my_list[i]:
                Social_connection.append(1)
            elif " Social connections" in my_list[i]:
                Social_connection.append(1)
            elif " and social connection" in my_list[i]:
                Social_connection.append(1)
            elif ' and Improved social skills' in my_list[i]:
                Social_connection.append(1)
            else:
                Social_connection.append(0)
        print(Social_connection)

        Mental_health = []
        for i in range(len(my_list)):
            if " and improves mental health" in my_list[i]:
                Mental_health.append(1)
            elif "Improves mental health" in my_list[i]:
                Mental_health.append(1)
            elif " Improves mental health" in my_list[i]:
                Mental_health.append(1)
            elif 'Reduces stress and improves mental health' in my_list[i]:
                Mental_health.append(1)
            elif 'Dancing can offer physical and mental health benefits' in my_list[i]:
                Mental_health.append(1)
            elif 'The Zapateado dance has the potential to offer numerous physical and mental health' in my_list[i]:
                Mental_health.append(1)
            elif 'Potential physical or mental health benefits associated with performing the dance. This describes' in my_list[i]:
                Mental_health.append(1)
            elif 'potential_physical_mental_health_benefits' in my_list[i]:
                Mental_health.append(1)
            else:
                Mental_health.append(0)
        print(Mental_health)

        Strength = []
        for i in range(len(my_list)):
            if "Improved flexibility and strength" in my_list[i]:
                Strength.append(1)
            elif "Improved strength and flexibility" in my_list[i]:
                Strength.append(1)
            else:
                Strength.append(0)
        print(Strength)

        Community = []
        for i in range(len(my_list)):
            if " A sense of community and belonging" in my_list[i]:
                Community.append(1)
            else:
                Community.append(0)
        print(Community)

        Boost = []
        for i in range(len(my_list)):
            if " Boost" in my_list[i]:
                Boost.append(1)
            elif "Boost" in my_list[i]:
                Boost.append(1)
            elif 'Stress relief and improved mood' in my_list[i]:
                Boost.append(1)
            elif ' Boosted mood'in my_list[i]:
                Boost.append(1)
            elif ' and Increased energy' in my_list[i]:
                Boost.append(1)
            elif ' Increased energy levels' in my_list[i]:
                Boost.append(1)
            elif '55]: Increased happiness and well-being'in my_list[i]:
                Boost.append(1)
            else:
                Boost.append(0)
        print(Boost)

        Cerebellum = []
        for i in range(len(my_list)):
            if " Improved balance" in my_list[i]:
                Cerebellum.append(1)
            elif "Improved balance" in my_list[i]:
                Cerebellum.append(1)
            elif ' and improved coordination' in my_list[i]:
                Cerebellum.append(1)
            elif ' Improved coordination' in my_list[i]:
                Cerebellum.append(1)
            elif ' Improved balance and coordination' in my_list[i]:
                Cerebellum.append(1)
            elif ' Improved cognitive function' in my_list[i]:
                Cerebellum.append(1)
            elif ' Improved posture' in my_list[i]:
                Cerebellum.append(1)
            elif ' Improved balance and' in my_list[i]:
                Cerebellum.append(1)
            elif ' Improved balance and coord' in my_list[i]:
                Cerebellum.append(1)
            elif ' Improved posture' in my_list[i]:
                Cerebellum.append(1)
            elif 'Improved posture' in my_list[i]:
                Cerebellum.append(1)
            else:
                Cerebellum.append(0)
        print(Cerebellum)

        #Create a matrix for each health benefit
        #health_benefits_matrix = pd.DataFrame([Improved_cardiovascular_health, Improved_flexibility, Stress_relief, confidence, physical_fitness,social_connection, mental_health, strength, community, boost, cerebellum])
        #print(type(health_benefits_matrix))
        health_benefits_matrix = pd.DataFrame({
            'Improved_cardiovascular_health': Improved_cardiovascular_health,
            'Improved_flexibility': Improved_flexibility,
            'Stress_relief': Stress_relief,
            'Confidence': Confidence,
            'Physical_fitness': Physical_fitness,
            'Social_connection': Social_connection,
            'Mental_health': Mental_health,
            'Strength': Strength,
            'Community': Community, 
            'Boost': Boost,
            'Cerebellum': Cerebellum
        })
'''
        st.code(code, language="python")

        st.divider()

        st.subheader("EDA")
        st.write("Heatmap")

        code='''
        plt.figure(figsize=(10, 8))
sns.heatmap(health_benefits_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap for Health Benefits Matrix')
'''
        st.code(code, language="python")

        st.divider()

        st.subheader("Cleaning")
        st.write("See IDA Section")
        st.divider()

        st.header("Encoding")
        st.write("N/A")
        st.divider()

        st.subheader("Imputing")
        st.write("N/A")
        st.divider()

        st.subheader("Modeling")
        st.write("Heatmap")
        code='''
        plt.figure(figsize=(10, 8))
sns.heatmap(health_benefits_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap for Health Benefits Matrix')
'''
        st.code(code, language="python")


    with tab3:
        st.header("Calories")

        df2 = pd.read_csv("/Users/kendallandrews/Downloads/calories-burned-during-exercise-and-activities/exercise_dataset.csv")
    
        st.write("Calories Dataset")
        st.dataframe(df2)

        #Edited Calories Dataset
        d3 = df2.drop(['130 lb', '155 lb', '180 lb', '205 lb'], axis=1)
        d3 = d3.iloc[[29, 34, 35, 36],:]
        st.write("Final Calories Dataset")
        st.dataframe(d3)

        st.subheader("IDA")

    #Handle missing values - Remove duplicates - Correct data types - Standardize formats
    #Missing Values - show code breakdown
        st.write("Missing Values")
        code = '''
   
        #identify missing values
        for i in df2.isnull().sum():
            if i > 0:
                print(df2.isnull().sum())
            else:
                pass
        #no missing values

        '''
        st.code(code, language="python")

    #Duplicates - Show code breakdown
        st.write("Duplicates")
        code='''
        #identify duplicates
        duplicate_rows2 = df2.duplicated()

        # print duplicate rows
        for i in duplicate_rows2:
            if i == True:
                print(duplicate_rows2)
            else:
                pass
        #no duplicates      
        '''
        st.code(code, language="python")    

    #Correct data types
        st.write("Data Types")
        st.write("The data types did not need to be corrected for they were all intergers with one float (numerical).")
    

    #Encoding 
        st.write("Encoding")
        st.write("No encoding was necessary.")

    #Mean Median Mode
        st.write("Mean, Median, and Mode")
        code='''
        #- Calculate mean, median, mode 
        print("\nMEAN:\n",df2[numeric_cols_df2].mean())
        #MEDIAN
        print("\nMEDIAN:\n",df2[numeric_cols_df2].median())
        #MODE
        print("\nMODE:\n",df2[numeric_cols_df2].mode()) 
   
        '''
        st.code(code, language="python")

        st.write("Range (Min and Max), Variance, Standard Deviation")
        code='''

        def range(column):
            m1 = df2[column].max()
            m2 = df2[column].min()
            range = m1-m2
            print("min:",m1)
            print("max:",m2)
            print("range:",range)

        print("\n130 lb")
        range("130 lb")

        print("\n155 lb")
        range("155 lb")

        print("\n180 lb")
        range("180 lb")

        print("\n205 lb")
        range("205 lb")

        print("\nCalories (kg)") 
        range("Calories per kg")  

        #VARIANCE
        print("\nVARIANCE: ", df2[numeric_cols_df2].var())

        #STANDARD DEVIATION
        print("\nSTANDARD DEVIATION: ", df2[numeric_cols_df2].std())
        '''
        
        st.code(code, language="python")

    #Standarized the data
        st.write("Standarized the data")
        code='''
        #Standardize formats
        numeric_cols_df2 = df2.select_dtypes(include=[np.number]).columns
        z2 = df2[numeric_cols_df2].apply(zscore)
        print(z2)
        '''
        st.code(code, language="python")

        st.write("Outlier detection")
        code='''
#IDA Step 7: Outlier detection - Identify potential outliers - Assess impact of outliers - Decide on treatment of outliers
#CALORIES
#['130 lb', '155 lb', '180 lb', '205 lb', 'Calories per kg']
#Identify potential outliers 

# Calculate the z-score 
def outlier(column):
    z = np.abs(stats.zscore(df2[column]))
    # Identify outliers as students with a z-score greater than 3
    threshold = 3
    outliers = df2[z > threshold]
    # Print the outliers
    print("****************")
    print("Outliers for", column, ":", outliers)
    print("*****************")
#outlier('130 lb') #running, cross country skiing
#outlier('155 lb') #running, cross country skiing
#outlier('180 lb') #running, cross country skiing
outlier('205 lb') #running, cross country skiing
outlier('Calories per kg') #running, cross country skiing
#all the variables have the same outliers...?

#Assess impact of outliers
#Create a histogram

plt.subplot(2,3,1)
plt.hist('130 lb')
plt.title("130 lb Outlier")

plt.subplot(2,3,2)
plt.hist('155 lb')
plt.title("155 lb Outlier")

plt.subplot(2,3,3)
plt.hist('180 lb')
plt.title("180 lb Outlier")

plt.subplot(2,3,4)
plt.hist('205 lb')
plt.title("205 lb Outlier")

plt.subplot(2,3,5)
plt.hist('Calories per kg')
plt.title("Calories  Outlier")
'''
        st.code(code, language="python")

        st.divider()

        st.subheader("EDA")
        st.write(" Univariate analysis - Histograms")
        code='''
fig = plt.figure(figsize =(10, 7))

# Creating plot
plt.subplot(2,3,1)
plt.boxplot(df2['130 lb'])
plt.title("130 lb")

plt.subplot(2,3,2)
plt.boxplot(df2['155 lb'])
plt.title("155 lb")

plt.subplot(2,3,3)
plt.boxplot(df2['180 lb'])
plt.title("180 lb")

plt.subplot(2,3,4)
plt.boxplot(df2['205 lb'])
plt.title("205 lb")

plt.subplot(2,3,5)
plt.boxplot(df2['Calories per kg'])
plt.title("Calories")

# show plot
plt.show()
'''
        st.code(code, language="python")

        st.write("Bivariate analysis - Scatter plots")
        code='''
import plotly.graph_objects as go
#!pip install plotly

# Put the data into a pandas df
dataF = pd.DataFrame({'x': d3["Activity, Exercise or Sport (1 hour)"],
                   'y': d3['Calories per kg']})

#Create the figure (for the moment: a blank graph)
fig = go.Figure()

# Add the scatter trace
fig.add_trace(go.Scatter( 
    x=dataF['x'], # Variable in the x-axis
    y=dataF['y'], # Variable in the y-axis
    mode='markers', # This explicitly states that we want our observations to be represented by points
    
    # Properties associated with points 
    marker=dict(
        size=12, # Size
        color='#cb1dd1', # Color
        opacity=0.8, # Point transparency 
        line=dict(width=1, color='black') # Properties of the edges
    ),
))

# Customize the layout
fig.update_layout(
    title='Interactive Scatter Plot of Activity vs. Calories Burned', # Title
    xaxis_title="Activity, Exercise or Sport (1 hour)", # x-axis name
    yaxis_title='Calories per kg', # y-axis name
    width=800,  # Set the width of the figure to 800 pixels
    height=600,  # Set the height of the figure to 600 pixels
)
#Perfect Positive Linear Regression Model
'''
        st.code(code, language="python")

        st.write("Cross Tabulations")
        code='''
# form crosstab with dropna=True (default)
pd.crosstab(d3['Activity, Exercise or Sport (1 hour)'], d3['Calories per kg'])

# form crosstab with dropna=False
pd.crosstab(d3['Activity, Exercise or Sport (1 hour)'], d3['Calories per kg'], dropna=False)
'''
        st.code(code, language="python")

        st.write("Pattern and trend identification")
        code='''
plt.scatter(d3['Activity, Exercise or Sport (1 hour)'], d3['Calories per kg'], color = 'lightcoral')
plt.title('Activity vs Calories')
plt.xlabel('Dance')
plt.ylabel('Calories')
plt.box(False)
plt.show()

'''
        st.code(code, language="python")

        st.divider()

        st.subheader("Cleaning")
        #Edited dataset code
        st.write("Edited Dataset Code")
        code='''
        #Creating a new dataset for calories that only includes the exercise and the calories, only for dance
        d3 = df2.drop(['130 lb', '155 lb', '180 lb', '205 lb'], axis=1)
        d3

        #Ballet, twist, jazz, tap",266,317,368,419,0.927494089552239
        #Ballroom dancing, slow",177,211,245,279,0.61742672238806
        #Ballroom dancing, fast",325,387,449,512,1.13262599402985

        print(df2["Activity, Exercise or Sport (1 hour)"][36])
        d3 = d3.iloc[[29, 34, 35, 36],:]
        print('*********')
        print(d3.columns)
        numeric_cols_d3 = d3.select_dtypes(include=[np.number]).columns
        print(d3['Activity, Exercise or Sport (1 hour)'][29])

'''
        st.code(code, language="python")

        st.divider()

        st.header("Encoding")
        st.write("N/A")
        st.divider()
        st.subheader("Imputing")
        st.write("N/A")
        st.divider()

        st.subheader("Modeling")
        code='''
        #Filter data
        filter2 = st.selectbox("Filter Activity", d3["Activity, Exercise or Sport (1 hour)"].unique())
        filtered2 = d3[d3["Activity, Exercise or Sport (1 hour)"]  == filter2]
        st.write(filtered2)
'''
        st.code(code, language="python")

    with tab4:
        st.header("Cardiovascular")
        df3 = pd.read_csv("/Users/kendallandrews/Downloads/CVD_cleaned.csv")
        st.write("Cardiovascular Dataset")
        st.dataframe(df3)

        st.subheader("IDA")

        st.write("Missing Values")
        code='''
        #IDA Step 2: Data cleaning and preprocessing - Handle missing values - Remove duplicates - Correct data types - Standardize formats
        #  Cardiovascular dataset
        import sklearn
        from sklearn.preprocessing import OrdinalEncoder, LabelEncoder, OneHotEncoder

        #identify missing values

        for i in df3.isnull().sum():
            if i > 0:
                print(df3.isnull().sum())
            else:
                pass

        # Check for missing values
        missing_values = df3.isnull()

        # Count missing values in each column
        missing_count = df3.isnull().sum()

        # Get the rows with missing values
        rows_with_missing = df3[df3.isnull().any(axis=1)]

        #print(missing_values)
        #print(missing_count)
        #print(rows_with_missing)
        #no missing values
        '''
        st.code(code, language="python")

        st.write("Duplicates")
        code='''
        #identify duplicates
        duplicate_rows3 = df3.duplicated()

        # print duplicate rows
        for i in duplicate_rows3:
            if i == True:
                #print(duplicate_rows3)
            #else:
                pass
        #no duplicates
        '''
        st.write("Correct Data Types")
        code='''
        le = LabelEncoder()
        #oe = OrdinalEncoder(categories=[['Poor','Fair','Good','Very Good','Excellent']])
        df3['General_Health']= le.fit_transform(df3['General_Health'])
        #Poor - 0 ', 'Fair - 1','Good- 2', 'Very Good - 3', 'Excellent - 4']) 

        # Fit and transform the data
        df3['Exercise'] = le.fit_transform(df3['Exercise'])
        #print(Exercise)
        #N - 0, Y - 1

        df3['Heart_Disease'] = le.fit_transform(df3['Heart_Disease'])
        #rint(heart_d)
        #N - 0, Y - 1

        df3['Depression']= le.fit_transform(df3['Depression'])
        #print(depression)
        #N - 0, Y - 1

        df3['Diabetes'] = le.fit_transform(df3['Diabetes'])
        #print(diabetes)
        #N - 0, Y - 1

        df3['Arthritis'] = le.fit_transform(df3['Arthritis'])
        #print(arth)
        #N - 0, Y - 1

        df3['Sex']= le.fit_transform(df3['Sex'])
        #print(sex)
        #F - 0, M - 1

        df3['Smoking_History'] = le.fit_transform(df3['Smoking_History'])
        #print(smoke)
        #N - 0, Y - 1

        oe = OrdinalEncoder(categories=[['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80+']])
        #print(df3['Age_Category'])
        #df3['General_Health']= le.fit_transform(df3['General_Health'])
        df3['Age_Category'] = le.fit_transform(df3['Age_Category'])

        #dropped new le columns because they are returning copies into the overall dataset instead of overwritting 
        #df3.drop(['Age_Category1'], axis=1, inplace=True)
        '''
        st.code(code, language="python")

        st.write("Standaraize formats")
        code='''
        #Standardize formats
        numeric_cols_df3 = df3.select_dtypes(include=[np.number]).columns
        z3 = df3[numeric_cols_df3].apply(zscore)
        print(z3)
        #print(df3[numeric_cols_df3].dtypes)
        '''
        st.code(code, language="python")

        st.write("Mean, Median, Mode")
        code='''
        # - Calculate mean, median, mode 
print("\nMEAN:\n",df3[numeric_cols_df3].mean())
#MEDIAN
print("\nMEDIAN:\n",df3[numeric_cols_df3].median())
#MODE
print("\nMODE:\n",df3[numeric_cols_df3].mode())
'''
        st.code(code, language="python")
        
        st.write("Range, Variance, and Standard deviation")
        code='''
# - Determine range, variance, standard deviation | - Identify minimum and maximum values 
#RANGE / MAX and MIN
def range(column):
    m1 = df3[column].max()
    m2 = df3[column].min()
    range = m1-m2
    print("min:",m1)
    print("max:",m2)
    print("range:",range)

for i in (df3[numeric_cols_df3]):
    print(i)
    range(i) 

#VARIANCE
print("\nVARIANCE: ", df3[numeric_cols_df3].var())

#STANDARD DEVIATION
print("\nSTANDARD DEVIATION: ", df3[numeric_cols_df3].std())
'''
        st.code(code, language="python")

        st.write("Quantify missing data")
        code='''
import plotly.figure_factory as ff

# Correlation Heatmap (Interactive)
#selected_features = ['General_Health', 'Exercise', 'Heart_Disease', 'Depression', 'Diabetes', 'Arth', 'Sex', 'Age', 'Height_(cm)', 'Weight_(kg)', 'BMI', 'Smoke', 'Alcohol_Consumption', 'Fruit_Consumption', 'Green_Vegetables_Consumption', 'FriedPotato_Consumption']  # Focus on these variables
selected_features1 = ['General_Health', 'Exercise', 'Heart_Disease', 'Height_(cm)', 'Weight_(kg)', 'BMI', 'Fruit_Consumption', 'Green_Vegetables_Consumption',]  # Focus on these variables
#.corr() - Compute pairwise correlation of columns, excluding NA/null values.
#.values - used to return a new view object that contains a list of all the values associated with the keys in the dictionary.
correlation_matrix = df3[selected_features1].corr().values
#create_annotated_heatmap() - Function that creates annotated heatmaps 
fig_heatmap = ff.create_annotated_heatmap(
    #z- z matrix to create heatmap.
    z=correlation_matrix,
    #x - x-axis
    x=selected_features1,
    #y - y-axis
    y=selected_features1,
    # colorscale - heatmap colorscale -> Viridis - Use the color scales in this package to make plots that are pretty, 
    #better represent your data, easier to read by those with colorblindness, and print well in gray scale.
    colorscale='Viridis'
)
fig_heatmap.update_layout(
    #heatmap title
    title="Correlation Heatmap of Cardiovascular Dataset (Interactive)",
    #heatmap x-axis title
    xaxis_title="Features",
    #heatmap y-axis title
    yaxis_title="Features",
    width=1500,  # Adjust width as needed
    height=1000  # Adjust height as needed
)
#print visualization
fig_heatmap.show()
'''
        st.code(code, language="python")

        code='''
plt.figure(figsize=(4,8))
# sns.heatmap(df.isna().transpose(), cmap="plasma")
# sns.heatmap(df.isna(), cmap="viridis")
sns.heatmap(df3.isna(), cmap="magma")
plt.title("Heatmap of Missingness in Cardiovascular Dataset")
'''
        st.code(code, language="python")

        st.write("Outlier detection")
        code='''
#IDA Step 7: Outlier detection - Identify potential outliers - Assess impact of outliers - Decide on treatment of outliers
#CARDIOV

from scipy import stats
import numpy as np
#Identify potential outliers 

# Calculate the z-score 
def outlier(column):
    z = np.abs(stats.zscore(df3[column].dropna()))

    # Identify outliers as students with a z-score greater than 3
    threshold = 3
    outliers = df3[z > threshold]

    # Identify the indices where the z-score is greater than the threshold
    outlier_indices = np.where(z > threshold)[0]

    # Count the number of outliers
    num_outliers = len(outlier_indices)

    # Print the outliers
    print("****************")
    print(f"Outliers for {column}: {num_outliers}")
    print("*****************")
#outlier('General_Health') #no outliers
#outlier('Exercise') #no outliers
#outlier('Heart_Disease') #ALOT - 24971
#outlier('Diabetes') #ALOT - 2646
#outlier('Height_(cm)') # 681
#outlier('Weight_(kg)') # 2978
#outlier('BMI')# 3960
#outlier('Fruit_Consumption')# 3118
#outlier('Green_Vegetables_Consumption') #11692


#Assess impact of outliers - visually inspect the data using plots like box plots to identify outliers, calculate statistical measures like z-scores to quantify their distance from the mean, and compare key statistics (like mean vs median) with and without outliers to understand their influence on the data distribution

#Visualization - Create a histogram

plt.figure(figsize=(15, 10))

# First subplot (2 rows, 3 columns, position 1)
plt.subplot(3, 3, 1)
plt.hist(df3['Heart_Disease'], color='skyblue')
plt.title("Heart Disease Outlier")

plt.subplot(3,3,2)
plt.hist(df3['Diabetes'], color='skyblue')
plt.title("Diabetes Outlier")

plt.subplot(3,3,3)
plt.hist(df3['Height_(cm)'], color='skyblue')
plt.title("Height Outlier")

plt.subplot(3,3,4)
plt.hist(df3['Weight_(kg)'], color='skyblue')
plt.title("Weight Outlier")

plt.subplot(3,3,5)
plt.hist(df3['BMI'], color='skyblue')
plt.title("BMI Outlier")

plt.subplot(3,3,6)
plt.hist(df3['Fruit_Consumption'], color='skyblue')
plt.title("Fruit Consumption Outlier")

plt.subplot(3,3,7)
plt.hist(df3['Green_Vegetables_Consumption'], color='skyblue')
plt.title("Green Vegetables Consumption Outlier")

#Calculate statistical measures like z-scores

def stats_m(column):
    # Calculate the z-scores for the column
    z_scores = np.abs(stats.zscore(df3[column].dropna()))

    # Calculate the overall mean of the z-scores
    z_mean = np.mean(z_scores)  # Mean of the z-scores

    # Calculate the mean of the original column
    column_mean = df3[column].mean()

    # Print the results
    print("****************")
    print(f"Stats for {column}:")
    print(f"Mean Z-score for the whole column: {z_mean:.2f}")
    print(f"Mean value of {column}: {column_mean:.2f}")
    print("*****************")

#stats_m('Heart_Disease') #.47 diff
#stats_m('Diabetes') #,40 diff
#stats_m('Height_(cm)') #big difference
#stats_m('Weight_(kg)') #big difference
#stats_m('BMI') #27.88 diff
#stats_m('Fruit_Consumption') #29.14 diff
#stats_m('Green_Vegetables_Consumption') #14.4 diff

#Mean and Median w/ outliers
def mean_median(column):
    m = df3[column].mean()
    med = df3[column].median()

    print(f"\n{column}: Mean w/ Outliers = {m}, Median w/ Outliers = {med}")

mean_median('Heart_Disease') #.08 diff
mean_median('Diabetes') #.3 diff
mean_median('Height_(cm)') #.7 diff
mean_median('Weight_(kg)') #2 diff
mean_median('BMI')# 1 diff
mean_median('Fruit_Consumption') #1 diff
mean_median('Green_Vegetables_Consumption') #3 diff

def mean_median_none(column):
    #drop outliers
    z = np.abs(stats.zscore(df3[column].dropna()))

    # Identify outliers as students with a z-score greater than 3
    threshold = 3
    outliers = df3[z > threshold]

    # Identify the indices where the z-score is greater than the threshold
    outlier_indices = np.where(z > threshold)[0]
    no_outliers = df3[column].drop(outlier_indices)
    m = no_outliers.mean()
    med = no_outliers.median()

    print(f"\n{column}: Mean w/o Outliers = {m}, Median w/o Outliers = {med}")

mean_median_none('Heart_Disease') #same
mean_median_none('Diabetes') #.2 diff
mean_median_none('Height_(cm)')# .6
mean_median_none('Weight_(kg)')#1
mean_median_none('BMI') #1
mean_median_none('Fruit_Consumption') #2
mean_median_none('Green_Vegetables_Consumption')# .9
       
'''
        st.code(code, language="python")

        st.divider()
        st.subheader("EDA")
        st.write("Histograms")
        code='''
plt.figure(figsize=(20, 15)) 
plt.subplot(2,2,1)
sns.countplot(x='General_Health', data=df3)
plt.title("General Health")

plt.subplot(2,2,2)
sns.countplot(x='Exercise', data=df3)
plt.title("Exercise")

plt.subplot(2,2,3)
sns.countplot(x='Heart_Disease', data=df3)
plt.title("Heart Disease")

plt.subplot(2,2,4)
sns.countplot(x='Diabetes', data=df3)
plt.title("Diabetes")
'''
        st.code(code, language="python")

        st.write("Box plots")
        code='''

#Box plots
fig = plt.figure(figsize =(12, 10))

# Creating plot
plt.subplot(3,3,1)
plt.boxplot(df3['General_Health'])
plt.title("General Health")

plt.subplot(3,3,2)
plt.boxplot(df3['Exercise'])
plt.title("Exercise")

plt.subplot(3,3,3)
plt.boxplot(df3['Heart_Disease'])
plt.title("Heart Disease")

plt.subplot(3,3,4)
plt.boxplot(df3['Diabetes'])
plt.title("Diabetes")

plt.subplot(3,3,5)
plt.boxplot(df3['Height_(cm)'])
plt.title("Height (cm)")

plt.subplot(3,3,6)
plt.boxplot(df3['Weight_(kg)'])
plt.title("Weight (kg)")

plt.subplot(3,3,7)
plt.boxplot(df3['BMI'])
plt.title("BMI")

plt.subplot(3,3,8)
plt.boxplot(df3['Fruit_Consumption'])
plt.title("Fruit Consumption")

plt.subplot(3,3,9)
plt.boxplot(df3['Green_Vegetables_Consumption'])
plt.title("Green Vegetables Consumption")
'''
        st.code(code, language="python")

        st.write("Interactive Scatterplots")
        code='''
import plotly.express as px

fig = px.scatter(df3, x='Height_(cm)', y='Weight_(kg)', color='General_Health')
#plt.title("Height vs. Weight Distribution Colored by General Health")
fig.update_layout(
    title="Relationship Between Height and Weight by General Health Status"
)
fig.show()

import plotly.express as px

fig = px.scatter(df3, x='Fruit_Consumption', y='Green_Vegetables_Consumption', color='General_Health')
#fig.title("Height vs. Weight Distribution Colored by General Health")
fig.update_layout(
    title="Relationship Between Fruit and Green Vegetables by General Health Status"
)
fig.show()
'''
        st.code(code, language="python")

        st.write("Cross tabulations")
        code='''
# form crosstab with dropna=False
pd.crosstab(df3['Fruit_Consumption'], df3['Green_Vegetables_Consumption'], dropna=False)
'''
        st.code(code, language="python")

        st.write("Multivariate analysis - Pair plots")
        code='''
#Pair Plots
sns.pairplot(df3)
'''
        st.code(code, language="python")

        st.divider()
        st.subheader("Cleaning")
        code='''
        #IDA Step 2: Data cleaning and preprocessing - Handle missing values - Remove duplicates - Correct data types - Standardize formats
#  Cardiovascular dataset
import sklearn
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder, OneHotEncoder

#identify missing values

for i in df3.isnull().sum():
    if i > 0:
        print(df3.isnull().sum())
    else:
        pass

# Check for missing values
missing_values = df3.isnull()

# Count missing values in each column
missing_count = df3.isnull().sum()

# Get the rows with missing values
rows_with_missing = df3[df3.isnull().any(axis=1)]

#print(missing_values)
#print(missing_count)
#print(rows_with_missing)
#no missing values

#identify duplicates
duplicate_rows3 = df3.duplicated()

# print duplicate rows
for i in duplicate_rows3:
    if i == True:
        #print(duplicate_rows3)
    #else:
        pass
#no duplicates

#Correct data types
#print(df3.dtypes)

#Cardio Dataset Datatypes

#General_Health                   object - poor, very good, good, fair (encoding) X
#Checkup                          object - within the pask 2 years, within the past year - (drop)
#Exercise                         object - No, Yes - encoding X
#Heart_Disease                    object - No, Yes - encoding X
#Skin_Cancer                      object - drop column 
#Other_Cancer                     object - drop column
#Depression                       object - No, Yes - encoding X
#Diabetes                         object - No, Yes - encoding
#Arthritis                        object - No, Yes - encoding X
#Sex                              object - F, M - encoding X
#Age_Category                     object - 70-74, 60-64, 75-79, 80+, 25-29... X
#Height_(cm)                     float64 - keep the same
#Weight_(kg)                     float64 - keep the same
#BMI                             float64 - keep the same
#Smoking_History                  object - No, Yes - encoding
#Alcohol_Consumption             float64 - 0.0, 4.0, 8.0 (keep same)
#Fruit_Consumption               float64 - keep the same
#Green_Vegetables_Consumption    float64 - keep the same
#FriedPotato_Consumption         float64 - keep the same (could drop)

le = LabelEncoder()
#oe = OrdinalEncoder(categories=[['Poor','Fair','Good','Very Good','Excellent']])
df3['General_Health']= le.fit_transform(df3['General_Health'])
#Poor - 0 ', 'Fair - 1','Good- 2', 'Very Good - 3', 'Excellent - 4']) 

# Fit and transform the data
df3['Exercise'] = le.fit_transform(df3['Exercise'])
#print(Exercise)
#N - 0, Y - 1

df3['Heart_Disease'] = le.fit_transform(df3['Heart_Disease'])
#rint(heart_d)
#N - 0, Y - 1

df3['Depression']= le.fit_transform(df3['Depression'])
#print(depression)
#N - 0, Y - 1

df3['Diabetes'] = le.fit_transform(df3['Diabetes'])
#print(diabetes)
#N - 0, Y - 1

df3['Arthritis'] = le.fit_transform(df3['Arthritis'])
#print(arth)
#N - 0, Y - 1

df3['Sex']= le.fit_transform(df3['Sex'])
#print(sex)
#F - 0, M - 1

df3['Smoking_History'] = le.fit_transform(df3['Smoking_History'])
#print(smoke)
#N - 0, Y - 1

oe = OrdinalEncoder(categories=[['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80+']])
#print(df3['Age_Category'])
#df3['General_Health']= le.fit_transform(df3['General_Health'])
df3['Age_Category'] = le.fit_transform(df3['Age_Category'])

#dropped new le columns because they are returning copies into the overall dataset instead of overwritting 
#df3.drop(['Age_Category1'], axis=1, inplace=True)

#Standardize formats
numeric_cols_df3 = df3.select_dtypes(include=[np.number]).columns
z3 = df3[numeric_cols_df3].apply(zscore)
print(z3)
#print(df3[numeric_cols_df3].dtypes)
'''
        st.code(code,language='python')
        st.divider()

        st.header("Encoding")
        code='''

        le = LabelEncoder()
        #oe = OrdinalEncoder(categories=[['Poor','Fair','Good','Very Good','Excellent']])
        df3['General_Health']= le.fit_transform(df3['General_Health'])
        #Poor - 0 ', 'Fair - 1','Good- 2', 'Very Good - 3', 'Excellent - 4']) 

        # Fit and transform the data
        df3['Exercise'] = le.fit_transform(df3['Exercise'])
        #print(Exercise)
        #N - 0, Y - 1

        df3['Heart_Disease'] = le.fit_transform(df3['Heart_Disease'])
        #rint(heart_d)
        #N - 0, Y - 1

        df3['Depression']= le.fit_transform(df3['Depression'])
        #print(depression)
        #N - 0, Y - 1

        df3['Diabetes'] = le.fit_transform(df3['Diabetes'])
        #print(diabetes)
        #N - 0, Y - 1

        df3['Arthritis'] = le.fit_transform(df3['Arthritis'])
        #print(arth)
        #N - 0, Y - 1

        df3['Sex']= le.fit_transform(df3['Sex'])
        #print(sex)
        #F - 0, M - 1

        df3['Smoking_History'] = le.fit_transform(df3['Smoking_History'])
        #print(smoke)
        #N - 0, Y - 1

        oe = OrdinalEncoder(categories=[['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80+']])
        #print(df3['Age_Category'])
        #df3['General_Health']= le.fit_transform(df3['General_Health'])
        df3['Age_Category'] = le.fit_transform(df3['Age_Category'])
'''
        st.code(code, language="python")
        st.divider()

        st.subheader("Imputing")
        st.write("N/A")

        st.divider()
        st.subheader("Modeling")
        code='''
corr_matrix = df3[numeric_cols_df3].corr()
plt.figure(figsize=(20, 16))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Fixed Calories Dataset')
'''
        st.code(code, language="python")
        st.write("PCA")
        code='''
from sklearn.preprocessing import StandardScaler  # to standardize the features
from sklearn.decomposition import PCA  # to apply PCA

#Standardize the features
#Create an object of StandardScaler which is present in sklearn.preprocessing
scalar = StandardScaler() 
scaled_data = pd.DataFrame(scalar.fit_transform(df3[numeric_cols_df3])) #scaling the data
scaled_data

#Check the Co-relation between features without PCA
sns.heatmap(scaled_data.corr())
pca = PCA(n_components = 3)
pca.fit(scaled_data)
data_pca = pca.transform(scaled_data)
data_pca = pd.DataFrame(data_pca,columns=['PC1','PC2','PC3'])
data_pca.head()

#Checking Co-relation between features after PCA
sns.heatmap(data_pca.corr())
'''
    st.code(code, language="python")

    st.write("Linear Regression (Interactive)")
    code='''
#Linear Regression Code:
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def linear_regression(feature1,feature2):
    # Feature matrix (X) and target variable (y)
    X = df3[[feature1]]  # Predictor (independent variable)
    y = df3[[feature2]]    # Target (dependent variable)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the linear regression model
    model = LinearRegression()

    # Fit the model to the training data
    model.fit(X_train, y_train)

    #Make predictions on the testing data
    y_pred = model.predict(X_test)

    # Model evaluation
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    # Print coefficients and evaluation metrics
    print(f"Intercept: {model.intercept_}")
    print(f"Coefficient: {model.coef_[0]}")
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R-squared: {r2:.2f}")

        # Create an interactive scatter plot with Plotly
    fig = go.Figure()

    # Add actual data points
    fig.add_trace(go.Scatter(
        x=X_test[feature1].values.flatten(),
        y=y_test[feature2].values.flatten(),
        mode='markers',
        name='Actual',
        marker=dict(color='blue')
    ))

    # Add regression line
    fig.add_trace(go.Scatter(
        x=X_test[feature1].values.flatten(),
        y=y_pred.flatten(),
        mode='lines',
        name='Predicted',
        line=dict(color='red', width=2)
    ))

    # Set plot title and labels
    fig.update_layout(
        title=f"Interactive Linear Regression: {feature1} vs. {feature2}",
        xaxis_title=feature1,
        yaxis_title=feature2,
        legend=dict(x=0, y=1)
    )

    # Show the interactive plot
    fig.show()
    
#High Correlations
plt.figure(figsize=(30, 20))
linear_regression('Weight_(kg)','BMI')
'''
    st.code(code, language="python")

    st.write("Linear Regression Plots")
    code='''
#Low Correlations
plt.figure(figsize=(30, 20))
linear_regression('Weight_(kg)','Sex')
#F - 0, M - 1

#Really Low Correlations
plt.figure(figsize=(30, 20))
linear_regression('Exercise','General_Health')

#Correlations dealing with Heart Disease (really low)
plt.figure(figsize=(30, 20))
plt.subplot(3,3,1)
linear_regression('Heart_Disease','Depression')

plt.figure(figsize=(30, 20))
plt.subplot(3,3,2)
linear_regression('Heart_Disease','Diabetes')

plt.figure(figsize=(30, 20))
plt.subplot(3,3,3)
linear_regression('Heart_Disease','Arthritis')

plt.figure(figsize=(30, 20))
plt.subplot(3,3,4)
linear_regression('Heart_Disease','Sex')

plt.figure(figsize=(30, 20))
plt.subplot(3,3,5)
linear_regression('Heart_Disease','Age_Category')

plt.figure(figsize=(30, 20))
plt.subplot(3,3,3)
linear_regression('Heart_Disease','Height_(cm)')

plt.figure(figsize=(30, 20))
plt.subplot(3,3,7)
linear_regression('Heart_Disease','Weight_(kg)')

plt.figure(figsize=(30, 20))
plt.subplot(3,3,8)
linear_regression('Heart_Disease','BMI')

plt.figure(figsize=(30, 20))
plt.subplot(3,3,9)
linear_regression('Heart_Disease','Smoking_History')

'''
    st.code(code, language="python")

    st.write("Time Series Analysis")
    st.write("Loading...")

        

#Notes:
#Historical data analysis with trends and patterns

#Health Improvement Forecasts: Show how continuing a specific dance routine can improve cardiovascular health or stamina.
#Example Insight:
#Based on your recent sessions, dancing for 20 more minutes per week could improve your cardiovascular endurance by 10%.”
 #Comparison of dance type over times for efficacy


#streamlit run /Users/kendallandrews/Downloads/dance_health.py
