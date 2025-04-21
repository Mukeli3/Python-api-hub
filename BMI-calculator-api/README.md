# 🧾 BMI Calculator API

A simple and efficient Flask-based API for calculating and tracking Body Mass Index (BMI) with SQLite integration.

## 🚀 Features

- ✅ Calculate BMI using **metric (kg/cm)** or **imperial (lbs/in)** units  
- 🧠 Returns health classification (Underweight, Normal, Overweight, Obese)  
- 📂 Stores BMI calculation history in a lightweight SQLite database  
- 📜 History endpoint for reviewing past calculations  
- 🧱 Clean JSON responses with built-in error handling  
- ↻ Easily extensible and production-ready

## 🛠 Tech Stack

- **Backend**: Python 3, Flask  
- **Database**: SQLite  
- **Testing**: HTTPie, Pytest  

## 📁 Project Structure

```
bmi_api/
├── app/
│   ├── routes/       # API endpoints (calculate, history)
│   ├── models/       # Database operations and logic
│   └── schemas/      # Table schema definition
├── config.py         # App configuration
└── run.py            # Entry point for the application
```

## ⚙️ Setup & Installation

1. Clone the repo  
   `git clone https://github.com/yourusername/bmi-api.git`  
   `cd bmi-api`

2. Create and activate a virtual environment  
   `python3 -m venv venv`  
   - Linux/Mac: `source venv/bin/activate`  
   - Windows: `venv\Scripts\activate`

3. Install dependencies  
   `pip install -r requirements.txt`

4. Run the application  
   `python3 run.py`

## 📡 API Endpoints

### 1. `POST /calculate`

Calculates BMI and stores the result.

**Parameters** (sent as JSON or form data):  
- `height` *(float)* – Height (cm or inches)  
- `weight` *(float)* – Weight (kg or lbs)  
- `unit_type` *(optional string)* – `"metric"` or leave blank for imperial

**Example Request**:  
`http POST http://localhost:5000/calculate height:=175 weight:=70 unit_type="metric"`

**Example Response**:
```json
{
  "bmi": 22.86,
  "category": "Normal weight",
  "message": "Calculation saved!"
} 
```

### 2. `GET /history`

Fetches all past BMI calculations.

**Example Request**:  
`http GET http://localhost:5000/history`

**Example Response**: 
```
[
  {
    "id": 1,
    "height": 175,
    "weight": 70,
    "unit_type": "metric",
    "bmi": 22.86,
    "category": "Normal weight",
    "created_at": "2025-04-18T14:30:00"
  }
]
```
## 🥪 Sample Test Cases

- Metric input:  
  `http POST :5000/calculate height:=180 weight:=75 unit_type="metric"`

- Imperial input:  
  `http POST :5000/calculate height:=70 weight:=160`

- Missing field:  
  `http POST :5000/calculate height:=180`

- Invalid unit_type:  
  `http POST :5000/calculate height:=180 weight:=75 unit_type="invalid"`

## 🐛 Troubleshooting

- **400 Bad Request**: Ensure you're sending valid parameters as JSON or form data.  
- **415 Unsupported Media Type**: Use HTTPie, Postman, or set appropriate headers in curl (e.g. `-H "Content-Type: application/json"`).  
- **Database errors**:  
  - Confirm the app has permission to write in the project directory  
  - Ensure `bmi_database.db` isn’t locked or corrupted

## 🧾 License

**MIT** — Feel free to fork, modify, and use.