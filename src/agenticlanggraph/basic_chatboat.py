import os
from dotenv import load_dotenv
load_dotenv()
from typing_extensions import Annotated, TypedDict
from  langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages
from langchain_groq import ChatGroq
from langchain.chat_models import init_chat_model
llm=init_chat_model(
     model="openai/gpt-oss-120b",)


class State(TypedDict):
    messages:Annotated[list,add_messages]

graph_builder=StateGraph(State)
