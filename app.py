from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.get('/')
def home():
    return{ 'data' : 'welcome to homepage'}

@app.get('/contact')
def contact():
    return{ 'data' : 'welcome to contact page'}

@app.post('/upload')
def handleImage(files: list[UploadFile]):
    print(files)
    return {'status': 'files uploaded'}

import uvicorn
uvicorn.run(app)