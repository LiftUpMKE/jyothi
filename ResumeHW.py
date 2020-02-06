from flask import Flask 
app = Flask (__name__)

Filey = open(file="C:\\Users\\jyoth\\OneDrive\\Desktop\\JyothiResume.htm")
webString = Filey.read()

@app.route('/')
def hello_world():
    return webString

if __name__ == '__main__':
    app.run() 