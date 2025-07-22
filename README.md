# 📱 Mobile Store - Django Web Application

This is a Django-based web application that includes two major modules:

- **Owner App**: For store management (product listing, order management, etc.)
- **Customer App**: For browsing and placing orders.

It also features email notifications via Gmail, messaging using Django's built-in messages framework, and basic image handling with Pillow. The frontend is kept minimal for focus on backend logic.

---

## 🔧 Features

### ✅ Owner App
- Add/Edit/Delete products
- Manage stock and orders
- View customer order details
- Upload product images (via **Pillow**)

### ✅ Customer App
- View available products
- Place orders
- Receive order confirmation via email (configured with **Gmail SMTP**)
- Flash success/error messages via Django’s **messages framework**

---

## 🛠 Tech Stack

- **Backend**: Django
- **Database**: SQLite (default)
- **Image Handling**: Pillow
- **Email**: Gmail SMTP
- **Frontend**: HTML, CSS (minimal)

---

## 📩 Email Notification Setup

This project uses Gmail to send email confirmations.

### Steps:
1. Enable **Less secure app access** or **App Passwords** in your Gmail account.
2. In your Django project’s `settings.py`, add:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
````

---

## 📷 Pillow Installation

Pillow is used to handle product image uploads.

```bash
pip install Pillow
```

---

## 🚀 How to Run the Project

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/mobile-store-django.git
cd mobile-store-django
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py migrate
```

5. **Create superuser (for Owner login)**

```bash
python manage.py createsuperuser
```

6. **Run the server**

```bash
python manage.py runserver
```

7. Visit `http://127.0.0.1:8000/` in your browser.

---

## 📁 Folder Structure Overview

```
mobile-store/
│
├── owner/           # Owner app: manage products, orders
├── customer/        # Customer app: browse & order
├── templates/       # Shared templates
├── static/          # CSS, JS, Images (minimal)
├── media/           # Uploaded product images
├── manage.py
├── requirements.txt
└── README.md
```

---

## 📝 Requirements

```
Django>=3.2
Pillow
```
