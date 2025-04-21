CREATE TABLE IF NOT EXISTS bmi_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    height REAL NOT NULL,
    weight REAL NOT NULL,
    unit_type TEXT NOT NULL,
    bmi REAL NOT NULL,
    category TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL
);