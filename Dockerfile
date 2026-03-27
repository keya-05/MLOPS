FROM python:3.9-slim
WORKDIR /app
# We create a dummy requirements file for now
RUN echo "flask" > requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
