# Dev Assessment - Webhook Receiver

This repository contains the **Flask-based webhook receiver** for GitHub events (Push, Pull Request, Merge).  
It receives GitHub webhooks, stores minimal event data to MongoDB Atlas, and exposes a UI and API to fetch the latest events.

*******************

## Setup

### 1. Clone the Repo

```bash
git clone https://github.com/ShivamIT23/tsk-public-assignment-webhook-repo.git
cd tsk-public-assignment-webhook-repo
```

### 2. Create the virtual env

```bash
pip install virtualenv
virtualenv venv
```

### 3. Activate the virtual env

```bash
source venv/bin/activate
```

### 4. Install requirements

```bash
pip install -r requirements.txt
```

### 5. 4. Create .env File

```env
MONGODB_URI=mongodb+srv://your-username:your-password@cluster.mongodb.net/webhook_db
```

## Run Locally

```bash
python run.py
```

### The endpoint is at:

* Webhook Endpoint (GitHub webhook):

```bash
POST /webhook
```

* Frontend UI (Shows latest events every 15s):

```bash
GET /events-ui
```

* API to fetch events (for polling):

```bash
GET /events
```

## ✅ Features
* Receives GitHub Push, Pull Request, and Merge events

* Stores minimal data to MongoDB Atlas

* Uses .env file for sensitive values

* Frontend polls /events every 15s

* UI displays formatted messages like:

** "Travis" pushed to "staging" on 1st April 2021 - 9:30 PM UTC

** "Travis" submitted a pull request from "dev" to "main"

** "Travis" merged branch "dev" to "main"

## 🌐 Deployment (Optional)

To deploy on Render:

1. Push this repo to GitHub

2. Create new Web Service on Render

3. Use:

    * Build Command: pip install -r requirements.txt

    * Start Command: python run.py

4. Add Environment Variable: MONGODB_URI = your-mongo-uri

5. Your Flask app will get a public URL to use as webhook

## 🔗 GitHub Webhook Setup
* Go to your action-repo → Settings → Webhooks → Add webhook

* Payload URL:

```bash
https://<your-render-or-ngrok-url>/webhook
```

* Content type: application/json

* Events: Check Push and Pull Request


## ✅ Summary
This project demonstrates real-time event tracking using Flask + MongoDB + GitHub Webhooks + Frontend polling.

Ready to deploy, test, or extend 🚀
*******************