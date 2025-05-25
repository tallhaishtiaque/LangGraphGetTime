import os
from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

import datetime
from langchain.chat_models import init_chat_model
from langchain_core.tools import tool


class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)


llm = init_chat_model("google_genai:gemini-2.0-flash")


@tool
async def get_current_time() -> dict:
    """Return current UTC time in ISO-8601 format. Example → {'utc': '2025-05-21T06:42:00Z'}"""

    now = datetime.datetime.now(datetime.timezone.utc)
    time = {"utc": now.strftime("%Y-%m-%dT%H:%M:%SZ")}
    return time


tools = [get_current_time]
llm_with_tools = llm.bind_tools(tools)



def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

graph_builder.add_node("chatbot", chatbot)

tool_node = ToolNode(tools=tools)
graph_builder.add_node("tools", tool_node)

graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)
# Any time a tool is called, we return to the chatbot to decide the next step
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")
graph = graph_builder.compile()