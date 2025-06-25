from flask import Flask, request, jsonify
import gradio as gr
from agent import SQLAgent
from dotenv import load_dotenv

load_dotenv(override=True)
app = Flask(__name__)
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Make sure to set this environment variable
sql_agent = SQLAgent(OPENAI_API_KEY=OPENAI_API_KEY)

def process_query(query):
    response = sql_agent.optimize_query(query)
    return response

iface = gr.Interface(fn=process_query, 
                     inputs="text", 
                     outputs="text", 
                     title="AI SQL Query Optimizer",
                     description="Enter your SQL or PL/SQL query to analyze and optimize it.")

if __name__ == "__main__":
    iface.launch()
