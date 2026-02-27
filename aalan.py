import os
from crewai import Agent, Task, Crew, Process, LLM

# 1. Setup your API Key
# שינינו את השם של המשתנה ל-GEMINI_API_KEY כדי ש-CrewAI יזהה אותו בוודאות
os.environ["GEMINI_API_KEY"] = "AIzaSyDplImZx4POLR45uCOo3cHc-QhGHx4Kw9k"

# 2. Define the Gemini Model
# שדרגנו למודל 2.5 שהוא עדכני, מהיר יותר וחינמי
gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    temperature=0.7
)

# 3. Defining Agents
researcher = Agent(
    role='Tech Trends Researcher',
    goal='Identify the top 3 AI trends for 2026',
    backstory='You are a specialist in emerging technologies with a focus on AI productivity.',
    llm=gemini_llm,
    verbose=True
)

writer = Agent(
    role='Professional Blogger',
    goal='Write a catchy LinkedIn post about the AI trends',
    backstory='You are a social media expert who knows how to make tech news viral.',
    llm=gemini_llm,
    verbose=True
)

# 4. Defining Tasks
task1 = Task(
    description="Research and list the 3 most important AI trends of 2026.",
    expected_output="A bullet-point list of 3 trends with a brief explanation for each.",
    agent=researcher
)

task2 = Task(
    description="Based on the research, write a LinkedIn post that is engaging and professional.",
    expected_output="A LinkedIn post including emojis and hashtags.",
    agent=writer
)

# 5. Forming the Crew and Starting
my_crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    process=Process.sequential
)

print("### Crew is starting the mission... ###")
result = my_crew.kickoff()

print("\n\n########################")
print("## FINAL OUTPUT ##")
print("########################\n")
print(result)