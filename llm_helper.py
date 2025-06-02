from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()


llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama3-8b-8192")

if __name__ == "__main__":
    response = llm.invoke("What's bigger? brain or bull? ")
    print(response.content)
