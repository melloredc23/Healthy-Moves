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

#please run
#Datasets
#df = pd.read_csv('/Users/kendallandrews/Downloads/dances/dance data.csv', encoding='latin-1')
#df2 = pd.read_csv("/Users/kendallandrews/Downloads/calories-burned-during-exercise-and-activities/exercise_dataset.csv")
df = pd.read_csv('dance data.csv', encoding='latin-1')
df2 = pd.read_csv("exercise_dataset.csv")
d3 = df2.drop(['130 lb', '155 lb', '180 lb', '205 lb'], axis=1)
d3 = d3.iloc[[29, 34, 35, 36],:]
df3 = pd.read_csv("CVD_cleaned.csv")

#Tabs -> Sidebar
pages = st.sidebar.radio("Pages:", ['Home Page', 'Profile', 'Library', "Dance Recommendation System", 'Data Science Work'])
# -> DS Sections - ['IDA', 'Data EDA', 'Cleaning', 'Encoding', 'Imputing', 'Modeling'])


if pages == 'Home Page':
    st.title("**Welcome to Healthy Moves**")
    st.subheader("Your Personalized Dance Fitness Companion 🕺💃")
    # Rhythm and Burn, Healthy Moves, Healthy Steps, Rhythm Revive Repeat, 
    st.header("Let's Start Your Dance Journey!")
    st.image('groupdance.jpg')
    st.subheader("**Introduction**")
    st.markdown(''' Are you ready to transform your fitness journey with the rhythm of dance?  
                This app is designed to help you discover the health benefits of various dance routines and build personalized playlists tailored to your fitness goals and preferences.  
                Whether you're looking to boost cardiovascular health or simply have fun, this app combines data-driven insights with the joy of movement.''')
    
    st.subheader("**Why Choose Dance for Fitness?**")
    st.markdown('''
        Dance is more than just an art form—it's a powerful way to enhance physical and mental well-being. Research shows that dance can:
        - Improve cardiovascular health by keeping your heart pumping.
        - Burn calories effectively while providing a full-body workout.
        - Boost stamina and endurance through consistent movement.
        - Enhance flexibility and coordination, reducing injury risk.
        - Elevate mood and relieve stress, promoting mental health.
                ''')
    
    st.subheader("Let the dance guide you and the data inspire you! 🎶💃✨")
    
    # Create three columns for centering
    l, m, r = st.columns([1, 2, 1])  # Adjust the ratio to change centering effect
    # Place the button in the middle column
    with m:
        start = st.button("Let's Begin", type="primary")
    if start:
        st.write("Start by creating your profile by clicking the arrow in the upper left hand corner")

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

    st.subheader(f"Welcome {name_input}👋!")
    st.subheader("Lets practice some dancing to improve your health✅!!!")

if pages == 'Library':
    st.title("**Library📖**")
    st.subheader("Collection of Dances")

    #Filter data
    filter = st.selectbox("Dance Type", df["Dance style"].unique())
    filtered = df[df["Dance style"]  == filter]
    st.write(filtered)

    st.subheader("Collection of Health Benefits")

    #DFR CODE
    benefit_keywords = {
    'Improved cardiovascular health': [
        'Improved cardiovascular health', 'Improved cardiov', 'Improved cardiovascular health and increased physical fitness',
        'Cardiovascular health', 'Positive effects on cardiovascular health', 'Moderate cardiovascular workout',
        ' such as improved cardiovascular'
    ],
    'Improved flexibility': [
        'Improved flexibility', 'Flexibility', 'Improved strength and flexibility', 'Improved flexibility and strength',
        ' and Improved flexibility.', ' and Improved flexibility', ' and improved flexibility'
    ],
    'Stress relief': [
        'Stress relief', 'Reduces stress', 'Reduces stress and anxiety', 'Stress relief and improved mood',
        ' Stress relief', ' stress relief'
    ],
    'Confidence': [
        'Increased self-confidence', ' Improved self-confidence', ' Increased self-esteem',
        ' and Increased self-confidence', ' Increased self-confidence', ' and Increased self-'
    ],
    'Physical fitness': [
        'Increased physical fitness', 'Improved physical fitness', 'Burning calories and losing', 
        ' and increased physical fitness', ' Improved physical fitness', 'Increased physical activity and exercise',
        'Enhanced physical fitness', 'Weight loss'
    ],
    'Social connection': [
        'Social connection', ' and Improved social skills', ' and Social connection', ' Social connections',
        ' and social connection'
    ],
    'Mental health': [
        'Improves mental health', 'Reduces stress and improves mental health',
        'Potential physical or mental health benefits associated with performing the dance', 
        'Dancing can offer physical and mental health benefits'
    ],
    'Strength': [
        'Improved strength and flexibility', 'Improved flexibility and strength', ' and Muscle'
    ],
    'Community': [
        'A sense of community and belonging'
    ],
    'Boost': [
        'Boost', ' Boosted mood', ' Increased energy levels', ' Boost', 'Stress relief and improved mood',
        ' and Increased energy', '55]: Increased happiness and well-being'
    ],
    'Cerebellum': [
        'Improved balance', ' Improved coordination', ' Improved posture', 
        ' Improved balance and coordination', ' Improved cognitive function'
    ]
}

    # Function to determine the overall health benefit
    def extract_overall_benefit(benefits):
        for benefit_name, keywords in benefit_keywords.items():
            if any(keyword in benefits for keyword in keywords):
                return benefit_name  # Return the first matching benefit category
        return 'None'  # Default if no benefits match

    # Replace the Health Benefits column with overall health benefit
    df['Health Benefits'] = df['Health Benefits'].apply(lambda x: extract_overall_benefit(x))

    dfr=df

    #Filter data
    filter2 = st.selectbox("Health Benefits", dfr["Health Benefits"].unique())
    filtered2 = dfr[dfr["Health Benefits"]  == filter2]
    st.write(filtered2)


if pages == "Dance Recommendation System":
    st.title("**Dance Recommendation System🕺💃**")
    #st.image('/Users/kendallandrews/Downloads/hangintherebaby.jpg')

    #AI-driven recommendations based on user data (e.g., suggesting new dances)
    #Adaptive feedback on form and intensity
    #Custom playlists of dances tailored to user preferences

    #What You'll Get From The App:
    #Custom Dance Playlists: Select your preferred intensity, health goals, and calorie targets to build a dance routine just for you.
    #Health Insights: Explore data on how different dance styles impact your health, from calorie burn to cardiovascular benefits.
    #Interactive Tools: Adjust filters and preferences to see real-time updates to your personalized dance recommendations.


    st.subheader("Get Started")
    st.markdown('''Simply choose your preferences—intensity level, health focus, and more—and let us curate a dynamic playlist of dances that match your goals. 
                            It’s time to move, groove, and improve your health through the power of dance!
                ''')
    st.divider()

    intensity = st.multiselect("Select your preferred intensity:", ['Very easy','Easy', 'Moderate', 'Hard', 'Difficult'])
    #df['difficulty]
    health_focus = st.multiselect("Select the health benefits you want to focus on:", ['Improved cardiovascular health', 'Improved flexibility', 'Stress relief', 'Confidence', 'Physical fitness', 'Social connection', 'Strength', 'Mental Wellness', 'Community', 'Boost', 'Cerebellum'])
    #Cardio - cardiovascular, boost, physical fitness
    #Flexibility - flexibility, physical fitness, cerebellum
    #Strength - strength, physical fitness, cerebellum
    #Mental - mental, social, boost, stress, confidence
    music = st.multiselect("Select what music you prefer:", ["Hip Hop", "Pop", "Rock", "Country", "Electronic", "Latin", "R&B", "K-Pop", "Jazz", "Metal", "Classical", "Traditional", "World Music", "Disco", "Gospel", "Contemporary", "Ceremonial", "Carnatic music", "Japanese traditional music", "Middle Eastern", "Arabic", "Christian", "Soul", "Popcorn", "Hindustani classical music", "Reggae", "Bossa", "House Music", "Blues", "Swing", "Rock and roll", "Blues, Jazz, and Swing", "Bhangra", "Bollywood", "Calypso", "Flamenco Music", "Tribal"])

    #Time Series Incorporation
    time_of_day = st.selectbox("What time of day do you usually dance?", ["Morning (6 AM - 12 PM)", "Afternoon (12 PM - 6 PM)", "Evening (6 PM - 9PM)", "Night (9PM - 6 AM)"])

    #Merged Datasets Code:
    df = pd.read_csv('dance data.csv', encoding='latin-1')

    benefit_keywords = {
    'Improved cardiovascular health': [
        'Improved cardiovascular health', 'Improved cardiov', 'Improved cardiovascular health and increased physical fitness',
        'Cardiovascular health', 'Positive effects on cardiovascular health', 'Moderate cardiovascular workout',
        ' such as improved cardiovascular'
    ],
    'Improved flexibility': [
        'Improved flexibility', 'Flexibility', 'Improved strength and flexibility', 'Improved flexibility and strength',
        ' and Improved flexibility.', ' and Improved flexibility', ' and improved flexibility'
    ],
    'Stress relief': [
        'Stress relief', 'Reduces stress', 'Reduces stress and anxiety', 'Stress relief and improved mood',
        ' Stress relief', ' stress relief'
    ],
    'Confidence': [
        'Increased self-confidence', ' Improved self-confidence', ' Increased self-esteem',
        ' and Increased self-confidence', ' Increased self-confidence', ' and Increased self-'
    ],
    'Physical fitness': [
        'Increased physical fitness', 'Improved physical fitness', 'Burning calories and losing', 
        ' and increased physical fitness', ' Improved physical fitness', 'Increased physical activity and exercise',
        'Enhanced physical fitness', 'Weight loss'
    ],
    'Social connection': [
        'Social connection', ' and Improved social skills', ' and Social connection', ' Social connections',
        ' and social connection'
    ],
    'Mental health': [
        'Improves mental health', 'Reduces stress and improves mental health',
        'Potential physical or mental health benefits associated with performing the dance', 
        'Dancing can offer physical and mental health benefits'
    ],
    'Strength': [
        'Improved strength and flexibility', 'Improved flexibility and strength', ' and Muscle'
    ],
    'Community': [
        'A sense of community and belonging'
    ],
    'Boost': [
        'Boost', ' Boosted mood', ' Increased energy levels', ' Boost', 'Stress relief and improved mood',
        ' and Increased energy', '55]: Increased happiness and well-being'
    ],
    'Cerebellum': [
        'Improved balance', ' Improved coordination', ' Improved posture', 
        ' Improved balance and coordination', ' Improved cognitive function'
    ]
}

    # Function to determine the overall health benefit
    def extract_overall_benefit(benefits):
        for benefit_name, keywords in benefit_keywords.items():
            if any(keyword in benefits for keyword in keywords):
                return benefit_name  # Return the first matching benefit category
        return 'None'  # Default if no benefits match

    # Replace the Health Benefits column with overall health benefit
    df['Health Benefits'] = df['Health Benefits'].apply(lambda x: extract_overall_benefit(x))

    dfr=df
    #print(dfr.columns)

    # Add a simulated 'Timestamp' column for testing
    import random
    from datetime import datetime, timedelta
    # Generate random timestamps for the past 30 days
    dfr['Timestamp'] = [datetime.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23)) for _ in range(len(dfr))]


    # Add a 'Time of Day' column to the dataset (simulated)
    # Assuming this column exists in your dataset or can be derived from a timestamp
    dfr['Time of Day'] = dfr['Timestamp'].apply(lambda x: "Morning" if 6 <= pd.to_datetime(x).hour < 12 else
                                          "Afternoon" if 12 <= pd.to_datetime(x).hour < 18 else
                                          "Evening" if 18 <= pd.to_datetime(x).hour < 21 else
                                          "Night")
    
    # Function to recommend dances based on user input
    def recommend_dances(df, intensity, health_focus, music, time_of_day):
        # Filter by intensity
        if intensity:
            filtered_dances = df[df['Learning Difficulty'].isin(intensity)]
        else:
            filtered_dances = df  # No filtering if intensity is empty

        # Filter by health focus
        if health_focus:
            filtered_dances = filtered_dances[
                filtered_dances['Health Benefits'].apply(
                    lambda x: any(benefit in x for benefit in health_focus)
                )
            ]

        # Filter by music 
        if music:
            filtered_dances = filtered_dances[
                filtered_dances['Associated Music Genre'].apply(
                    lambda x: any(genre in x for genre in music)
                )
            ]

        # Filter by time of day
        if time_of_day:
            time_of_day_label = time_of_day.split(' ')[0]  # Extract 'Morning', 'Afternoon'...
            filtered_dances = filtered_dances[filtered_dances['Time of Day'] == time_of_day_label]

        return filtered_dances


    # Get recommendations
    recommended_dances = recommend_dances(dfr, intensity, health_focus, music, time_of_day)

    # Display results
    if not recommended_dances.empty:
        st.write("Recommended Dances for You:")
        st.write(recommended_dances[['Dance Type', 'Dance style', 'Learning Difficulty', 'Health Benefits', 'Associated Music Genre', 'Origin', 'Time of Day']])
    else:
        st.write("No dances found matching your preferences.")

    if 'Improved cardiovascular health' in health_focus:
        st.markdown('''
                    Cardiovascular health refers to the overall well-being of your heart and blood vessels, and encompasses conditions like coronary artery disease, stroke, heart failure, and arrhythmias; "cardiovascular disease" refers to a group of disorders affecting the heart and blood vessels, often caused by risk factors like high blood pressure, high cholesterol, smoking, and diabetes, making it the leading cause of death globally.
                    In order to keep good cardiovascular health, you should keep a **heart-healthy diet**, **stay active**, **keep a health weight**, **Do not partake in smoking and drink alcohol in moderation**.")
                    ''')

    st.subheader("Summary")
    st.markdown('''
                The dance recommendation system tailors suggestions based on your preferences and fitness goals. 
                This system not only motivates users but also helps them achieve health goals in a fun and engaging way!
                ''')     


    #    It integrates data filtering, ranking, and potential machine learning models to provide meaningful, personalized playlists.

if pages == 'Data Science Work':
    st.title("Data Science Work")
    #IDA, EDA, cleaning, encoding, imputing, modeling, etc.
    tab1, tab2, tab3, tab4 = st.tabs(["Dance", "Health Benefits", "Calories", "Cardiovascular"])
    with tab1:
        st.header("Dance Styles and Genres")

        df = pd.read_csv('dance data.csv', encoding='latin-1')
        st.write("Dance Styles and Genres Dataset")
        st.dataframe(df)

        #Purpose:
        st.subheader("Overview")
        st.markdown(''' The purpose of the dataset is to give detailed information about various dance styles and genres from around the world, encompassing both traditional and modern forms. 
                 It includes features such as origin, cultural significance, notable characteristics, associated music genres, health benefits, and more. 
                    The dataset aims to serve as a comprehensive resource for understanding the diversity, cultural contexts, and characteristics of different dance types.''')
        st.subheader("Features:")
        st.markdown(
            """
            The following list won't indent no matter what I try:
            -  Dance Type: The specific name of the dance genre (Text)
            -  Dance Style: The style or form of the dance. This describes the overall approach or method of the dance (Text)
            -  Origin: The geographical origin of the dance. This indicates where the dance was first developed or became popular (Text)
            -  Time Period: The historical period when the dance originated. This provides context about the era in which the dance was created or became prominent (Text)
            -  Cultural Significance: The role and importance of the dance in its cultural context (Text)
            -  Notable Characteristics: Key features or attributes of the dance. This includes specific movements, formations, styles, or any unique aspects that define the dance (Text)
            -  Instrumental: The type of instruments commonly associated with the dance genre. This lists the musical instruments that typically accompany the dance (Text)
            -  Hardness Ratio: The difficulty level of the dance, represented as a float value. This quantifies how challenging the dance is to learn and perform. Examples include 0.5 (easy), 1.0 (moderate), and 2.0 (hard) (Float)
            -  Dance Formation: Describes the typical formation or arrangement of dancers. This indicates whether the dance is performed solo, in pairs, in a circle, or in another formation (Text)
            -  Costume: Details about the traditional or typical attire worn during the dance (Text)
            -  Tempo: The speed or pace of the dance in beats per minute (BPM). This indicates how fast or slow the dance is performed (Integer)
            -  Famous Practitioners: Notable dancers or choreographers associated with the dance genre. This lists individuals who are well-known for their contributions to the dance, such as  Michael Jackson and John Travolta (Text)
            -  Events and Festivals: Major events or festivals where the dance is prominently featured (Text)
            -  Modern Adaptations: Information about how the dance has evolved or been adapted in contemporary times (Text)
            -  Associated Music Genre: The genre of music that typically accompanies the dance. This indicates the type of music that is commonly played during the dance (Text)
            -  Learning Difficulty: A qualitative description of how difficult it is to learn the dance (Text)
            -  Health Benefits: Potential physical or mental health benefits associated with performing the dance. This describes the positive effects of dancing on health and well-being(Text)
            -  Age Group: The typical age group that performs the dance (Text)         
            """
            )

        #IDA
        st.subheader("IDA")

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
        st.write("The data types were mostly textual/categorical. The main variables I worked with I made them numerical which were **Hardness Ratio, Tempo (BPM), Learning Difficulty, Health Benefits, Age Group**") 
        st.write("I will show how I corrected these data types in the encoding section")

        #Mean, Median, Mode
        st.write("Mean, Median, and Mode")
        code='''
    #MEAN
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

        st.divider()

        st.subheader("EDA")

        df["health_count"] = df["Health Benefits"].str.split(",").apply(len)

        #learning difficulty - object (easy, moderate, hard) - can change to numerical (CHECK)
        from sklearn.preprocessing import OrdinalEncoder
        #LabelEncoder, OneHotEncode
        oe = OrdinalEncoder(categories=[[ 'Very easy','Easy', 'Moderate', 'Hard', 'Difficult']])
        df['difficulty'] = oe.fit_transform(df[['Learning Difficulty']])

        df['Age Group'].replace('574]: All ages]', 'All ages', inplace=True)

        oe = OrdinalEncoder(categories=[['Children','Teens and young adults', 'Children and Adults', 'Teens and young adults, Adults','Adults', 'All ages']])
        df['ages'] = oe.fit_transform(df[['Age Group']])

        #Quantify missing data
        st.subheader("Correlation Heatmap - Quantify missing data")
        # Correlation Heatmap (Interactive)
        # Calculate correlation matrix
        selected_features = ['Hardness Ratio', 'Tempo (BPM)', 'health_count', 'difficulty', 'ages']
        corr_matrix = df[selected_features].corr().values
        # Display the correlation matrix using a heatmap
        st.header('Correlation Matrix')
        fig, ax = plt.subplots()
        sns.heatmap(corr_matrix, annot=True, ax=ax, cmap='coolwarm')
        plt.title("Correlation Heatmap of Dance Dataset")
        plt.xlabel('Features')
        plt.ylabel('Features')
        st.pyplot(fig)

        #Missingness
        st.subheader("Missingness")
        fig, ax = plt.subplots()
        sns.heatmap(df.isna(), cmap="magma")
        plt.title("Heatmap of Missingness in Dance Dataset")
        st.pyplot(fig)

        st.subheader("Identify outliers")
        from scipy import stats
        def outlier(column):
            z = np.abs(stats.zscore(df[column]))
            threshold = 3
            outliers = df[z > threshold]
            st.write(f"### Outliers for {column}:")
            if not outliers.empty:
                st.dataframe(outliers)
            else:
                st.write("No outliers detected.")

        # Call the function for each column
        outlier('Hardness Ratio')
        outlier('Tempo (BPM)')
        outlier('health_count')
        outlier('difficulty')
        outlier('ages')

        # Plot histograms for visualizing outliers
        st.subheader("Histograms - Outliers")
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))

        axes[0].hist(df['Hardness Ratio'], bins=10, color='skyblue')
        axes[0].set_title("Hardness Ratio Outlier")

        axes[1].hist(df['Tempo (BPM)'], bins=10, color='red')
        axes[1].set_title("Tempo (BPM) Outlier")

        axes[2].hist(df['difficulty'], bins=10, color='green')
        axes[2].set_title("Difficulty Outlier")

        # Display the histograms in Streamlit
        st.pyplot(fig)

        st.subheader("Univariate analysis - Histograms ")
        st.write("## Health Count Distribution")
        plt.figure(figsize=(8, 5))
        sns.countplot(x='health_count', data=df)
        plt.title("Health Count")
        st.pyplot(plt.gcf())  # Display the current figure

        # Second Seaborn count plot: Ages
        st.write("## Ages Distribution")
        plt.figure(figsize=(8, 5))
        sns.countplot(x='ages', data=df)
        plt.title("Ages")
        st.pyplot(plt.gcf()) 

        st.subheader("Univariate analysis - Box plots")
        # Create the figure for the box plots
        fig = plt.figure(figsize=(10, 7))

        # Plot each feature in a subplot
        plt.subplot(2, 3, 1)
        plt.boxplot(df['Hardness Ratio'])
        plt.title("Hardness")

        plt.subplot(2, 3, 2)
        plt.boxplot(df['Tempo (BPM)'])
        plt.title("Tempo")

        plt.subplot(2, 3, 3)
        plt.boxplot(df['difficulty'])
        plt.title("Difficulty")

        plt.subplot(2, 3, 4)
        plt.boxplot(df['health_count'])
        plt.title("Health Count")

        plt.subplot(2, 3, 5)
        plt.boxplot(df['ages'])
        plt.title("Ages")
   
        st.subheader("Bar plots - Categorical variables")
        fig = plt.figure(figsize=(10, 7))

        # Hardness vs. Difficulty
        plt.subplot(2, 3, 1)
        plt.bar(df['Hardness Ratio'], df['difficulty'], color='skyblue')
        plt.title('Hardness vs. Difficulty')
        plt.xlabel('Hardness')
        plt.ylabel('Difficulty')

        # Hardness vs. Health Count
        plt.subplot(2, 3, 2)
        plt.bar(df['Hardness Ratio'], df['health_count'], color='orange')
        plt.title('Hardness vs. Health Count')
        plt.xlabel('Hardness')
        plt.ylabel('Health')

        # Difficulty vs. Health Count
        plt.subplot(2, 3, 3)
        plt.bar(df['difficulty'], df['health_count'], color='green')
        plt.title('Difficulty vs. Health Count')
        plt.xlabel('Difficulty')
        plt.ylabel('Health')

        # Display the plot in Streamlit
        st.pyplot(fig)
        
        st.subheader("Interactive Bar Plots")
        import plotly.express as px
        # Hardness vs. Difficulty
        fig1 = px.bar(df, x='Hardness Ratio', y='difficulty', title='Hardness vs. Difficulty')
        st.plotly_chart(fig1)

        # Hardness vs. Health Count
        fig2 = px.bar(df, x='Hardness Ratio', y='health_count', title='Hardness vs. Health Count')
        st.plotly_chart(fig2)

        # Difficulty vs. Health Count
        fig3 = px.bar(df, x='difficulty', y='health_count', title='Difficulty vs. Health Count')
        st.plotly_chart(fig3)

        st.subheader("Bivariate analysis - Scatter plots")
        # Create the figure
        fig = go.Figure()

        # Put the data into a new DataFrame
        dataF = pd.DataFrame({'x': df['Hardness Ratio'], 'y': df['Tempo (BPM)']})

        # Add the scatter trace
        fig.add_trace(go.Scatter(
            x=dataF['x'],  # Variable in the x-axis
            y=dataF['y'],  # Variable in the y-axis
            mode='markers',  # Points represented as markers
            marker=dict(
                size=12,  # Size of markers
                color='#cb1dd1',  # Marker color
                opacity=0.8,  # Transparency
                line=dict(width=1, color='black')  # Edge properties
            ),
        ))

        # Customize the layout
        fig.update_layout(
            title='Interactive Scatter Plot of Hardness vs. Tempo',  # Title
            xaxis_title='Hardness',  # x-axis label
            yaxis_title='Tempo (BPM)',  # y-axis label
            width=800,  # Figure width
            height=600  # Figure height
        )

        # Display the figure in Streamlit
        st.plotly_chart(fig)

        st.subheader("Multivariate analysis - Pair plots")
        pairplot_fig = sns.pairplot(df)
        st.pyplot(pairplot_fig.fig)

        st.divider()

        st.subheader("Cleaning")
        code='''
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

    #df.columns

    #'Dance Type', 'Dance style', 'Origin', 'Time Period',
        #'Cultural Significance', 'Notable Characteristics', 'Instrumental',
        # 'Hardness Ratio', 'Dance Formation', 'Costume', 'Tempo (BPM)',
        #'Famous Practitioners', 'Events and Festivals', 'Modern Adaptations',
        # 'Associated Music Genre', 'Learning Difficulty', 'Health Benefits',
        #'Age Group'
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

        st.subheader("Dimensionality assessment - PCA - Linear Algebra")

        from sklearn.preprocessing import StandardScaler
        from sklearn.decomposition import PCA

        # Identify numeric columns for scaling
        numeric_cols_df = df.select_dtypes(include='number').columns

        # Standardize the features
        st.subheader("Standardized Data")
        scaler = StandardScaler()
        scaled_data = pd.DataFrame(scaler.fit_transform(df[numeric_cols_df]), columns=numeric_cols_df)
        st.write(scaled_data)

        # Correlation heatmap without PCA
        st.subheader("Correlation Heatmap Without PCA")
        plt.figure(figsize=(8, 5))
        sns.heatmap(scaled_data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
        st.pyplot(plt.gcf())  # Show the heatmap

        # Applying PCA
        st.subheader("PCA Transformation")
        pca = PCA(n_components=3)
        data_pca = pca.fit_transform(scaled_data)
        data_pca = pd.DataFrame(data_pca, columns=['PC1', 'PC2', 'PC3'])
        st.write(data_pca.head())  # Show the first few rows

        # Correlation heatmap after PCA
        st.subheader("Correlation Heatmap After PCA")
        plt.figure(figsize=(8, 5))
        sns.heatmap(data_pca.corr(), annot=True, cmap='coolwarm', fmt='.2f')
        st.pyplot(plt.gcf())  # Show the heatmap


        st.subheader("Pattern and trend identification - Linear Regression")
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LinearRegression
        # Tempo Distribution Plot
        st.write("## Tempo Distribution Plot")
        plt.figure(figsize=(8, 5))
        sns.histplot(df['Tempo (BPM)'], kde=True, color='skyblue')  # Updated to histplot instead of distplot (distplot is deprecated)
        plt.title('Tempo Distribution Plot')
        st.pyplot(plt.gcf())  # Show the plot in Streamlit

        # Scatter Plot: Health Benefits vs Tempo
        st.write("## Health Benefits vs Tempo")
        plt.figure(figsize=(8, 5))
        plt.scatter(df['health_count'], df['Tempo (BPM)'], color='lightcoral')
        plt.title('Health Benefits vs Tempo')
        plt.xlabel('Health Count')
        plt.ylabel('Tempo (BPM)')
        plt.box(False)
        st.pyplot(plt.gcf())  # Show the scatter plot in Streamlit

        st.subheader("Time Series Analysis Code")
        code='''
    # Add a simulated 'Timestamp' column for testing
    import random
    from datetime import datetime, timedelta
    # Generate random timestamps for the past 30 days
    dfr['Timestamp'] = [datetime.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23)) for _ in range(len(dfr))]


    # Add a 'Time of Day' column to the dataset (simulated)
    # Assuming this column exists in your dataset or can be derived from a timestamp
    dfr['Time of Day'] = dfr['Timestamp'].apply(lambda x: "Morning" if 6 <= pd.to_datetime(x).hour < 12 else
                                          "Afternoon" if 12 <= pd.to_datetime(x).hour < 18 else
                                          "Evening" if 18 <= pd.to_datetime(x).hour < 21 else
                                          "Night")
    
    # Function to recommend dances based on user input
    def recommend_dances(df, intensity, health_focus, music, time_of_day):
        # Filter by intensity
        if intensity:
            filtered_dances = df[df['Learning Difficulty'].isin(intensity)]
        else:
            filtered_dances = df  # No filtering if intensity is empty

        # Filter by health focus
        if health_focus:
            filtered_dances = filtered_dances[
                filtered_dances['Health Benefits'].apply(
                    lambda x: any(benefit in x for benefit in health_focus)
                )
            ]

        # Filter by music 
        if music:
            filtered_dances = filtered_dances[
                filtered_dances['Associated Music Genre'].apply(
                    lambda x: any(genre in x for genre in music)
                )
            ]

        # Filter by time of day
        if time_of_day:
            time_of_day_label = time_of_day.split(' ')[0]  # Extract 'Morning', 'Afternoon'...
            filtered_dances = filtered_dances[filtered_dances['Time of Day'] == time_of_day_label]

        return filtered_dances


    # Get recommendations
    recommended_dances = recommend_dances(dfr, intensity, health_focus, music, time_of_day)

    # Display results
    if not recommended_dances.empty:
        st.write("Recommended Dances for You:")
        st.write(recommended_dances[['Dance Type', 'Dance style', 'Learning Difficulty', 'Health Benefits', 'Associated Music Genre', 'Origin', 'Time of Day']])
    else:
        st.write("No dances found matching your preferences.")
        '''
        st.code(code, language='python')

    with tab2:
        st.header("Health Benefits")

        health_benefits_split = df['Health Benefits'].str.split(",")
        my_list = health_benefits_split.tolist()

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
                if health_benefits_matrix.at[row, col] == 0:  # Access element by row and column
                    health_benefits_matrix.at[row, col] = "None"


        st.write("Health Benefits Dataset")
        st.dataframe(health_benefits_matrix)

        st.write("Merged Dataset with Dance Dataset")
        #Merged Datasets Code:
        df = pd.read_csv('dance data.csv', encoding='latin-1')

        benefit_keywords = {
        'Improved cardiovascular health': [
            'Improved cardiovascular health', 'Improved cardiov', 'Improved cardiovascular health and increased physical fitness',
            'Cardiovascular health', 'Positive effects on cardiovascular health', 'Moderate cardiovascular workout',
            ' such as improved cardiovascular'
        ],
        'Improved flexibility': [
            'Improved flexibility', 'Flexibility', 'Improved strength and flexibility', 'Improved flexibility and strength',
            ' and Improved flexibility.', ' and Improved flexibility', ' and improved flexibility'
        ],
        'Stress relief': [
            'Stress relief', 'Reduces stress', 'Reduces stress and anxiety', 'Stress relief and improved mood',
            ' Stress relief', ' stress relief'
        ],
        'Confidence': [
            'Increased self-confidence', ' Improved self-confidence', ' Increased self-esteem',
            ' and Increased self-confidence', ' Increased self-confidence', ' and Increased self-'
        ],
        'Physical fitness': [
            'Increased physical fitness', 'Improved physical fitness', 'Burning calories and losing', 
            ' and increased physical fitness', ' Improved physical fitness', 'Increased physical activity and exercise',
            'Enhanced physical fitness', 'Weight loss'
        ],
        'Social connection': [
            'Social connection', ' and Improved social skills', ' and Social connection', ' Social connections',
            ' and social connection'
        ],
        'Mental health': [
            'Improves mental health', 'Reduces stress and improves mental health',
            'Potential physical or mental health benefits associated with performing the dance', 
            'Dancing can offer physical and mental health benefits'
        ],
        'Strength': [
            'Improved strength and flexibility', 'Improved flexibility and strength', ' and Muscle'
        ],
        'Community': [
            'A sense of community and belonging'
        ],
        'Boost': [
            'Boost', ' Boosted mood', ' Increased energy levels', ' Boost', 'Stress relief and improved mood',
            ' and Increased energy', '55]: Increased happiness and well-being'
        ],
        'Cerebellum': [
            'Improved balance', ' Improved coordination', ' Improved posture', 
            ' Improved balance and coordination', ' Improved cognitive function'
        ]
    }

        # Function to determine the overall health benefit
        def extract_overall_benefit(benefits):
            for benefit_name, keywords in benefit_keywords.items():
                if any(keyword in benefits for keyword in keywords):
                    return benefit_name  # Return the first matching benefit category
            return 'None'  # Default if no benefits match

        # Replace the Health Benefits column with overall health benefit
        df['Health Benefits'] = df['Health Benefits'].apply(lambda x: extract_overall_benefit(x))

        dfr=df
        st.dataframe(dfr)

        #Purpose:
        st.subheader("Overview")
        st.markdown(''' The purpose of the dataset is to identify the potential physical or mental health benefits associated with the dances from the dance dataset. 
                    It is able to describes the positive effects of dancing on health and well-being.
                    This helps encourage people to exercise through dance, learn how to dance, explore different dance styles from differe cultures, and more!''')
    
        st.subheader("Features:")
        st.markdown('''
                    - Improved cardiovascular health (Text)
                    - Improved flexibility (Text)
                    - Stress relief (Text)
                    - Confidence (Text)
                    - Physical fitness (Text)
                    - Social connection (Text)
                    - Mental health (Text)
                    - Strength (Text)
                    - Community (Text)
                    - Boost (Text)
                    - Cerebellum (Text)
                    ''')

        st.subheader("IDA")
        st.write("I created this dataset from the dance dataset, so the IDA is the same. ")

        code='''
        health_benefits_split = df['Health Benefits'].str.split(",")
        my_list = health_benefits_split.tolist()
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

        st.subheader("Heatmap")

        health_benefits_split = df['Health Benefits'].str.split(",")
        my_list = health_benefits_split.tolist()
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
        #print(Improved_cardiovascular_health)

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
        #print(Improved_flexibility)

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
        #print(Stress_relief)

        #added to cerebellum
        Improved_posture = []
        for i in range(len(my_list)):
            if " Improved posture" in my_list[i]:
                Improved_posture.append(1)
            elif "Improved posture" in my_list[i]:
                Improved_posture.append(1)
            else:
                Improved_posture.append(0)
       #print(Improved_posture)

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
        #print(Confidence)

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
        #print(Physical_fitness)

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
        #print(Social_connection)

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
        #print(Mental_health)

        Strength = []
        for i in range(len(my_list)):
            if "Improved flexibility and strength" in my_list[i]:
                Strength.append(1)
            elif "Improved strength and flexibility" in my_list[i]:
                Strength.append(1)
            else:
                Strength.append(0)
        #print(Strength)

        Community = []
        for i in range(len(my_list)):
            if " A sense of community and belonging" in my_list[i]:
                Community.append(1)
            else:
                Community.append(0)
        #print(Community)

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
        #print(Boost)

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
        #print(Cerebellum)

        #Create a matrix for each health benefit
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

        # Heatmap for Health Benefits Matrix
        st.write("## Heatmap for Health Benefits Matrix")
        plt.figure(figsize=(10, 8))
        sns.heatmap(health_benefits_matrix, annot=True, cmap='coolwarm')
        plt.title('Heatmap for Health Benefits Matrix')
        st.pyplot(plt.gcf())  # Display the plot in Streamlit

        st.divider()

        st.subheader("Encoding")
        st.write("N/A")
        st.divider()

        st.subheader("Imputing")
        #st.write("N/A")
        code='''

        dance_names = df['Dance style'].tolist()  # Convert dance styles to a list

        # Iterate over the DataFrame by rows and columns to replace 1s
        for col in health_benefits_matrix.columns:  # Iterate over each column
            for row in range(len(health_benefits_matrix)):  # Iterate over each row
                if health_benefits_matrix.at[row, col] == 1:  # Access element by row and column
                    health_benefits_matrix.at[row, col] = dance_names[row]  # Replace 1 with the dance name
                if health_benefits_matrix.at[row, col] == 0:  # Access element by row and column
                    health_benefits_matrix.at[row, col] = "None"

        st.write(health_benefits_matrix)
        '''
        st.code(code, language="python")

        st.divider()

        st.subheader("Modeling")
        st.subheader("Recommendation System Code")
        code = '''
        
    benefit_keywords = {
    'Improved cardiovascular health': [
        'Improved cardiovascular health', 'Improved cardiov', 'Improved cardiovascular health and increased physical fitness',
        'Cardiovascular health', 'Positive effects on cardiovascular health', 'Moderate cardiovascular workout',
        ' such as improved cardiovascular'
    ],
    'Improved flexibility': [
        'Improved flexibility', 'Flexibility', 'Improved strength and flexibility', 'Improved flexibility and strength',
        ' and Improved flexibility.', ' and Improved flexibility', ' and improved flexibility'
    ],
    'Stress relief': [
        'Stress relief', 'Reduces stress', 'Reduces stress and anxiety', 'Stress relief and improved mood',
        ' Stress relief', ' stress relief'
    ],
    'Confidence': [
        'Increased self-confidence', ' Improved self-confidence', ' Increased self-esteem',
        ' and Increased self-confidence', ' Increased self-confidence', ' and Increased self-'
    ],
    'Physical fitness': [
        'Increased physical fitness', 'Improved physical fitness', 'Burning calories and losing', 
        ' and increased physical fitness', ' Improved physical fitness', 'Increased physical activity and exercise',
        'Enhanced physical fitness', 'Weight loss'
    ],
    'Social connection': [
        'Social connection', ' and Improved social skills', ' and Social connection', ' Social connections',
        ' and social connection'
    ],
    'Mental health': [
        'Improves mental health', 'Reduces stress and improves mental health',
        'Potential physical or mental health benefits associated with performing the dance', 
        'Dancing can offer physical and mental health benefits'
    ],
    'Strength': [
        'Improved strength and flexibility', 'Improved flexibility and strength', ' and Muscle'
    ],
    'Community': [
        'A sense of community and belonging'
    ],
    'Boost': [
        'Boost', ' Boosted mood', ' Increased energy levels', ' Boost', 'Stress relief and improved mood',
        ' and Increased energy', '55]: Increased happiness and well-being'
    ],
    'Cerebellum': [
        'Improved balance', ' Improved coordination', ' Improved posture', 
        ' Improved balance and coordination', ' Improved cognitive function'
    ]
}

    # Function to determine the overall health benefit
    def extract_overall_benefit(benefits):
        for benefit_name, keywords in benefit_keywords.items():
            if any(keyword in benefits for keyword in keywords):
                return benefit_name  # Return the first matching benefit category
        return 'None'  # Default if no benefits match

    # Replace the Health Benefits column with overall health benefit
    df['Health Benefits'] = df['Health Benefits'].apply(lambda x: extract_overall_benefit(x))

    dfr=df
        '''
        st.code(code,language='python')


       


    with tab3:
        st.header("Calories")
        df2 = pd.read_csv("exercise_dataset.csv")
    
        st.write("Calories Dataset")
        st.dataframe(df2)

        #Purpose:
        st.subheader("Overview")
        st.markdown(''' The purpose of the dataset is to gather the number of calories burned by a person while performing some activity/exercise. 
                    The dataset contatins 248 activities and exercises that range from running, cycling, calisthenics, dance, and more.
                    ''')
        st.subheader("Features:")
        st.markdown(
            """
                - Activity, Exercise or Sport (1 hour) - The activity/exercise names (Text)
                - 130 lb - The calories burned by a person weighing 130 lb ~ 58.967 kg (Integer)
                - 155 lb - The calories burned by a person weighing 150 lb ~ 70.306 kg (Integer)
                - 180 lb - The calories burned by a person weighing 180 lb ~ 81.646 kg (Integer)
                - 205 lb - The calories burned by a person weighing 205 lb ~ 92.986 kg (Integer)
                - Calories per lb - The number of calories burned per kg (Float)
            """
            )

        #Edited Calories Dataset
        st.subheader("Edited Calories Dataset")
        #d3 = df2.drop(['130 lb', '155 lb', '180 lb', '205 lb'], axis=1)
        d3 = df2.iloc[[29, 34, 35, 36],:]
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
        st.write("The data types did not need to be corrected for they were all integers, except for one feature being a float value (numerical)")

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

        st.divider()

        st.subheader("EDA")

        st.title("Outlier Detection and Visualization")

        # Function to detect outliers
        def outlier(column):
            z = np.abs(stats.zscore(df2[column]))
            threshold = 3
            outliers = df2[z > threshold]
            st.write(f"**Outliers for {column}:**")
            st.dataframe(outliers)

        # Outlier detection for specific columns
        st.write("### Outlier Detection Results")
        outlier('205 lb')  # Running, cross-country skiing
        outlier('Calories per kg')  # Running, cross-country skiing

        # Visualize outliers with histograms
        st.write("### Histograms for Outlier Assessment")
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))

        columns = ['130 lb', '155 lb', '180 lb', '205 lb', 'Calories per kg']
        titles = ['130 lb Outlier', '155 lb Outlier', '180 lb Outlier', '205 lb Outlier', 'Calories Outlier']

        for i, (column, title) in enumerate(zip(columns, titles)):
            ax = axes.flat[i]
            ax.hist(df2[column], bins=10, color='skyblue', edgecolor='black')
            ax.set_title(title)
            ax.set_xlabel(column)
            ax.set_ylabel("Frequency")

        # Hide the last subplot if the number of columns is less than the grid
        if len(columns) < len(axes.flat):
            axes.flat[len(columns)].axis("off")

        st.pyplot(fig)

        #st.write(" Univariate analysis - Histograms")
        st.title("Boxplot Visualization for Outlier Detection")

        # Plotting Boxplots
        fig = plt.figure(figsize=(10, 7))

        plt.subplot(2, 3, 1)
        plt.boxplot(df2['130 lb'])
        plt.title("130 lb")

        plt.subplot(2, 3, 2)
        plt.boxplot(df2['155 lb'])
        plt.title("155 lb")

        plt.subplot(2, 3, 3)
        plt.boxplot(df2['180 lb'])
        plt.title("180 lb")

        plt.subplot(2, 3, 4)
        plt.boxplot(df2['205 lb'])
        plt.title("205 lb")

        plt.subplot(2, 3, 5)
        plt.boxplot(df2['Calories per kg'])
        plt.title("Calories")

        # Display the figure in Streamlit
        st.pyplot(fig)


        st.subheader("Bivariate analysis - Scatter plots")
        # Create the figure (initially blank)
        fig = go.Figure()

        # Add the scatter trace
        fig.add_trace(go.Scatter(
            x=dataF['x'],  # Variable on the x-axis
            y=dataF['y'],  # Variable on the y-axis
            mode='markers',  # Observations are represented as points
            marker=dict(
                size=12,  # Marker size
                color='#cb1dd1',  # Marker color
                opacity=0.8,  # Marker transparency
                line=dict(width=1, color='black')  # Marker edge properties
            ),
        ))

        # Customize the layout
        fig.update_layout(
            title='Interactive Scatter Plot of Activity vs. Calories Burned',  # Plot title
            xaxis_title="Activity, Exercise or Sport (1 hour)",  # x-axis label
            yaxis_title='Calories per kg',  # y-axis label
            width=800,  # Plot width
            height=600,  # Plot height
        )

        st.plotly_chart(fig)


        st.subheader("Cross Tabulations")
        st.title("Crosstab of Activities and Calories Burned")

        # Generate a simple crosstab
        crosstab_result = pd.crosstab(d3['Activity, Exercise or Sport (1 hour)'], d3['Calories per kg'])

        # Crosstab with `dropna=False`
        crosstab_with_na = pd.crosstab(d3['Activity, Exercise or Sport (1 hour)'], d3['Calories per kg'], dropna=False)

        # Display the crosstab results
        st.write("**Crosstab Without NaN Values Dropped:**")
        st.dataframe(crosstab_result)

        st.write("**Crosstab With NaN Values Included:**")
        st.dataframe(crosstab_with_na)
       

        st.subheader("Pattern and trend identification")
        st.title("Scatter Plot: Activity vs. Calories Burned")

        # Create the scatter plot using Matplotlib
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.scatter(d3['Activity, Exercise or Sport (1 hour)'], d3['Calories per kg'], color='lightcoral')
        ax.set_title('Activity vs. Calories', fontsize=14)
        ax.set_xlabel('Activity', fontsize=12)
        ax.set_ylabel('Calories', fontsize=12)
        #ax.box(False)
        st.pyplot(fig)

        st.divider()

        st.subheader("Cleaning")
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
        st.write("No encoding was necessary.")
        st.divider()

        st.subheader("Imputing")
        st.write("N/A")
        st.divider()

        st.subheader("Modeling")
        st.title("Filter Activities")
        # Select box to filter activities
        filter2 = st.selectbox("Filter Activity", d3["Activity, Exercise or Sport (1 hour)"].unique())

        # Filter the DataFrame based on the selected activity
        filtered2 = d3[d3["Activity, Exercise or Sport (1 hour)"] == filter2]

        # Display the filtered DataFrame
        st.write("Filtered Data:")
        st.dataframe(filtered2)

    with tab4:
        st.header("Cardiovascular")
        df3 = pd.read_csv("CVD_cleaned.csv")
        st.write("Cardiovascular Dataset")
        st.dataframe(df3)

        #Purpose:
        st.subheader("Overview")
        st.markdown("""This dataset incorporates *The Behavioral Risk Factor Surveillance System (BRFSS)*. The BRFSS is the nation’s premier system of health-related telephone surveys that collect state data about U.S. residents regarding their health-related risk behaviors, chronic health conditions, and use of preventive services.
                    The dataset from BRFSS contains 304 unique variables, but this dataset only contains 19 variables that relate to lifestyle factors of a person that can be contributed to being at risk with any form of Cardiovascular Diseases.
                   """)
        st.subheader("Features:")
        st.markdown(
            """
            - General Health - Ranks your general health varying from: poor, very good, good, fair (Text)
            - Checkup - Asks how long has it been since you last visited a doctor for a routine checkup varying from: within the pask 2 years, within the past year (Text)
            - Exercise - If during the past month, other than your regular job, did you participate in any physical activities or exercises, with the answer being either yes or no (Text)
            - Heart Disease - Respondents reported having coronary heart disease or mycardialinfarction, with the answer being either yes or no (Text)
            - Skin Cancer - Respondents that reported having skin cancer with the answer being either yes or no (Text)
            - Other Cancer - Respondents that reported having any other types of cancer with the answer being either yes or no (Text)
            - Depression - Respondents that reported having a depressive disorder (including depression, major depression, with the answer being either yes or no (Text)
            - Diabetes - Respondents that reported having a diabetes. If yes, what type of diabetes it is/was (Text)
            - Arthritis - Respondents that reported having an Arthritis, with the answer being either yes or no (Text)
            - Sex - Respondent's Gender (Text)
            - Age Category - Respondent's Age (Text)
            - Height(cm) - Respondent's Height (Float)    
            - Weight(kg) - Respondent's Weight (Float)
            - BMI - Respondent's BMI score (Float)  
            - Smoking_History - If respondents have a history of smoking with the answer being either yes or no (Text)
            - Alcohol Consumption - If during the past month, how much alcohol have the respondents consumed (Float)
            - Fruit Consumption - How much fruit the respondents consume (Float)    
            - Green Vegetables Consumption - How much green vegetables the respondents consume (Float)
            - Fried Potato Consumption- How much fried potatoes the respondents consume (Float)    

            """
        )

        st.subheader("IDA")

        st.write("Missing Values")
        code='''
        #IDA Step 2: Data cleaning and preprocessing - Handle missing values - Remove duplicates - Correct data types - Standardize formats
        # Cardiovascular dataset
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
        st.code(code, language='python')

        st.write("Data Types")
        st.write("The data types for the features consisted of majority categorical (textual) with the others people floats.")
        st.write("I corrected the categorical features through encoding")

        st.write("Standaraize formats")
        code='''
        #Standardize formats
        numeric_cols_df3 = df3.select_dtypes(include=[np.number]).columns
        z3 = df3[numeric_cols_df3].apply(zscore)
        print(z3)
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

        st.divider()

        st.subheader("EDA")

        st.write("Quantify missing data")
        from sklearn.preprocessing import OrdinalEncoder, LabelEncoder, OneHotEncoder
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

        df3['Age_Category'] = le.fit_transform(df3['Age_Category'])

        import plotly.figure_factory as ff
        selected_features1 = [
            'General_Health', 'Exercise', 'Heart_Disease',
            'Height_(cm)', 'Weight_(kg)', 'BMI',
            'Fruit_Consumption', 'Green_Vegetables_Consumption'
        ]

        # Compute the correlation matrix
        correlation_matrix = df3[selected_features1].corr().values

        # Create an annotated heatmap
        fig_heatmap = ff.create_annotated_heatmap(
            z=correlation_matrix,
            x=selected_features1,
            y=selected_features1,
            colorscale='Viridis'
        )

        # Update layout
        fig_heatmap.update_layout(
            title="Correlation Heatmap of Cardiovascular Dataset (Interactive)",
            xaxis_title="Features",
            yaxis_title="Features",
            width=1500,
            height=1000
        )

        st.title("Interactive Correlation Heatmap")
        st.plotly_chart(fig_heatmap)

    
        st.title("Heatmap of Missingness in Cardiovascular Dataset")
        # Plot heatmap of missing values
        fig, ax = plt.subplots(figsize=(4, 8))
        sns.heatmap(df3.isna(), cmap="magma", ax=ax)
        ax.set_title("Heatmap of Missingness in Cardiovascular Dataset")
        st.pyplot(fig)


        st.write("Outlier detection")

        def outlier(column):
            z = np.abs(stats.zscore(df3[column].dropna()))
            threshold = 3
            outliers = df3.iloc[np.where(z > threshold)]
            st.write(f"**Outliers for {column}:** {len(outliers)} rows detected.")

        # Select column for outlier analysis
        column = st.selectbox(
            "Select a column to analyze for outliers:",
            ['Heart_Disease', 'Diabetes', 'Height_(cm)', 'Weight_(kg)', 'BMI', 'Fruit_Consumption', 'Green_Vegetables_Consumption']
        )
        if column:
            outlier(column)

        # Visualization: Histograms
        st.write("### Distribution Plots with Outliers")

        fig, axs = plt.subplots(3, 3, figsize=(15, 10))
        axs = axs.flatten()

        columns = [
            'Heart_Disease', 'Diabetes', 'Height_(cm)', 'Weight_(kg)', 
            'BMI', 'Fruit_Consumption', 'Green_Vegetables_Consumption'
        ]

        for i, col in enumerate(columns):
            if i < len(axs):
                axs[i].hist(df3[col], color='skyblue')
                axs[i].set_title(f"{col} Outliers")
                axs[i].set_xlabel(col)
                axs[i].set_ylabel("Frequency")

        plt.tight_layout()
        st.pyplot(fig)

        # Mean and Median calculations
        st.write("### Mean and Median with Outliers")
        for col in columns:
            mean = df3[col].mean()
            median = df3[col].median()
            st.write(f"{col}: Mean = {mean:.2f}, Median = {median:.2f}")

        # Mean and Median calculations without outliers
        st.write("### Mean and Median Without Outliers")
        for col in columns:
            z = np.abs(stats.zscore(df3[col].dropna()))
            no_outliers = df3[col][z <= 3]
            mean = no_outliers.mean()
            median = no_outliers.median()
            st.write(f"{col}: Mean (No Outliers) = {mean:.2f}, Median (No Outliers) = {median:.2f}")

        st.subheader("Count Plots for Key Health Indicators")

        fig, axs = plt.subplots(2, 2, figsize=(20, 15))

        sns.countplot(x='General_Health', data=df3, ax=axs[0, 0])
        axs[0, 0].set_title("General Health")

        sns.countplot(x='Exercise', data=df3, ax=axs[0, 1])
        axs[0, 1].set_title("Exercise")

        sns.countplot(x='Heart_Disease', data=df3, ax=axs[1, 0])
        axs[1, 0].set_title("Heart Disease")

        sns.countplot(x='Diabetes', data=df3, ax=axs[1, 1])
        axs[1, 1].set_title("Diabetes")

        plt.tight_layout()
        st.pyplot(fig)

        st.subheader("Box Plots for Key Health and Lifestyle Indicators")
        fig = plt.figure(figsize=(12, 10))

        plt.subplot(3, 3, 1)
        plt.boxplot(df3['General_Health'])
        plt.title("General Health")

        plt.subplot(3, 3, 2)
        plt.boxplot(df3['Exercise'])
        plt.title("Exercise")

        plt.subplot(3, 3, 3)
        plt.boxplot(df3['Heart_Disease'])
        plt.title("Heart Disease")

        plt.subplot(3, 3, 4)
        plt.boxplot(df3['Diabetes'])
        plt.title("Diabetes")

        plt.subplot(3, 3, 5)
        plt.boxplot(df3['Height_(cm)'])
        plt.title("Height (cm)")

        plt.subplot(3, 3, 6)
        plt.boxplot(df3['Weight_(kg)'])
        plt.title("Weight (kg)")

        plt.subplot(3, 3, 7)
        plt.boxplot(df3['BMI'])
        plt.title("BMI")

        plt.subplot(3, 3, 8)
        plt.boxplot(df3['Fruit_Consumption'])
        plt.title("Fruit Consumption")

        plt.subplot(3, 3, 9)
        plt.boxplot(df3['Green_Vegetables_Consumption'])
        plt.title("Green Vegetables Consumption")

        plt.tight_layout()
        st.pyplot(fig)

        st.write("### Interactive Scatterplots")
        fig1 = px.scatter(
            df3,
            x='Height_(cm)',
            y='Weight_(kg)',
            color='General_Health',
            title="Relationship Between Height and Weight by General Health Status",
            labels={"Height_(cm)": "Height (cm)", "Weight_(kg)": "Weight (kg)", "General_Health": "General Health"}
        )

        #first scatter plot
        st.plotly_chart(fig1)

        # Scatter plot: Fruit Consumption vs. Green Vegetables Consumption
        fig2 = px.scatter(
            df3,
            x='Fruit_Consumption',
            y='Green_Vegetables_Consumption',
            color='General_Health',
            title="Relationship Between Fruit and Green Vegetables by General Health Status",
            labels={"Fruit_Consumption": "Fruit Consumption", "Green_Vegetables_Consumption": "Green Vegetables Consumption", "General_Health": "General Health"}
        )

        #second scatter plot
        st.plotly_chart(fig2)

        st.subheader("Cross tabulations")
        crosstab = pd.crosstab(
            df3['Fruit_Consumption'],
            df3['Green_Vegetables_Consumption'],
            dropna=False
        )

        # Display the crosstab in Streamlit
        st.write(crosstab)

        #st.subheader("Multivariate analysis - Pair plots")
        numeric_cols_df3 = df3.select_dtypes(include=[np.number]).columns
        #fig = sns.pairplot(df3[numeric_cols_df3])
        #st.pyplot(fig)

        st.divider()

        st.subheader("Cleaning")
        st.write("Examples of cleaning the dataset in IDA and Encoding sections")
        code='''

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

        # Compute correlation matrix
        numeric_cols_df3 = df3.select_dtypes(include=[np.number]).columns
        corr_matrix = df3[numeric_cols_df3].corr()

        # Display the heatmap
        st.subheader("Correlation Heatmap of Fixed Calories Dataset")
        fig, ax = plt.subplots(figsize=(20, 16))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax)
        plt.title('Correlation Heatmap of Fixed Calories Dataset')
        st.pyplot(fig)

        st.code(code, language="python")
        st.write("PCA")
        numeric_cols_df3 = df3.select_dtypes(include='number').columns

        # Standardize the features
        scaler = StandardScaler()
        scaled_data = pd.DataFrame(scaler.fit_transform(df3[numeric_cols_df3]), columns=numeric_cols_df3)

        # Display scaled data
        st.write("### Scaled Data")
        st.dataframe(scaled_data)

        # Heatmap of correlation before PCA
        st.write("### Correlation Heatmap Before PCA")
        fig1, ax1 = plt.subplots(figsize=(10, 8))
        sns.heatmap(scaled_data.corr(), annot=True, cmap='coolwarm', ax=ax1)
        st.pyplot(fig1)

        # Apply PCA
        pca = PCA(n_components=3)
        pca.fit(scaled_data)
        data_pca = pd.DataFrame(pca.transform(scaled_data), columns=['PC1', 'PC2', 'PC3'])

        # Display PCA-transformed data
        st.write("### PCA Transformed Data")
        st.dataframe(data_pca)

        # Heatmap of correlation after PCA
        st.write("### Correlation Heatmap After PCA")
        fig2, ax2 = plt.subplots(figsize=(8, 6))
        sns.heatmap(data_pca.corr(), annot=True, cmap='coolwarm', ax=ax2)
        st.pyplot(fig2)

        st.subheader("Linear Regression (Interactive)")
        from sklearn.linear_model import LinearRegression
        from sklearn.model_selection import train_test_split
        from sklearn.metrics import mean_squared_error, r2_score
        import plotly.graph_objects as go

        # Linear Regression Function
        def linear_regression(feature1, feature2):
            # Feature matrix (X) and target variable (y)
            X = df3[[feature1]]  # Predictor (independent variable)
            y = df3[[feature2]]  # Target (dependent variable)

            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Initialize the linear regression model
            model = LinearRegression()

            # Fit the model to the training data
            model.fit(X_train, y_train)

            # Make predictions on the testing data
            y_pred = model.predict(X_test)

            # Model evaluation
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)

            # Display coefficients and evaluation metrics
            st.write(f"### Linear Regression Results for {feature1} vs {feature2}")
            st.write(f"Intercept: {model.intercept_[0]:.2f}")
            st.write(f"Coefficient: {model.coef_[0][0]:.2f}")
            st.write(f"Mean Squared Error: {mse:.2f}")
            st.write(f"R-squared: {r2:.2f}")

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

            st.plotly_chart(fig)

        st.title("Linear Regression Analysis")
        # Feature selection
        feature1 = st.selectbox("Select Predictor (X)", numeric_cols_df3)
        feature2 = st.selectbox("Select Target (Y)", numeric_cols_df3)

        # Run linear regression if features are selected
        if feature1 != feature2:
            linear_regression(feature1, feature2)
        else:
            st.write("Please select different features for Predictor and Target.")

        st.subheader("Linear Regression Plots")

        # Linear Regression Function
        def linear_regression(feature1, feature2):
            # Feature matrix (X) and target variable (y)
            X = df3[[feature1]]
            y = df3[[feature2]]

            # Split the data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Initialize the linear regression model
            model = LinearRegression()
            model.fit(X_train, y_train)

            # Make predictions on the testing data
            y_pred = model.predict(X_test)

            # Evaluation Metrics
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)

            # Display metrics
            st.write(f"### Regression Results for {feature1} vs {feature2}")
            st.write(f"Intercept: {model.intercept_[0]:.2f}")
            st.write(f"Coefficient: {model.coef_[0][0]:.2f}")
            st.write(f"Mean Squared Error: {mse:.2f}")
            st.write(f"R-squared: {r2:.2f}")

            # Create an interactive scatter plot
            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=X_test[feature1].values.flatten(),
                y=y_test[feature2].values.flatten(),
                mode='markers',
                name='Actual',
                marker=dict(color='blue')
            ))

            fig.add_trace(go.Scatter(
                x=X_test[feature1].values.flatten(),
                y=y_pred.flatten(),
                mode='lines',
                name='Predicted',
                line=dict(color='red', width=2)
            ))

            fig.update_layout(
                title=f"Linear Regression: {feature1} vs {feature2}",
                xaxis_title=feature1,
                yaxis_title=feature2,
                legend=dict(x=0, y=1)
            )

            st.plotly_chart(fig)

        # Streamlit Layout
        st.title("Linear Regression Analysis for Various Features")

        # Define regression cases
        regression_cases = [
            ('Weight_(kg)', 'Sex'),
            ('Exercise', 'General_Health'),
            ('Heart_Disease', 'Depression'),
            ('Heart_Disease', 'Diabetes'),
            ('Heart_Disease', 'Arthritis'),
            ('Heart_Disease', 'Sex'),
            ('Heart_Disease', 'Age_Category'),
            ('Heart_Disease', 'Height_(cm)'),
            ('Heart_Disease', 'Weight_(kg)'),
            ('Heart_Disease', 'BMI'),
            ('Heart_Disease', 'Smoking_History'),
        ]

        # Create dropdown for user selection
        case = st.selectbox("Select Feature Pair for Linear Regression", regression_cases, format_func=lambda x: f"{x[0]} vs {x[1]}")

        # Perform linear regression for the selected case
        if case:
            linear_regression(*case)
        

#Notes:
#Historical data analysis with trends and patterns

#Health Improvement Forecasts: Show how continuing a specific dance routine can improve cardiovascular health or stamina.
#Example Insight:
#Based on your recent sessions, dancing for 20 more minutes per week could improve your cardiovascular endurance by 10%.”
 #Comparison of dance type over times for efficacy


#streamlit run /Users/kendallandrews/Downloads/dance_health.py
