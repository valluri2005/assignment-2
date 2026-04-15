import streamlit as st

# Page configuration
st.set_page_config(page_title="My College Event", layout="centered")

# -------------------------
# CSS Styling (Inline in Streamlit)
# -------------------------
st.markdown("""
    <style>
        .main-title {
            text-align: center;
            color: white;
            background-color: #333;
            padding: 15px;
            border-radius: 10px;
        }

        .highlight {
            background-color: yellow;
            padding: 5px;
            font-weight: bold;
        }

        .section {
            background-color: #4caf50;
            padding: 15px;
            border-radius: 10px;
            color: white;
        }

        ul {
            background-color: #e0f7fa;
            padding: 15px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------
# Title
# -------------------------
st.markdown("<h1 class='main-title'>My College Event</h1>", unsafe_allow_html=True)

# Inline-style like text
st.markdown("<p style='color:red; text-align:center;'>Welcome to our Annual College Fest!</p>", unsafe_allow_html=True)

# -------------------------
# About Section
# -------------------------
st.subheader("About the Event")
st.write("Our college event includes cultural activities, technical workshops, and fun competitions.")

# -------------------------
# Special Attractions Section
# -------------------------
st.markdown("<div class='section'><h2>Special Attractions</h2></div>", unsafe_allow_html=True)

st.markdown("<p class='highlight'>Live Music, Food Stalls, Dance Shows, and Games!</p>", unsafe_allow_html=True)

# -------------------------
# Event Schedule
# -------------------------
st.subheader("Event Schedule")

st.markdown("""
<ul>
    <li>10:00 AM - Opening Ceremony</li>
    <li>12:00 PM - Technical Workshop</li>
    <li>2:00 PM - Cultural Programs</li>
    <li>5:00 PM - Prize Distribution</li>
</ul>
""", unsafe_allow_html=True)

# -------------------------
# Footer
# -------------------------
st.success("Thank you for visiting My College Event Page!")
