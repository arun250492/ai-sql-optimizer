from flask import Flask, request, jsonify
import gradio as gr
from agent import SQLAgent

app = Flask(__name__)
sql_agent = SQLAgent()

def process_query(query):
    response = sql_agent.analyze_and_optimize(query)
    return response

iface = gr.Interface(fn=process_query, 
                     inputs="text", 
                     outputs="text", 
                     title="AI SQL Query Optimizer",
                     description="Enter your SQL or PL/SQL query to analyze and optimize it.")

if __name__ == "__main__":
    iface.launch()