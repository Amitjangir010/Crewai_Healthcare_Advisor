from dotenv import load_dotenv
load_dotenv()
import os

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

from crewai_tools import SerperDevTool

serper_dev_tool = SerperDevTool(api_key=os.getenv('SERPER_API_KEY'))
