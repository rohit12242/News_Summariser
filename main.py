# main.py
import os
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from tools import search_news

load_dotenv()

# LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Tools
tools = [search_news]

# Agent
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

if __name__ == "__main__":
    goal = input("Enter your goal: ")
    result = agent.invoke(goal)
    print("\nFinal Output:\n", result)
