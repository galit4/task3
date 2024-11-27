from fastapi import APIRouter
router = APIRouter(tags=["info"])



@router.get("/info")
def hello_world():
    return "the simple example of FastApi usage\n authon YD"