from fastapi import APIRouter

AdminRouter = APIRouter()

@AdminRouter.get("/", tags=["admin"])
async def admin_root():
    return {"message": "Admin"}
