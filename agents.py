from crewai import Agent
from tools import google_search_tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# Call the Gemini models
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose=True,
                             temperature=0.5,
                             google_api_key=os.getenv("GOOGLE_API_KEY"))

# Creating a healthcare researcher agent with memory and verbose mode
healthcare_researcher = Agent(
    role="Healthcare Researcher",
    goal='Discover, verify, and compile safe and effective home remedies for {topic}.',
    verbose=True,
    memory=True,
    backstory=(
        "As a seasoned healthcare professional with a deep understanding of "
        "traditional and modern remedies, your mission is to uncover reliable "
        "and practical information that can improve daily life. Your approach "
        "is meticulous, ensuring all recommendations are safe, effective, and "
        "backed by credible sources."
    ),
    tools=[google_search_tool],
    llm=llm,
    allow_delegation=True
)

# Creating a healthcare writer agent responsible for writing detailed articles
healthcare_writer = Agent(
    role='Content Writer',
    goal='Create engaging, informative, and well-structured articles on {topic} that educate and empower readers.',
    verbose=True,
    memory=True,
    backstory=(
        "With extensive experience in health journalism and a talent for making "
        "complex information accessible, your writing captivates and informs. "
        "You transform research findings into compelling narratives that are easy "
        "to read and trustworthy, ensuring readers are well-informed and confident "
        "in applying the knowledge."
    ),
    tools=[],
    llm=llm,
    allow_delegation=False
)
