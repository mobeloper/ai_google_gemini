import os
import streamlit as st
from vertexai.preview.generative_models import GenerativeModel
import vertexai
import logging
from google.cloud import logging as cloud_logging
from PIL import Image

from app_tab1 import render_story_tab
from app_tab2 import render_mktg_campaign_tab
from app_tab3 import render_image_playground_tab
from app_tab4 import render_video_playground_tab

# configure logging
logging.basicConfig(level=logging.INFO)
# attach a Cloud Logging handler to the root logger
log_client = cloud_logging.Client()
log_client.setup_logging()

PROJECT_ID = os.environ.get('PROJECT_ID')   # Your Qwiklabs Google Cloud Project ID
LOCATION = os.environ.get('REGION')         # Your Qwiklabs Google Cloud Project Region
vertexai.init(project=PROJECT_ID, location=LOCATION)

@st.cache_resource
def load_models():
    text_model_pro = GenerativeModel("gemini-pro")
    multimodal_model_pro = GenerativeModel("gemini-pro-vision")
    return text_model_pro, multimodal_model_pro


im_logo = Image.open("./assets/logo.ico")

st.set_page_config(
    page_title="SamurAI",
    page_icon=im_logo,
    layout="centered",
)


# st.title("🤓 🥷:ninja: ⚔️ _SamurAI_", anchor='#title', help=None)
st.header(':ninja: SamurAI', divider='rainbow')
# st.header("_NoBrainer_ - Multimodal AI with Google Gemini API")
# st.subheader('Multimodal AI with Google Gemini API', divider='rainbow')


# st.write("Multimodal AI Platform for Automated Content Generation")

text_model_pro, multimodal_model_pro = load_models()

tab1, tab2, tab3, tab4 = st.tabs(["Story Maker", "Marketing Campaign", "Image Vision", "Video Vision"])

with tab1:
    render_story_tab(text_model_pro)


with tab2:
    render_mktg_campaign_tab(text_model_pro)
    
with tab3:
    render_image_playground_tab(multimodal_model_pro)

with tab4:
    render_video_playground_tab(multimodal_model_pro)
