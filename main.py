from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch





llm = ChatOpenAI()
tools = [TavilySearch()]

agent = create_agent(model=llm, tools=tools)

def main():
    
    print("Hello from langchain-course!")
    result = agent.invoke({"messages":HumanMessage(content="search me 3 job postings for ai engineer for langgraph")})
    print(result)

if __name__ == "__main__":
    main()
