import streamlit as st
import pandas as pd

def app():
    # title of the app
    st.markdown('All Tournament Games Since 1985')
    team = st.text_input("Team: ",'')
    AG = pd.read_csv('notebooks/step04_FUHistory.csv')

    AG = AG.drop(['Fti','Uti'],axis=1)
    AG['Year'] = AG['Year'].astype('str')

    if team != "":
        AG = AG[(AG['AFTeam'].str.contains(team))|(AG['AUTeam'].str.contains(team))]
        
        
        
    st.dataframe(AG,height= 500)

    
    
     
    