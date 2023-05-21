from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon="🎉", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_pyawb2b1.json")
img_rc_team = Image.open("images/rc-team.jpeg")
img_cuisine = Image.open("images/cuisine-restaurant.jpg")

# ---- Header Section ----
with st.container():
    st.subheader("Hi, I am Arnaldo 👋")
    st.title("Software Engineer")
    st.write("I am passionate about video games, swimming, pool, and creating websites")
    st.write("[Learn More >](https://github.com/ArnoldPires)")

# ---- What I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            A deep analytical growth mindset problem solver who creates and maintains Full Stack Web Applications.
            - Strong Technological IT Support Background
            - QA Tester
            - UX/UI designer
            - Avid Gamer
            - Swimmer
            - Lover of Art
            - Nature
            - Deep Conversation
            - and Philosophy.
            """
        )
        st.write("[Portfolio >](https://arnaldopires.com/)")
    with right_column:
        if lottie_coding is not None:
            st_lottie(lottie_coding, height=300, key="coding")
        else:
            st.write("Failed to load Lottie animation.")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_rc_team)
    with text_column:
        st.subheader("Resilient Coders Living Room")
        st.write(
            """
            I created this Virtual Reality website using A-frame, a JavaScript framework only using HTML!
            """
        )
        st.markdown("[Check it out...](https://arnaldopires.com/Resilient-Coder-Living-Room/)")

with st.container():
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_cuisine)
    with text_column:
        st.subheader("Cuisine Restaurant")
        st.write(
            """
            Using HTML, CSS, and JavaScript, I was able to create this wonderful site for a restaurant.
            """
        )
        st.markdown("[Check it out...](https://cuisine-restaurant.netlify.app/)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documentation: https://formsubmit.co/
    contact_form = """
    <form action="https://formsubmit.co/arnold.pires92@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
