import streamlit as st
st.title('Airline and Climate Analysis: Snowflake and Streamlit Demo')
st.image("Hump Jupiter (XS)_jpg.jpg")


st.balloons()
st.header("Meet the Snowflake Soldiers!")

col1, col2 = st.columns(2)

with col1:  
    st.image("Michael.jpg", "Michael Nguyen", width = 200)
    st.image("Sivaji.jpg", "Sivaji Turimella", width = 200)


with col2:
    st.image("Jackie.jpg", "Jackie Driscoll", width = 200)
    st.image("Sruti.png", "Sruti Bandaru", width = 200)

