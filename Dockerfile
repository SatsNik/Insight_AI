# # Use a stable Python version
# FROM python:3.11-slim

# # Set working directory inside the container
# WORKDIR /app

# # Copy dependency list first (to cache better)
# COPY requirements.txt .

# # Install system dependencies and Python packages
# RUN apt-get update && apt-get install -y gcc libffi-dev libssl-dev \
#     && pip install --no-cache-dir -r requirements.txt

# # Copy the rest of your code
# COPY . .

# # Run the app
# CMD ["python", "app.py"]


FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

# RUN apt-get update && apt-get install -y --no-install-recommends \
#     gcc libffi-dev libssl-dev build-essential \
#     && pip install --upgrade pip \
#     && pip install --no-cache-dir -r requirements.txt \
#     && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN apt-get update
RUN apt-get install -y --no-install-recommends gcc libffi-dev libssl-dev build-essential
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["python", "main.py"]

