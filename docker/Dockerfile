FROM python:3.10-slim

WORKDIR /code

RUN apt update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY weights/RFB-320.tflite /code/weights/RFB-320.tflite
COPY weights/sparse_face.tflite /code/weights/sparse_face.tflite
COPY . .
ENTRYPOINT ["python", "app.py"]