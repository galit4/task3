from fastapi import FastAPI
from api import info, keyword, critical_cve, all_cve, new_cve


app = FastAPI()
app.include_router(info.router)