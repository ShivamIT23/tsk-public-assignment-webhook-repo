from app.webhook import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render-assigned port
    app.run(debug=True, host="0.0.0.0", port=port)  # Bind to all interfaces