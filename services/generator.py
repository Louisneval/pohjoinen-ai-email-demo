import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_customer_output(row):

    spend = float(row["spend"])

    if spend > 300:
        segment = "High Value Customer"
    elif spend > 100:
        segment = "Mid Value Customer"
    else:
        segment = "Low Value Customer"

    prompt = f"""
You are an AI CRM assistant for an outdoor ecommerce company.

Rules:
- Return ONLY structured output
- EMAIL must be marketing text (NOT email address)
- RECOMMENDATION must be one of: winter gear, cycling gear, camping gear, running gear

Customer data:
Name: {row['customer']}
Category: {row['category']}
Spend: {spend}

Output format:
SEGMENT: {segment}
SUBJECT: short engaging subject (max 6 words)
EMAIL: 2-3 sentence personalized marketing message referencing spend or category
RECOMMENDATION: matching product category
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"""SEGMENT: {segment}
SUBJECT: Special Offer for You
EMAIL: Hi {row['customer']}, we have curated outdoor deals based on your activity.
RECOMMENDATION: {row['category']}
ERROR: {str(e)}"""