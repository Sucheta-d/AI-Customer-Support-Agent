# Backend/agents/refund_agent.py

import os
from dotenv import load_dotenv

from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

#################################################
# LLM
#################################################

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0
)

#################################################
# Structured Output Schema
#################################################

class RefundDecision(BaseModel):
    decision: str = Field(
        description="Either APPROVED or DENIED or NEED HUMAN INTERVENTION"
    )

    reason: str = Field(
        description="Short explanation of the decision"
    )

#################################################
# Structured LLM
#################################################

structured_llm = llm.with_structured_output(
    RefundDecision
)

#################################################
# Prompt
#################################################

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI Customer Support Agent.

Your job is to decide whether a refund should be APPROVED or DENIED.

You MUST:
1. Follow the refund policy strictly.
2. Consider the customer's stated reason.
3. Deny refunds if fraud_flag=True.
4. Return a structured response.
"""
        ),
        (
            "human",
            """
Refund Policy:
{policy}

Customer Information:
{customer}

Order Information:
{order}

Customer Refund Reason:
{refund_reason}
"""
        )
    ]
)

#################################################
# Chain
#################################################

refund_chain = prompt | structured_llm