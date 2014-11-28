from aikithoughts import setup

app = setup.create_app()
db = setup.db

if __name__ == "__main__":
    app.run(debug=True)