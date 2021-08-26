from fastapi import APIRouter


router = APIRouter()

@router.get("/users/me/")
async def read_users_me(current_user: str):
    return current_user