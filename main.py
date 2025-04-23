import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

# Add custom background color
st.markdown("""
    <style>
        .stApp {
            background-color: aliceblue;
            button{
                background-color: #000000;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
            }
            
        }
            st.title{
                color: #000000;
                font-size: 40px;
                font-weight: bold;
                text-align: center;
                font-family: 'Arial black', sans-serif;
                text-transform: uppercase;
        
                
            }
    </style>
""", unsafe_allow_html=True)

# Load environment variables
load_dotenv()
client = Groq(
    api_key=os.environ.get("api"),
)

# Streamlit UI
st.title("AI AJAY EDUCATION")

# Create a selectbox for choices
choice = st.selectbox(
    "Choose your quiz domain:",
    ["geography", "economics", "general knowledge"]
)

# Create a text input for user question
user_input = st.text_input("Enter your Question:")

# Create a submit button    
if st.button("submit",):

    if user_input:
        if choice == "geography":
            text = f"you are a geography expert AI assistant. you task is to provide accurate and insightful response to the following user related to geography: {user_input}. for any other topic, respond 'I don't know.'"
        elif choice == "economics":
            text = f"you are a economics expert AI assistant. you task is to provide accurate and insightful response to the following user related to economics: {user_input}. for any other topic, respond 'I don't know.'"
        elif choice == "general knowledge":
            text = f"you are a general knowledge expert AI assistant. you task is to provide accurate and insightful response to the following user related to general knowledge: {user_input}. for any other topic, respond 'I don't know.'"
        elif choice == "computer programming":
            text = f"you are a computer programming expert AI assistant. you task is to provide accurate and insightful response to the following user related to computer programming: {user_input}. for any other topic, respond 'I don't know.'"

        # Get response from Groq
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": text,
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        
        # Display the response
        st.write("Response:")
        st.write(chat_completion.choices[0].message.content)
