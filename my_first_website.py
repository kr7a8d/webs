from PIL import Image 
import requests
import streamlit as st
from streamlit_lottie import st_lottie


#find more emojies here: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.set_page_config(page_title="my_WebPage", page_icon=":toda:")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



# ----LOAD ASSETS----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_for_proj1 = Image.open("images/Here_is_My_first_Project.jpg")
img_for_proj2 = Image.open("images/Here_is_My_second_Project.jpg")

# ----HEADER SECTION----
with st.container():
    st.subheader("Hi My Name is Faris :wave:")
    st.title(" a NEW Coding Programer from (SaudiArabia)")
    st.write("")
    st.write("i am Passionate about finding ways to use Programing Language to be more efficient and effective in buesiness settings")

# ----What I Do----
with st.container():
    st.write("-----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My Dream")
        st.write("##")
        st.write(
        """
        My Dream is to be a Programer. my favorite part of Programing is Game Development because my main programing language is C#.
        i'll spend a lot of my free time on Game Development. this is my first try of making a website. i'll put all of my projects here. 
        """
         )
        st.write("##")
        st.write("all of my new projects will be down here but for now i don't have any projects to work on in my mind")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


# --- PROJECTS ---

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    
    with image_column:
        st.image(img_for_proj1)

with text_column:
    st.subheader("This is my first project")
    st.write("discerption")

#--- SECOND PROJECT ---

with st.container():
    st.write("##")
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img_for_proj1)
    
with text_column:
    st.subheader("This is my second project")
    st.write("discreption")
