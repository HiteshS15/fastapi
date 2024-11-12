from fastapi import FastAPI

# creating an instance of the FastAPI class called app, 
# which will serve as the main entry point for your application.
app = FastAPI()

# This is a GET request for the application root path /.
@app.get("/")

# when someone visits the / route. This function returns a dictionary {"msg": "Api is Working"}.
def index():
    return {"msg":"Api is Working"}
    
#python -m uvicorn FastAPI:app --reload

@app.get("/about")
def about():
    return {"msg":"About Page"}