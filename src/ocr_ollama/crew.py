# src/ocr_ollama/crew.py

from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class InvoiceExtractionCrew():
    """OCR + Invoice Field Extraction Crew"""
    agents: List[BaseAgent]
    tasks: List[Task]
    ocr_text: str  # ✅ Dynamic input for OCR text

    @agent
    def invoice_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['invoice_agent'],
            verbose=True,
        )

    @task
    def extract_invoice_data(self) -> Task:
        task_template = self.tasks_config['extract_invoice_data']
        description = task_template['description'].format(ocr_text=self.ocr_text)

        return Task(
            description=description,
            expected_output=task_template['expected_output'],
            agent=self.invoice_agent(),
            output_file='BILL_INFO.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
