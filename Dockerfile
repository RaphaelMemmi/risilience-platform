FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip  # Ensure latest pip version
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port 8050 for Dash
EXPOSE 8050

CMD ["python", "main.py"]
