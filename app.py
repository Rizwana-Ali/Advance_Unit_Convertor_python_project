
import streamlit as st
import base64
from pint import UnitRegistry

# Set page config
st.set_page_config(page_title="UniScale - Unit Converter", layout="wide")

# Background image URL
background_image_url = "bg-image.png"

def get_base64_of_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Load and encode background image
try:
    base64_image = get_base64_of_image(background_image_url)
    bg_image_css = f"""
        <style>
        .stApp {{
            background: url('data:image/png;base64,{base64_image}') no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
    """
except FileNotFoundError:
    bg_image_css = ""  # No background if the file is missing

# Apply background image CSS
st.markdown(bg_image_css, unsafe_allow_html=True)

# Initialize unit registry
ureg = UnitRegistry()

# Title
st.markdown("<h1 style='text-align: center; color: white;'>🌍 Advanced Unit Converter ⚖️</h1>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; font-size: 1.5em; color: white;'><b>Convert any unit into different Units easily! 🚀</b></div>", unsafe_allow_html=True)

# Category selection
st.markdown("<h2 style='color: white;'>Select a Conversion Category</h2>", unsafe_allow_html=True)
categories = ["Length", "Weight", "Currency", "Temperature", "Time", "Distance", "Speed"]
category = st.selectbox("Select a category", categories)

# Functions for conversions
def convert_units(value, from_unit, to_unit):
    try:
        result = value * ureg(from_unit).to(to_unit)
        return result.magnitude
    except Exception as e:
        return f"Error: {e}"

# Handling different categories
if category == "Length":
    units = ["meter", "kilometer", "mile", "yard", "foot", "inch"]
elif category == "Weight":
    units = ["gram", "kilogram", "pound", "ounce"]
elif category == "Currency":
    st.warning("Currency conversion requires an API for real-time exchange rates.")
    units = ["USD", "EUR", "GBP", "INR", "JPY"]
elif category == "Temperature":
    units = ["celsius", "fahrenheit", "kelvin"]
elif category == "Time":
    units = ["second", "minute", "hour", "day"]
elif category == "Distance":
    units = ["meter", "kilometer", "mile", "yard", "foot"]
elif category == "Speed":
    units = ["meter/second", "kilometer/hour", "mile/hour"]
else:
    units = []

from_unit = st.selectbox("From Unit", units)
to_unit = st.selectbox("To Unit", units)
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

if st.button("Convert Now"):
    result = convert_units(value, from_unit, to_unit)
    st.markdown(f"<h3 style='color: white; text-align: center;'>Converted Value: {value} {from_unit} = {result} {to_unit}</h3>", unsafe_allow_html=True)
    st.balloons()

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>© 2025 | Developed by Rizwana Ali ⚖️ <br> 🔗 <a href='https://www.linkedin.com' target='_blank' style='color: lightblue;'>Connect on LinkedIn</a></p>", unsafe_allow_html=True)



















































































