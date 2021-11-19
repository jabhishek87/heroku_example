from fastapi import APIRouter

UserRouter = APIRouter()

@UserRouter.get("/users", tags=["users"])
async def users_root():
    return {"message": "Users"}
