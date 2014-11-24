from aikithoughts import setup

app = setup.setup()
db = setup.db

if __name__ == "__main__":
    app.run(debug=True)