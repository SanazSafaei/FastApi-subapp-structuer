from fastapi import APIRouter

router = APIRouter()


@router.get("/admins/me/")
async def read_admins_me(current_user: str):
    return current_user