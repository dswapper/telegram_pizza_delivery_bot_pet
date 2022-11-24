import app.db
import app.telegram

def run() -> None:
    app.db.run()
    app.telegram.run()
