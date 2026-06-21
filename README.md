# 📧 AI CRM Email Personalization Tool (Pohjoinen Case Study)

## Overview

This project is an AI-powered CRM automation tool built for Pohjoinen, an outdoor ecommerce company in Finland.

The system automatically generates customer segmentation, personalized marketing emails, and product recommendations using AI.

It is designed to simulate how modern ecommerce companies can scale marketing operations using LLMs.

---

## Business Problem

Pohjoinen has:

- 180,000+ customers
- 8,000 products
- highly seasonal demand (winter, camping, cycling, running)

Marketing teams currently spend a lot of time manually:

- writing email campaigns
- segmenting customers
- selecting product recommendations

This process is slow, repetitive, and does not scale.

---

## Solution

This project automates CRM marketing workflows using AI.

The system:

- reads customer data from CSV
- analyzes spending and category
- generates customer segments
- creates personalized marketing emails
- recommends product categories

All outputs are generated automatically using a Large Language Model.

---

## AI Model

The system uses Groq API with:

- model: llama-3.1-8b-instant

The model is responsible for:

- natural language generation
- marketing copy creation
- customer personalization
- segmentation logic

---

## Tech Stack

- Python
- Streamlit
- Groq API
- Pandas
- python-dotenv

---

## Project Structure

app.py → Streamlit frontend  
services/generator.py → AI generation logic  
utils/prompts.py → prompt templates  
data/customers.csv → sample dataset  
requirements.txt → dependencies  
.gitignore → ignored files configuration  

---

## How It Works

1. User uploads a CSV file with customer data
2. The system reads each customer row
3. AI processes:
   - customer name
   - category
   - spend
4. AI returns:
   - segment
   - subject line
   - personalized email
   - product recommendation
5. Results are displayed in a web UI

---

## Input Format (CSV)

The file must contain:

customer,category,spend

Example:

Anna,winter,480  
Mark,cycling,120  
Emma,camping,700  
Leo,running,90  

---

## Output Format

For each customer the system generates:

SEGMENT: High Value Customer  
SUBJECT: Upgrade Your Winter Gear  
EMAIL: Personalized marketing message based on customer behavior  
RECOMMENDATION: winter gear  

---

## Setup Instructions

### 1. Clone repository

git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git  
cd YOUR_REPO  

---

### 2. Create virtual environment

python -m venv venv  
source venv/bin/activate (Mac/Linux)  
venv\Scripts\activate (Windows)  

---

### 3. Install dependencies

pip install -r requirements.txt  

---

### 4. Get API Key

Go to:

https://console.groq.com

Create an account and generate an API key.

---

### 5. Create environment file

Create a file named .env in the project root:

GROQ_API_KEY=your_api_key_here  

---

### 6. Run the app

streamlit run app.py  

Open:

http://localhost:8501  

---

## Features

- AI-powered customer segmentation
- Automated email generation
- Product recommendation engine
- CSV batch processing
- Simple web interface

---

## Business Value

This system helps ecommerce teams:

- scale personalization to 180,000+ users
- reduce manual CRM workload
- improve email marketing performance
- react faster to seasonal demand
- increase customer engagement

---

## Deployment

This project can be deployed using Streamlit Cloud.

Steps:

1. Push code to GitHub
2. Go to https://streamlit.io/cloud
3. Connect repository
4. Select app.py as entry point

Add API key in Streamlit Secrets:

GROQ_API_KEY = "your_api_key_here"

---

## Future Improvements

- integration with Klaviyo
- A/B testing for email subject lines
- advanced customer segmentation models
- automated campaign scheduling
- multi-model AI comparison

---

## Summary

This project demonstrates how AI can automate CRM marketing workflows in ecommerce by combining customer data with large language models to generate personalized content at scale.
