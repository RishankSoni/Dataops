from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse
import requests
from typing import Optional
import os

app = FastAPI()

# Serve static files (including index.html)
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

# Redirect root URL to index.html
@app.get("/")
def read_root():
    return RedirectResponse(url="/static/index.html")

BACKEND_URL = "http://10.190.0.2:9567"

# Route for retrieving the best-scoring document
@app.get("/get")
def get_best_document(query: Optional[str] = None):
    try:
        # Passing query parameter to backend
        if query:
            print(f"Sending query to backend: '{query}'")
            response = requests.get(f"{BACKEND_URL}/get?query={query}")
        else:
            print("No query parameter, sending request without query")
            response = requests.get(f"{BACKEND_URL}/get")
            
        response.raise_for_status()
        data = response.json()
        
        # Adding debugging to see the actual response
        print(f"Backend response contains {len(data.get('messages', {}))} documents")
        
        # Return directly to ensure proper structure
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to backend: {str(e)}")
        return {"messages": {}, "error": str(e)}

# Route for inserting a document
@app.post("/insert/{text}")
def insert_document(text: str):
    try:
        response = requests.post(f"{BACKEND_URL}/messages/{text}/")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

@app.get("/check-backend")
def check_backend():
    """Diagnostic endpoint to check backend connectivity"""
    try:
        # Trying all possible endpoints
        results = {}
        endpoints = ["/messages", "/get", "/es-status"]
        
        for endpoint in endpoints:
            try:
                response = requests.get(f"{BACKEND_URL}{endpoint}")
                results[endpoint] = {
                    "status_code": response.status_code,
                    "content": response.json() if response.status_code == 200 else None
                }
            except Exception as e:
                results[endpoint] = {"error": str(e)}
                
        return {"backend_url": BACKEND_URL, "results": results}
    except Exception as e:
        return {"error": str(e)}
