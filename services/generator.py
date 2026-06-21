import os
from groq import Groq


CATEGORY_MAP = {
    "winter": "winter gear",
    "cycling": "cycling gear",
    "camping": "camping gear",
    "running": "running gear",
}


def get_client():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("Missing GROQ_API_KEY")

    return Groq(api_key=api_key)


def generate_customer_output(row):

    client = get_client()

    customer = str(row["customer"]).strip()
    category = str(row["category"]).strip().lower()
    spend = float(row["spend"])

    if spend > 300:
        segment = "High Value Customer"
    elif spend > 100:
        segment = "Mid Value Customer"
    else:
        segment = "Low Value Customer"

    recommendation = CATEGORY_MAP.get(category, f"{category} gear")

    prompt = f"""
You are an AI CRM assistant for an outdoor ecommerce company.

STRICT RULES:

- Return ONLY the required output
- Do NOT add explanations
- Do NOT add notes
- EMAIL must be marketing text ONLY
- EMAIL must NEVER contain email addresses
- EMAIL must be exactly 2–3 sentences
- SUBJECT must be maximum 6 words
- Keep recommendations aligned with category
- Use concise professional marketing tone

Customer:
{customer}

Category:
{category}

Spend:
{spend}

Return EXACTLY this format:

SEGMENT: {segment}
SUBJECT: ...
EMAIL: ...
RECOMMENDATION: {recommendation}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.3,
        )

        result = response.choices[0].message.content.strip()

        lines = result.split("\n")

        updated = []

        recommendation_found = False

        for line in lines:

            if line.startswith("RECOMMENDATION:"):
                updated.append(
                    f"RECOMMENDATION: {recommendation}"
                )
                recommendation_found = True

            else:
                updated.append(line)

        if not recommendation_found:
            updated.append(
                f"RECOMMENDATION: {recommendation}"
            )

        result = "\n".join(updated)

        if "@" in result:
            result = result.replace("@", "")

        return result

    except Exception as e:

        return f"""SEGMENT: {segment}
SUBJECT: Special Offer For You
EMAIL: Hi {customer}, explore our latest outdoor collection selected for your interests.
RECOMMENDATION: {recommendation}
ERROR: {str(e)}"""