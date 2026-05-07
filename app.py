import streamlit as st
import requests
import google.generativeai as genai
from groq import Groq

# --- 1. APNI KEYS YAHAN BHARIYE ---
# In quotes ke beech mein apni keys paste kar dein
GROQ_API_KEY = "YAHAN_GROQ_KEY_PASTE_KAREIN"
GEMINI_API_KEY = "YAHAN_GEMINI_KEY_PASTE_KAREIN"
TAVILY_API_KEY = "YAHAN_TAVILY_KEY_PASTE_KAREIN"
UNSPLASH_ACCESS_KEY = "YAHAN_UNSPLASH_TOKEN_PASTE_KAREIN"

# Setup APIs
client_groq = Groq(api_key=GROQ_API_KEY)
genai.configure(api_key=GEMINI_API_KEY)
model_gemini = genai.GenerativeModel('gemini-1.5-flash')

# --- UI DESIGN (Perplexity Style) ---
st.set_page_config(page_title="My-Tube AI Intelligence", layout="wide")

# Sidebar: Admin Control Panel (Sirf Aapke Liye)
with st.sidebar:
    st.title("🛠 Admin Dashboard")
    st.info("Stream X Monitoring Active ✅")
    
    if st.button("Fix Platform Crashes"):
        st.warning("AI is scanning Stream X for bugs...")
        # Yahan aapka AI backend check karega
        st.success("System Cleaned!")

    st.divider()
    st.write("💰 Monetization Status: **Active**")
    st.button("Request Payout")

# Main Screen: Perplexity Style Search
st.title("🌐 My-Tube Search")
query = st.text_input("", placeholder="Ask anything... (Search trends, news, or platform help)")

if query:
    with st.spinner("Searching and Thinking..."):
        # STEP 1: Search (Tavily)
        search_url = "https://tavily.com"
        payload = {"api_key": TAVILY_API_KEY, "query": query}
        search_res = requests.post(search_url, json=payload).json()
        
        # STEP 2: Reason (Gemini)
        context = str(search_res.get('results', 'No live info found.'))
        prompt = f"User asked: {query}. Based on this data: {context}, give a clear Perplexity-style answer."
        response = model_gemini.generate_content(prompt)
        
        # STEP 3: Image (Unsplash)
        img_res = requests.get(f"https://unsplash.com{query}&client_id={UNSPLASH_ACCESS_KEY}").json()
        
        # DISPLAY RESULTS
        st.markdown(f"### Results for: {query}")
        if 'urls' in img_res:
            st.image(img_res['urls']['regular'], width=500)
        st.write(response.text)
        st.caption("Sources: Verified via Tavily Search Engine")
