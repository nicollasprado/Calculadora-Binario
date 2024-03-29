from src.app import app


HOST = "0.0.0.0"
PORT = 5000
DEBUG = True

if (__name__ == '__main__'):
    app.run(HOST, PORT, DEBUG)