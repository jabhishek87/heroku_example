from fastapi import FastAPI
import uvicorn

from app.admin import AdminRouter
from app.user import UserRouter

# port = int(os.environ.get('PORT', 8000))

app = FastAPI()

app.include_router(AdminRouter, prefix="/admin")
app.include_router(UserRouter)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

# if __name__ == "__main__":
#     uvicorn.run("app.api:app", host="0.0.0.0", port=port, reload=True)