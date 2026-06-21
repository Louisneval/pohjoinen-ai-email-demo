# AI CRM Email Personalization Tool

## Overview
This project is an AI-powered CRM automation tool built for Pohjoinen, an outdoor ecommerce company.

It generates:
- Customer segmentation
- Personalized marketing emails
- Product recommendations

## Problem
Marketing team manually creates:
- email campaigns
- segmentation
- product targeting

This is slow and not scalable for 180,000 users.

## Solution
AI system using:
- Groq LLM (llama-3.1-8b-instant)
- Streamlit UI
- CSV-based customer input

## Features
- Upload customer CSV
- Automatic segmentation based on spend
- AI-generated email content
- Product recommendations
- Export results

## Tech Stack
- Python
- Streamlit
- Groq API
- Pandas

## AI Role
LLM is used for:
- natural language generation
- personalization
- marketing copy creation

## How to run

```bash
pip install -r requirements.txt
streamlit run app.py