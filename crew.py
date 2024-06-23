from crewai import Crew, Process
from tasks import research_task, write_task
from agents import healthcare_researcher, healthcare_writer

crew = Crew(
    agents=[healthcare_researcher, healthcare_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
)

# Example input for generating a healthcare article
result = crew.kickoff(inputs={'topic': 'i am feeling headache from 3 days'})
print(result)
