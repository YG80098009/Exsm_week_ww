FROM python:3.9

WORKDIR /app

# העתקת הדרישות והתקנה
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# [span_14](start_span)העתקת כל קוד האפליקציה[span_14](end_span)
COPY ./app ./app

# [span_15](start_span)הגדרת פורט והרצה[span_15](end_span)
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]