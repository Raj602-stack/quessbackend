# HRMS Lite – Backend

## 📌 Project Overview

HRMS Lite is a lightweight Human Resource Management System designed to manage employee records and daily attendance.

The backend provides secure, RESTful APIs for:
- Employee management
- Attendance tracking
- Bulk attendance marking
- Date-wise attendance retrieval
- Token-based authentication

The application is fully Dockerized and uses PostgreSQL for data persistence.

---

## 🛠 Tech Stack

- Python 3.x
- Django
- Django REST Framework (DRF)
- PostgreSQL
- Docker & Docker Compose
- Token-based Authentication

---

## 🚀 Features

- Admin-only access (Token authentication)
- Create, view, delete employees
- Mark attendance (Present / Absent)
- Prevent weekend attendance marking
- Prevent duplicate attendance for same employee & date
- Bulk attendance marking API
- Filter attendance by date or employee
- Retrieve attendance history per employee

---

## 🧪 API Authentication

All endpoints require:

Authorization Header:

---

BACKEND HOSTED ON RAILWAY(as asked)

url:- https://splendid-wholeness-production-ecb0.up.railway.app

## 📂 Key Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/token/ | Get authentication token |
| GET | /api/employees/ | List employees |
| POST | /api/employees/ | Create employee |
| DELETE | /api/employees/{id}/ | Delete employee |
| GET | /api/attendance/?date=YYYY-MM-DD | Date-wise attendance |
| POST | /api/attendance/bulk_mark/ | Bulk mark attendance |
| GET | /api/employees/{id}/attendance/ | Employee attendance history |

---

## ⚠ Assumptions & Limitations

- Single admin user (no multi-role authentication).
- Leave management and payroll features are out of scope.
- No pagination implemented (suitable for small-to-medium datasets).
- Attendance marking restricted on weekends.
- Soft delete not implemented (employees are permanently deleted).

---

## 🧠 Design Considerations

- Uses `update_or_create` for safe bulk attendance updates.
- Enforces uniqueness on employee_id and email.
- Prevents duplicate attendance per employee per date.
- Dockerized for easy deployment.
