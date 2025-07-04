import os
from dotenv import load_dotenv

load_dotenv()

from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from datetime import datetime
from flask import send_from_directory

print("Current working directory:", os.getcwd())
webhook_bp = Blueprint("webhook", __name__)

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["webhook_db"]
events_collection = db["events"]

@webhook_bp.route("/", methods=["GET"])
def home():
    return "Webhook Server is Running 🚀"


@webhook_bp.route("/events-ui")
def frontend():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../frontend"))
    return send_from_directory(base_dir, "index.html")

@webhook_bp.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    event_type = request.headers.get("X-GitHub-Event")
    timestamp = datetime.utcnow().isoformat() + "Z"
    author = data.get("sender", {}).get("login", "Unknown")

    if event_type == "push":
        to_branch = data.get("ref", "").split("/")[-1]
        event = {
            "type": "push",
            "author": author,
            "from_branch": None,
            "to_branch": to_branch,
            "timestamp": timestamp
        }
        events_collection.insert_one(event)

    elif event_type == "pull_request":
        pr_action = data.get("action")
        pr = data.get("pull_request", {})
        from_branch = pr.get("head", {}).get("ref")
        to_branch = pr.get("base", {}).get("ref")

        if pr_action == "opened":
            event = {
                "type": "pull_request",
                "author": author,
                "from_branch": from_branch,
                "to_branch": to_branch,
                "timestamp": timestamp
            }
            events_collection.insert_one(event)

        elif pr_action == "closed" and pr.get("merged") is True:
            event = {
                "type": "merge",
                "author": author,
                "from_branch": from_branch,
                "to_branch": to_branch,
                "timestamp": timestamp
            }
            events_collection.insert_one(event)

    return jsonify({"status": "received"}), 200

@webhook_bp.route("/events", methods=["GET"])
def get_events():
    events = list(events_collection.find().sort("_id", -1).limit(10))
    for e in events:
        e["_id"] = str(e["_id"])
    return jsonify(events)
