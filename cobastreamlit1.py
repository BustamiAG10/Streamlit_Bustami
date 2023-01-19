import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import altair as alt
import graphviz as graphviz

st. write("Halo, mari kita pelajari cara membuat aplikasi streamlit bersama")
st.title ("this is the app title")
st.header("this is the header")
st.markdown("this is the mardown")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')


st.image("unsada_logo.jpg")
st.audio("my_audio2.mp3")
st.video("my_video.mp4")
#video - loop
video_html = """
 <video controls width="700" autoplay="true" muted="true" loop="true">
 <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-
videos/flower.webm" type="video/mp4" />
 </video>
 """
col1, col2 = st.columns([1, 1])
col1.markdown(video_html, unsafe_allow_html=True)
# image-center
col1, col2, col3 = st.columns(3)
with col1:
 st.write(' ')
with col2:
 st.image("unsada_logo.jpg")
with col3:
 st.write(' ')


st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)


st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')




st.success("You did it !")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError("RuntimeError exception"))

rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

df= pd.DataFrame(
 np.random.randn(10, 2),
 columns=['x', 'y'])
st.line_chart(df)

df= pd.DataFrame(
 np.random.randn(10, 2),
 columns=['x', 'y'])
st.bar_chart(df)

df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [-6.23, 106.93],
columns=['lat', 'lon'])
st.map(df)


