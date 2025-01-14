"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
from PIL import Image
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview","About Us"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### NM3 Data Systems')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("Our solution is built to give your users a highly accurate recommendation. The solution is developed to make recommendations using both content based recommendations and collaborative based recommendations.")
        st.write("With its high accuracy rating when making recommendations, the solution is also easy to use. We spared no effort in making sure that any one can make use of the solution even if it is the first time the user is coming in contact with it.")
        st.write("In order to make sure your needs are met whenever they come up, we have customer support running 24 hours every day of the week. Sit back, relax and see your user interaction improve with an accompanying revenue boost.")         
        
        # EDA Images
       
        genres = Image.open('resources/imgs/movies_by_genre.png')
        production_year = Image.open('resources/imgs/movies_by_production_year.png')
        top_rated = Image.open('resources/imgs/Top_rated_movies.png')

        # Exploratory Data Analysis
        st.subheader("Insight from the Data - EDA")
        st.write("Below are insights into the dataset used in developing our solution.")
        
        # Genres
        st.image(genres)
        st.write("The graph shows the genres of movies in the data set. We can see that users watch more of dramas, comedies and thrillers")

        # production year
        st.image(production_year)
        st.write("Insight from our data shows that over 1750 movies were produced in the year 2015. This period represents the most active year of movie production.")

        # Top rated movies
        st.image(top_rated)
        st.write("The most top rated movie in our data set is Shawshank Redemption produced in 1994. The graph shows the 20 most top rated movies.")
        
        
        st.write("NM3 Data Systems, providing solutions to your problems.")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
    # Our contact for enquiries

    if page_selection == "About Us":
        st.title("About Us")
        st.write("NM3 Data Systems Ltd. is a data solutions company, specializing in prediction models and recommender engines. We are headquartered in Abuja, Nigeria. Our team members include Harmony Odumuko (CEO), Murtala Umar Adamu (CTO), Njoku Okechukwu Valentine, Prince-Charles, Akinbo-Taylor and Abdulwasiu Inusa.")
        st.write("Our vision is to become the leading IT company in Africa by solving the most pressing challenges faced by our clients through innovative solutions that help them grow their businesses faster and more efficiently than ever before.")
        st.subheader("Contact info")
        st.write("Cola Street, Near ATTC,")
        st.write("ICT Hub, Central Business District,\
            Abuja, P.O. Box AN0000, Nigeria")
        st.write("Telephone:+234 00 111 2222")
        st.write("WhatsApp:+234 210 12344 1390")
        st.write("Email: contact@datasytems.com")
        st.write("Website: www.datasytems.com") 

    
if __name__ == '__main__':
    main()
