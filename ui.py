import streamlit as st
import requests
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()

st.title("🧠 PyTorch Image Classifier")

uploaded_file = st.file_uploader("Upload an image")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    if st.button("Predict"):
        with st.spinner("Predicting..."):
            files = {"file": uploaded_file.getvalue()}

            # chain_response = crop_or_not(image)
            # result = str(chain_response.content).strip().lower()
            # if result == "false":
            #     st.error("The image does not contain a crop.")
            # else:
            #     st.success("The image contains a crop.")

            response = requests.post("http://127.0.0.1:8000/predict", files=files)
            print(response)
            response = response.json()
            if response['result'] == False:
                st.error(response['message'])
            else:
                result = response
                st.success(f"Predicted Crop: {result['crop']}, Disease: {result['disease']}")

                suggestions_response = response.post(f"http://127.0.0.1:8000/suggestions/English/{result['crop']}/{result['disease']}",)
