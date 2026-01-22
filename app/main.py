from fastapi import FastAPI, UploadFile, File
import pandas as pd
import io
from .db import get_connection

app = FastAPI()


@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    contents = file.read()
    df = pd.read_csv(io.BytesIO(contents))

    def get_risk(range_km):
        if range_km <= 20:
            return "low"
        elif range_km <= 100:
            return "medium"
        elif range_km <= 300:
            return "high"
        else:
            return "extreme"

    df['risk_level'] = df['range_km'].apply(get_risk)

    df['manufacturer'] = df['manufacturer'].fillna("Unknown")

    conn = get_connection()
    cursor = conn.cursor()
    
    count_records = 0
    sql = """INSERT INTO weapons (weapon_id, weapon_name, weapon_type, range_km, 
                weight_kg, manufacturer, origin_country, storage_location, 
                year_estimated, risk_level) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql)
    count_records += 1
    
    conn.commit()
    cursor.close()
    conn.close()

    return {"status": "success", "inserted_records":count_records}