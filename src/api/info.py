from fastapi import APIRouter
router = APIRouter(tags=["info"])



@router.get("/info")
def info_print():
    return "the simple example of FastApi usage\n authon YD"