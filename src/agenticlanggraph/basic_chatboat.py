import os
from dotenv import load_dotenv
load_dotenv()
from typing_extensions import Annotated, TypedDict
from  langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages

class State(TypedDict):
    messages:Annotated[list,add_messages]

graph_builder=StateGraph(State)
