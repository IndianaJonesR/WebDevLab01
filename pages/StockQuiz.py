import streamlit as st
import openai
import os


# Load environment variables from .env file
load_dotenv()


st.title("Stock Investment Quiz 📊")

st.write("Answer these 5 quick questions, and we'll generate a personalized investment summary for you!")


progress = 0
increment = 20


age = st.number_input("What is your age?", min_value=10, max_value=100, step=1)  #NEW
if age:
    progress += increment


goals = st.radio(
    "What’s your primary investment goal?",
    ["Growth", "Income", "Capital Preservation", "Speculative"]  #NEW
)
if goals:
    progress += increment


risk = st.slider("On a scale of 1-10, what’s your risk tolerance?", 1, 10, 5) 
if risk:
    progress += increment


industries = st.multiselect(
    "Which industries are you most interested in?",
    ["Technology", "Healthcare", "Energy", "Finance", "Real Estate", "Consumer Goods"] #NEW
)
if industries:
    progress += increment


horizon = st.selectbox(
    "What is your investment horizon?",
    ["< 1 year", "1-3 years", "3-5 years", "5+ years"]
)
if horizon:
    progress += increment


st.progress(progress) 

if st.button("Generate My Investment Summary"):
    prompt = f"""
    Based on the following quiz results, generate a concise investment summary:
    - Age: {age}
    - Goal: {goals}
    - Risk Tolerance: {risk}/10
    - Industries of Interest: {', '.join(industries)}
    - Horizon: {horizon}
    """
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        st.error("OpenAI API key not found. Please check your .env file.")
        return
    
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are a financial assistant."},
                  {"role": "user", "content": prompt}]
    )
    
    summary = response.choices[0].message.content
    st.subheader("📑 Your Investment Summary")
    st.write(summary)


st.image("Images/stocks.jpg", caption="Stock Market", use_container_width=True)
st.image("Images/finance.jpg", caption="Financial Planning", use_container_width=True)
st.image("Images/industries.jpg", caption="Different Sectors", use_container_width=True)



