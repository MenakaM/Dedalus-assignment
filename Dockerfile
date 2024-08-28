From python:3.9

Workdir /app

COPY longest_subdir.py

CMD ["python" , longest_subdir.py , "/app"
