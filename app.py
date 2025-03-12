import streamlit as st

st.markdown(
    """
    <style>
    body{
        background-color:rgb(7, 7, 7);
        color: white;
    }

    .stApp{
        background: linear-gradient(135deg,hsl(188, 21.20%, 79.60%),rgb(79, 72, 109));
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgb(7, 7, 7);
    }
    h1{
        text-align: center;
        font-size: 36px;
        color: white;
    }

    .stButton>button{
        background: linear-gradient(135deg,rgb(29, 28, 27),rgb(110, 95, 167));
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }

    .stButton>button:hover{
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black;
    }

    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: hsl(187, 40.50%, 61.80%);
        padding: 15px;
        color: rgb(245, 205, 30);
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgb(31, 39, 41);
    }
    
    .footer{
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description 
st.markdown("<h1>Unit Converter using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write("Convert between different units of length, weight, and temperature.")

# Sidebar menu
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000,
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28084, 'Inches': 39.3701
    }
    return (value / length_units[from_unit]) * length_units[to_unit]


def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilograms': 1, 'Grams': 1000, 'Milligrams': 1000000, 'Pounds': 2.20462, 'Ounces': 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]


def temperature_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":  # Fixed condition
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value

# Conversion button
if st.button("Convert"):
    result = None
    if conversion_type == "Length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temperature_converter(value, from_unit, to_unit)

    if result is not None:
        st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>Created with Love by Izma Sadiq</div>", unsafe_allow_html=True)
