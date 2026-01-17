AI Study Planner Agent

An adaptive Agentic AI system that dynamically plans and reallocates daily study time based on user feedback at the end of the day. 

This system operates in a multi-day loop, observing user behaviour by checking actual time taken and analyzing subject difficulty based on that and autonomously adjusting future study plans. 

Why this over a simple static planner?
This satisfies the key properties looked for in Agentic AI:

- Goal-orieneted: Optimize study time allocation
- Autonomous: Makes decisions without user telling it to do so
- Stateful: Memory maintained
- Adaptive: feedback loop works and plans changed as per it
- Temporal: Day counter given as it understands the days are changing

## System Architecture
┌───────────────┐
│ Frontend │
│ (HTML + JS) │
└───────┬───────┘
│ User Input / Feedback
▼
┌───────────────┐
│ Flask API │
│ (backend) │
└───────┬───────┘
│
▼
┌───────────────────────────┐
│ Agent Layer │
│ │
│ Planner → Analyzer → Decision
│ │
└───────────────┬───────────┘
│
▼
┌────────────────┐
│ Agent Memory │
│ (JSON files) │
│ plan.json │
│ meta.json │
│ feedback.json │
└────────────────┘

## Agent Components

### 1. Planner Agent
- Generates daily study plan and evenly distributed available hours across subjects
- Initializes agent memory

### 2. Analyzer Agent
- Compares planned vs actual daily study time and computes the difficulty score
- Higher score means subject is harder

### 3. Decision Agent
- Reallocates time based on difficulty scores and updates the plan for next day's plan.

## Multi-Day Agent Loop
Day N starts
↓
Agent provides daily plan
↓
User studies
↓
End-of-day feedback submitted
↓
Agent analyzes performance
↓
Agent updates plan
↓
days_left = days_left - 1
↓
Day N+1 starts

## Tech Stack 
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Vanilla JS
- **Agentic Logic**: Rule-based decision engine
- **Memory**: JSON files
- **Environment**: Virtualenv

