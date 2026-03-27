
import streamlit as st
import requests

st.title("CodeMantra")

prompt = st.text_input("Enter your prompt")

if st.button("Generate Code"):

    res = requests.post(
        "http://127.0.0.1:8000/chat",
        params={"prompt": prompt}
    )

    data = res.json()

    if "error" in data:
        st.error(data["error"])
    else:
        

        st.subheader("AI Response")
        st.code(data["response"])
