from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
        return "<center><h1>Welcome to Rossum's Original Band Of Tubas!</h1><p><img src='static/colored_robot.jpg' height='400px' width='290px' alt='funny tuba picture'></center>"

if __name__ == "__main__":
        app.run(host='192.168.2.209',port=5000)
