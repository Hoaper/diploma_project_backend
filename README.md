# FLAT - Backend
## Pre-requirements:
- Python 3.11+
- Docker (optional)
- MongoDB
## Install
```bash
git clone https://github.com/Hoaper/diploma_project_backend
pip install -r requirements.txt
```

## Run
Make .env file extending from .env.example and replace all params to your preferences. <br />
Run could be with docker compose or without

### Without docker
This approach assumes that you have already running MongoDB instance
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Using docker 
```bash
docker compose up --build
```
