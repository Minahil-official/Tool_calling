from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the GOOGLE_API_KEY from the environment
GOOGLE_api_key = os.getenv("GOOGLE_API_KEY")


# Check if the API key is loaded correctly
if GOOGLE_api_key:
    print(f"Your API Key is found")
else:
    print("API Key is not found. Please check your .env file.")

from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
import streamlit as st

@tool
def multiply(a: int, b: int) -> int:
    """Multiply a and b."""
    print("function is called")
    return a * b

tools = [multiply]

llm = ChatGoogleGenerativeAI(model = "gemini-2.0-flash-exp" , api_key=GOOGLE_api_key)
agent = initialize_agent(tools, llm , agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION )

st.title("TOOL CALLING")
st.write("welcome to my app")
user_input = st.text_input("enter your prompt")

 
 
if st.button("Submit", key="process_data"):
    response = agent.invoke(user_input)
    st.write(response)
