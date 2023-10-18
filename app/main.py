from fastapi import FastAPI, HTTPException, status
import uvicorn
from model import Comment
from completion import completion_api_predict

app = FastAPI(title="Comment Classifier")


@app.get("/healthcheck/",tags=["Health check"])
async def hc():
    return "server started"

@app.post("/comment",tags=["Comment"])
async def comment(req:Comment):
    if req.comment:
        result = completion_api_predict(req.comment)
        return {"result": result}
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad request")
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", proxy_headers=True, port=8000)