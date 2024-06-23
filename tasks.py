from crewai import Task
from tools import google_search_tool
from agents import healthcare_researcher, healthcare_writer

# Research task for identifying safe home remedies
research_task = Task(
    description=(
        "Conduct thorough research to identify effective and safe home remedies for {topic}. "
        "Ensure all information is verified through credible sources and provide a detailed report. "
        "Focus on practical application, benefits, and any necessary precautions. "
        "Your findings should be comprehensive and include various perspectives."
    ),
    expected_output=(
        "A comprehensive 3-paragraph report on the best home remedies for {topic}, "
        "including practical applications, benefits, and precautions. "
        "Each paragraph should address the following: \n"
        "1. Overview of the home remedies and their general benefits.\n"
        "2. Detailed benefits of each remedy, supported by credible sources.\n"
        "3. Precautions and considerations to keep in mind while using these remedies."
    ),
    tools=[google_search_tool],
    agent=healthcare_researcher,
)

# Writing task with language model configuration for creating an article
write_task = Task(
    description=(
        "Compose an engaging and informative article on {topic}. "
        "Highlight the best home remedies, their benefits, and any precautions. "
        "Ensure the article is easy to read, informative, and trustworthy. "
        "The article should be formatted in markdown and include the following sections: \n"
        "1. **Introduction**: Briefly introduce the topic and its relevance.\n"
        "2. **Main Content**: Discuss the top home remedies in detail, their benefits, and any precautions.\n"
        "3. **Conclusion**: Summarize the key points and provide actionable advice or tips."
    ),
    expected_output=(
        "A 4-paragraph article on {topic} advancements formatted as markdown, including:\n"
        "1. **Introduction**: Setting the context and importance of the topic.\n"
        "2. **Main Content**: Detailed explanation of each home remedy, supported by credible sources.\n"
        "3. **Precautions**: Highlight any necessary precautions or side effects.\n"
        "4. **Conclusion**: Summarize the main points and offer practical advice or tips."
    ),
    tools=[],
    agent=healthcare_writer,
    async_execution=False,
    output_file='new-blog-post.md'  # Example of output customization
)
