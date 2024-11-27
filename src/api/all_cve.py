from fastapi import APIRouter
import requests
import datetime

# Обчислення дати 5 днів тому
starttime = (datetime.datetime.now() - datetime.timedelta(days=5)).isoformat()
endtime = datetime.datetime.now().isoformat()  # Поточний час в ISO форматі
router = APIRouter(tags=["info"])

API_key = "0533abd6-0a0d-4ab3-ba4e-e9ca0649134c"
url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

@router.get("/get/all")
def get_all():
    params = {
        "pubStartDate": f"{starttime}Z",
        "pubEndDate": f"{endtime}Z",
        "resultsPerPage": 40  # Перевірка правильного параметра для кількості результатів
    }
    headers = {
        "accept": "application/json",
        "apikey": API_key,
    }
    response = requests.get(url, headers=headers, params=params)
    
    # Перевірка статусу відповіді
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Not connected to NIST, status code: {response.status_code}, details: {response.text}"}
