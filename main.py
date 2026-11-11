from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from typing import List
from langchain.agents import create_tool_calling_agent , AgentExecutor
from tools import search_tool 

load_dotenv()

class ResearchResponse(BaseModel):
topic: str = Field(description= "The research topic")
summary: str = Field(description="Detailed, evidence-based summary")
strengths: List[str] = Field(description="Strengths identified in the research")
weaknesses: List[str] = Field(description="Weaknesses or limitations identified")
controversies: List[str] = Field(description="Controversies or debates within the field")
sources: List[str] = Field(description="List of sources used")


llm = ChatOpenAI(model = "gpt-4o")
parser = PydanticOutputParser (pydantic_object = ResearchResponse)

 system_message = """  
You are a senior academic researcher and critical analyst.
Your task is to provide detailed, objective, and evidence-based summaries of the research query.
Use formal, academic language.
Identify and evaluate both the strengths and weaknesses of the data.
Cite potential controversies, debates, or conflicting viewpoints within the field.
{format_instructions} """

prompt = ChatPromptTemplate.from_messages([
("system", system_message),
("human", "{query}")
])

chain =prompt.partial(format_instructions=parser.get_format_instructions()) | llm | parser


response = chain.invoke({"query": "The impact of AI on software engineering"})
print(response)

tools = [search_tool]
agent = create_tool_calling_agent (
 llm = llm,
 prompt = prompt, 
 tools = tools
)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose = True)
raw_response = agent_executor.invoke({"query": "The impact of AI on software engineering"})
print (raw_response)

structured_response = parser.parse (raw_response.get("output")[0]["text"])
print(structured_response)

try:
 structured response = parser.parse(raw_response.get("output")[0]["text"]
expect Exception as e:
    print(f"Error parsing response" , e, "Raw Response is - " , raw_response)
                                    
                                    )



