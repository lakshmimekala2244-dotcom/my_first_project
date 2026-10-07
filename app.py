import streamlit as st

st.set_page_config(
    page_title="Lakshmi Currency Converter",
    page_icon="💱"
)

st.title("💱 Lakshmi Currency Converter")
st.write("Convert an amount between different currencies.")

amount = st.number_input(
    "Enter Amount",
    min_value=0.0,
    value=100.0
)

from_currency = st.selectbox(
    "From Currency",
    ["USD", "INR", "EUR", "GBP"]
)

to_currency = st.selectbox(
    "To Currency",
    ["INR", "USD", "EUR", "GBP"]
)

# Example fixed exchange rates
rates = {
    "USD": {"INR": 83.0, "EUR": 0.92, "GBP": 0.79, "USD": 1.0},
    "INR": {"USD": 0.012, "EUR": 0.011, "GBP": 0.0095, "INR": 1.0},
    "EUR": {"USD": 1.09, "INR": 90.0, "GBP": 0.86, "EUR": 1.0},
    "GBP": {"USD": 1.27, "INR": 105.0, "EUR": 1.16, "GBP": 1.0}
}

if st.button("Convert 💱"):
    result = amount * rates[from_currency][to_currency]

    st.success(
        f"{amount:.2f} {from_currency} = "
        f"{result:.2f} {to_currency}"
    )