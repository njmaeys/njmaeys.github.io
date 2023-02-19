import os
import uvicorn

if __name__ == "__main__":
    
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=1024,
        ssl_keyfile=os.environ.get("KEY_FILE"), 
        ssl_certfile=os.environ.get("CERT_FILE"),
    )