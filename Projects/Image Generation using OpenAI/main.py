import openai
import urllib.request
from PIL import Image
import streamlit as st


openai.api_key="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"

def generateImage(description):
    response = openai.Image.create(
        prompt=description,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']

    urllib.request.urlretrieve(image_url, "image.png")

    img=Image.open("image.png")

    return img


st.title("DALL-E Image Generation using OpenAI")

title_desc=st.text_input('Enter the text to extract image')


if st.button("Show Image"):
    imagesdis = generateImage(title_desc)
    st.image(imagesdis)
