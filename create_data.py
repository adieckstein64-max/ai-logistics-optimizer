import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import FileReadTool

# --- 1. SETTINGS & DB CONNECTION (SQLAlchemy) ---
DB_USER = "root"
DB_PASS = "Adieck642001!" # עודכן עם הסיסמה שלך
DB_HOST = "localhost"
DB_NAME = "logistics_db"

# חיבור מקצועי שמונע אזהרות
engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}")

try:
    df = pd.read_sql("SELECT * FROM inventory", engine)
    print("Step 1: Professional SQL Connection Successful.")
except Exception as e:
    print(f"Error connecting to MySQL: {e}")
    exit()

# --- 2. ADVANCED ENGINEERING CALCULATIONS ---
# מקדם רמת שירות ל-95%
Z = 1.65
# הערכת סטיית תקן של הביקוש (20% מהממוצע)
df['Demand_Std_Dev'] = df['Daily_Demand_Avg'] * 0.2

# חישוב מלאי ביטחון: Safety Stock = Z * StdDev * sqrt(LeadTime)
df['Safety_Stock'] = np.ceil(Z * df['Demand_Std_Dev'] * np.sqrt(df['Lead_Time_Days']))

# נקודת הזמנה מעודכנת (ROP) כולל מלאי ביטחון
df['Reorder_Point'] = (df['Daily_Demand_Avg'] * df['Lead_Time_Days']) + df['Safety_Stock']
df['Stock_Status'] = np.where(df['Current_Stock'] < df['Reorder_Point'], 'Restock', 'OK')

# ניתוח ערך מלאי וסיווג ABC הנדסי
df['Inventory_Value'] = df['Current_Stock'] * df['Unit_Cost']
df['ABC_Class'] = np.where(df['Inventory_Value'] > 5000, 'A',
                  np.where(df['Inventory_Value'] > 2000, 'B', 'C'))

# שמירה לקובץ עבור סוכני ה-AI
df.to_csv('logistics_data_advanced.csv', index=False)

# --- 3. UPDATED GRAPH (Matplotlib) ---
plt.figure(figsize=(12, 6))
plt.bar(df['Product_Name'], df['Current_Stock'], label='Current Stock', color='#3498db', alpha=0.7)
plt.step(df['Product_Name'], df['Reorder_Point'], where='mid', label='ROP (incl. Safety Stock)', color='#e74c3c', linestyle='--')

plt.title('Advanced Inventory Control: Safety Stock & ROP Analysis')
plt.ylabel('Units')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.savefig('advanced_inventory.png')
print("Step 2: Engineering Graph Saved as 'advanced_inventory.png'.")

# --- 4. STRATEGIC AI ANALYSIS (Groq) ---
os.environ["GROQ_API_KEY"] = "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"
groq_llm = LLM(model="groq/llama-3.3-70b-versatile", temperature=0.1)
file_tool = FileReadTool(file_path='logistics_data_advanced.csv')

# בניית צוות המנהלים
analyst = Agent(
    role='Industrial Engineer',
    goal='Optimize inventory using Safety Stock logic',
    backstory='Expert in supply chain optimization from Afeka College.',
    tools=[file_tool],
    llm=groq_llm
)

cfo = Agent(
    role='CFO',
    goal='Approve procurement budget based on ROI',
    backstory='Corporate finance expert focused on inventory turnover.',
    llm=groq_llm
)

t1 = Task(description="Analyze stock levels vs ROP and explain the importance of Safety Stock for the restock items.", expected_output="Technical logistics report.", agent=analyst)
t2 = Task(description="Provide final budget approval and a summary of Class A inventory value.", expected_output="Financial approval statement.", agent=cfo, context=[t1])

crew = Crew(agents=[analyst, cfo], tasks=[t1, t2])
result = crew.kickoff()

print("\n### STRATEGIC FINAL REPORT ###\n")
print(result)
plt.show()