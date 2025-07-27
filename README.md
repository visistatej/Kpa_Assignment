# KPA Backend Assignment

This project implements two backend APIs for the KPA Form Data System using **FastAPI** and **PostgreSQL**. The APIs are built as per the provided Postman collection and integrate with the Flutter frontend.

---

## Features

### 1. POST `/form/submit`
- Accepts: `name`, `phone`, `email` as JSON
- Stores the data in PostgreSQL
- Returns success confirmation and submitted data

### 2. GET `/form/submissions`
- Fetches all submissions from the database
- Returns a list of JSON entries

---

## Tech Stack

- Python 3.13
- FastAPI
- PostgreSQL
- SQLAlchemy (ORM)
- Pydantic (Data validation)
- python-dotenv (for managing `.env` files)
- Swagger UI (auto API documentation)
- Postman (for API testing)

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/visistatej/Kpa_Assignment.git
cd Kpa_Assignment
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory and add your database URL:

```env
DATABASE_URL=postgresql://youruser:yourpassword@localhost:5432/yourdbname
```

Make sure `.env` is added to `.gitignore`:

```bash
echo ".env" >> .gitignore
```

### 5. Run the server

```bash
uvicorn main:app --reload
```

Visit: `http://127.0.0.1:8000`

---

## API Endpoints

### POST `/form/submit`

Submit a new form entry.

**Sample cURL:**
```bash
curl -X POST http://127.0.0.1:8000/form/submit \
-H "Content-Type: application/json" \
-d '{"name": "Teja", "phone": "6304504204", "email": "visistatejareddy1234@gmail.com"}'
```

### GET `/form/submissions`

Retrieve all submitted form entries.

---

## API Documentation

Access the Swagger UI at:

```
http://127.0.0.1:8000/docs
```

---

## Postman Collection

- File: `KPA_form_data.postman_collection.json`
- Contains:
  - POST `/form/submit`
  - GET `/form/submissions`
  - Sample requests and responses

---

## Author

- **Name**: Visista Teja Reddy  
- **Email**: visistatejareddy1234@gmail.com  
- **GitHub**: [https://github.com/visistatej](https://github.com/visistatej)
