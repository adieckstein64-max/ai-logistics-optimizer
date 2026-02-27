# AI-Powered Logistics & Inventory Optimization System

## Overview
This project implements an autonomous multi-agent system designed to optimize warehouse operations. It integrates **Industrial Engineering** principles with **Generative AI** to manage inventory levels, calculate safety stocks, and provide strategic procurement approvals.

## Key Features
- **SQL Integration**: Real-time data fetching from a MySQL database using SQLAlchemy.
- **Engineering Logic**: Automated calculation of Reorder Points (ROP) using the formula:
  $$ROP = (d \times L) + SS$$
  Where $SS$ (Safety Stock) is calculated for a 95% service level.
- **ABC Analysis**: Automated inventory classification based on value and demand.
- **Multi-Agent Orchestration**: Powered by **CrewAI** and **Groq (Llama 3)**, featuring:
  - *Logistics Analyst*: Identifies operational risks and stockouts.
  - *CFO Agent*: Provides financial oversight and budget approval.
  - *CEO Agent*: Final strategic decision-making.

## Tech Stack
- **Language**: Python
- **Database**: MySQL
- **AI Framework**: CrewAI
- **Data Science**: Pandas, Numpy, Matplotlib
- **LLM**: Groq (Llama 3.3 70b)