# 📧 AI CRM Email Personalization Tool (Pohjoinen Case Study)

## 🚀 Overview

This project is an AI-powered CRM automation tool built for **Pohjoinen**, an outdoor ecommerce company in Finland.

It simulates a real marketing workflow where AI automatically:

- Segments customers based on purchase behavior
- Generates personalized marketing emails
- Recommends product categories
- Reduces manual CRM workload

The goal is to demonstrate how AI can scale marketing operations without increasing team size.

---

## 🎯 Business Problem

Pohjoinen has:

- 180,000+ customers
- 8,000 products
- strong seasonal demand (winter, camping, cycling, running)

### Current issue:

Marketing team manually handles:

- email writing
- segmentation
- product targeting
- campaign personalization

This results in:

- slow campaign production
- low personalization
- missed seasonal opportunities
- high operational workload

---

## 💡 AI Solution

This tool automates the entire CRM content pipeline using AI:

### What it does:

1. Reads customer data (CSV)
2. Analyzes spend & category
3. Uses an LLM (Groq / Llama 3) to:
   - assign customer segment
   - generate marketing email
   - suggest product category

---

## 🧠 AI Model Used

- Groq API
- Model: `llama-3.1-8b-instant`
- Used for:
  - natural language generation
  - personalization
  - marketing copy creation

---

## 🛠 Tech Stack

- Python
- Streamlit (UI)
- Groq API (LLM inference)
- Pandas (data processing)
- dotenv (environment variables)

---

## 📂 Project Structure
