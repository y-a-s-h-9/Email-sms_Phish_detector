import streamlit as st
import pickle
import string
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import ssl
import time

# SSL workaround
try:
    _create_unverified_https_context = ssl._create_unverified_context
    ssl._create_default_https_context = _create_unverified_https_context
except AttributeError:
    pass

# Download stopwords
nltk.download('stopwords')

# Initialize stemmer
ps = PorterStemmer()

# Check for suspicious links
def is_suspicious_link(word):
    suspicious_keywords = ['free', 'win', 'prize', 'claim', 'click', 'offer', '$', 'cash', 'urgent', 'limited', 'risk-free', 'guaranteed']
    suspicious_tlds = ['xyz', 'top', 'tk', 'gq', 'ml', 'cf']
    if any(tld in word for tld in suspicious_tlds) or any(keyword in word for keyword in suspicious_keywords):
        return True
    return False

# Preprocessing function
def transform_text(text):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    cleaned = []
    suspicious = False
    for word in words:
        if word not in stopwords.words('english') and word not in string.punctuation:
            if is_suspicious_link(word):
                cleaned.append('suspicious_link_detected')
                suspicious = True
            elif ('http' in word) or ('www' in word) or ('.com' in word) or ('.in' in word):
                cleaned.append('link_detected')
            else:
                cleaned.append(ps.stem(word))
    return " ".join(cleaned), suspicious

# Load model
try:
    with open('vectorizer.pkl', 'rb') as f:
        tfidf = pickle.load(f)
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"❌ Error loading model files: {e}")
    st.stop()

# ------------------------ Streamlit UI ------------------------

# Page config
st.set_page_config(page_title="Spam Detector", page_icon="📩", layout="wide")

# CSS for Dark Mode (without affecting button)
st.markdown("""
    <style>
    body {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    .stTextArea textarea {
        background-color: #262730;
        color: #FFFFFF;
        border: 1px solid #5c5c5c;
    }
    .big-font {
        font-size:50px !important;
        text-align: center;
        color: #FF4B4B;
        font-weight: bold;
    }
    .card {
        background: #1E2127;
        padding: 2em;
        border-radius: 15px;
        box-shadow: 0px 4px 20px rgba(255,255,255,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("ℹ️ About")
    st.write("""A simple, powerful app to detect **Spam** or **Safe** messages using Machine Learning. """)
    st.markdown("---")

# Header
st.markdown('<p class="big-font">🚨 Spam Message Detector 🚨</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter a message and check if it's spam instantly!</p>", unsafe_allow_html=True)

st.markdown("---")

# Card for input
with st.container():
    input_sms = st.text_area("✉️ Enter your message here:", height=200)
    col1, col2, col3 = st.columns([3,2,2])
    with col2:
        predict_btn = st.button('🔍 Predict')

# Prediction logic
if predict_btn:
    if input_sms.strip() == "":
        st.warning("⚠️ Please enter a message before predicting.")
    else:
        with st.spinner('Analyzing... Please wait ⏳'):
            time.sleep(1.5)  # simulate loading time

            # Preprocess
            transformed_sms, suspicious_flag = transform_text(input_sms)

            # Vectorize
            vector_input = tfidf.transform([transformed_sms])

            # Predict
            result = model.predict(vector_input)[0]

            st.markdown('<div class="card">', unsafe_allow_html=True)

            # Show result
            if result == 1 or suspicious_flag:
                st.error("🚨 Spam Detected! This message is highly suspicious.")
            else:
                st.success("✅ Safe: This message is likely not spam.")
            
            # Expandable preprocessed text
            with st.expander("🔍 See Preprocessed Text"):
                st.info(transformed_sms)

            st.markdown('</div>', unsafe_allow_html=True)
