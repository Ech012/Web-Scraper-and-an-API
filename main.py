import fastapi as fs
from scraper import get_price_ils
from datetime import datetime
from fastapi import HTTPException

#creating the api
app = fs.FastAPI(title="Transfering any Currency to ILS", version="1.0")



@app.get("/get_cur/{cur}", description="The request returns the value of the currency in ILS")
async def get_ils(cur: str):
    coin = get_price_ils(cur)
    
    #in case of an error
    if coin == "Couldnt get the data":
        raise HTTPException(status_code=404, detail="The coin doesn't exist or there is an error")
    
    date = datetime.now()
    #the regulat data

    return {
        "Year":date.year ,
        "Month": date.month,
        "Day": date.day,
        "Hour": date.hour,
        "Min": date.minute,
        "Sec": date.second,
        "Cur in ILS": float(coin)
    }
