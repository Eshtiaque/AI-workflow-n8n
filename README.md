# 🚀 AI Article Summarizer & Analyzer Agent

A powerful, automated workflow that takes any article URL, extracts its content, analyzes it using AI (Groq + LLaMA 3), saves the insights to Google Sheets, and emails a beautifully formatted summary directly to the user.

![Project Status](https://img.shields.io/badge/Status-Completed-success)
![Version](https://img.shields.io/badge/Version-1.0.0-blue)
![Tech Stack](https://img.shields.io/badge/Tech_Stack-FastAPI_|_n8n_|_Groq_AI-purple)

## 💡 How It Works

This project consists of three main components working seamlessly together:

1.  **Frontend (HTML/Tailwind CSS):** A clean, modern UI where users input their email address and an article link.
2.  **Backend (FastAPI):** A Python server that acts as a bridge. It receives the user's data, generates a unique session ID, and triggers the n8n webhook.
3.  **Automation Engine (n8n):** The brain of the operation. It performs the following steps:
    * Receives data via **Webhook**.
    * Fetches the article content using an **HTTP Request**.
    * Sends the text to **Groq AI (LLaMA 3.3 70b)** to generate a 3-sentence summary.
    * Sends the text to Groq AI again to extract 5 key insights.
    * Appends all data (Session ID, URL, Summary, Insights, Email) to a **Google Sheet**.
    * Sends a formatted email containing the summary and insights via **Gmail**.

## 🛠️ Technology Stack

* **Frontend:** HTML5, Tailwind CSS, JavaScript (Fetch API)
* **Backend:** Python, FastAPI, Uvicorn, Requests
* **Automation:** n8n (Node-based workflow automation)
* **AI Model:** LLaMA 3.3 70b-versatile (via Groq API)
* **Integrations:** Google Sheets API, Gmail API

## 📋 Prerequisites

To run this project locally, you will need:
* Python 3.8+ installed.
* An active [n8n](https://n8n.io/) instance (Cloud or Self-hosted).
* A [Groq API Key](https://console.groq.com/keys) for AI processing.
* Google Cloud Platform credentials for Google Sheets and Gmail integrations.

## 🚀 Setup & Installation

### 1. n8n Workflow Setup
1. Open your n8n instance.
2. Go to **Workflows** -> **Add Workflow** -> **Import from file**.
3. Upload the `My workflow.json` file provided in this repository.
4. Open the workflow and configure the following credentials:
   * **HTTP Request Nodes:** Add your `Groq API Key` as a Header (`Authorization: Bearer YOUR_API_KEY`).
   * **Google Sheets Node:** Connect your Google account and select your target spreadsheet.
   * **Gmail Node:** Connect your Google account.
5. Save and **Activate** the workflow. Ensure your Webhook URL matches the one in the FastAPI code.

### 2. FastAPI Backend Setup
1. Clone this repository:
   ```bash
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
   cd your-repo-name
Install the required Python packages:

Bash
pip install fastapi uvicorn pydantic requests
Update the N8N_WEBHOOK_URL variable in main.py (or your Python file) to point to your active n8n webhook URL.

Run the FastAPI server:

Bash
uvicorn main:app --reload
The server will start at http://127.0.0.1:8000.

3. Frontend Setup
Open the index.html file in any modern web browser.

Enter an email and an article URL.

Click "Generate Analysis" and watch the magic happen!
