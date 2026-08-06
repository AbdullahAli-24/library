# 📚 Library Management System

A complete **Library Management System** built with **Django 6** and **Bootstrap 5**.

The system allows users to browse books, borrow and return them, reserve unavailable books, rate books, manage favorites, and provides a dedicated dashboard for librarians.

---

# 🚀 Features

## Authentication

- User Registration
- User Login
- User Logout
- Strong Password Validation
- Protection against brute-force login attacks using Django Axes

---

## Book Management

- View all books
- Search books by title or author
- View detailed information for each book
- Add new books (Admin)
- Edit books (Admin)
- Delete books (Admin)

---

## Borrowing System

- Borrow available books
- Return borrowed books
- Automatic due date (14 days)
- Track current loans
- Borrow history

---

## Reservation System

- Reserve books when all copies are borrowed
- Automatically notify the first user in the reservation queue when a copy becomes available

---

## Ratings & Favorites

- Add books to Favorites
- Remove books from Favorites
- Rate books
- Calculate average rating
- Display rating count

---

## Overdue Management

- Detect overdue books
- Display overdue status
- Calculate overdue days
- Calculate late-return fines
- Display due-date reminders

---

## Librarian Dashboard

- Total books
- Total users
- Borrowed books
- Overdue books
- Top-rated books
- Most favorite books
- Recent loan activity

---

# 🛠 Technologies Used

- Python 3.14
- Django 6
- SQLite3
- Bootstrap 5
- HTML5
- CSS3
- JavaScript
- Django Axes

---

# 📂 Project Structure

```text
library/
│
├── books/
├── loan/
├── member/
├── project/
├── media/
├── static/
├── manage.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Go to the project directory

```bash
cd library
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Create an administrator account

```bash
python manage.py createsuperuser
```

### 8. Run the development server

```bash
python manage.py runserver
```

### 9. Open the application

```
http://127.0.0.1:8000/
```

---

# 👨‍💻 User Roles

## User

- Register
- Login
- Browse books
- Search books
- Borrow books
- Return books
- Reserve unavailable books
- Add favorites
- Rate books
- View personal loans

## Admin / Librarian

- Add books
- Edit books
- Delete books
- Access Django Admin
- Access Librarian Dashboard
- Monitor borrowing activity

---

# 📸 Screenshots

Add screenshots of:

- Login Page
- Registration Page
- Books Page
- Book Details
- Borrow Book
- My Loans
- Librarian Dashboard
- Django Admin

---

# 📄 Future Improvements

- Email reminders before due dates
- PDF borrowing receipts
- Barcode / QR code support
- Online payments for late fines
- REST API
- Docker deployment

---

# 👤 Author

**Ahmed Ayman Mashhour**

Faculty of Computers and Artificial Intelligence

---

# 📜 License

This project was developed for educational purposes and training.