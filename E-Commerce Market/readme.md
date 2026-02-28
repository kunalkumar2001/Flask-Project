# 🛒 Flask Market — Premium Animated E-Commerce Web App

Flask Market is a modern, fully functional **E-Commerce web application** built using **Flask, SQLAlchemy, Bootstrap, and JavaScript**, featuring a premium UI with animated backgrounds, glassmorphism cards, secure authentication, and complete buy/sell functionality.

This project demonstrates full-stack development skills including backend logic, database integration, authentication, and advanced frontend design.

---

## 🚀 Features

### 🔐 Authentication System
- User Registration with validation
- Secure Login and Logout
- Password hashing using bcrypt
- Unique username validation
- Secure session management using Flask-Login

---

### 🛍️ Market System
- View available products
- Buy items from the market
- Sell owned items back to market
- Dynamic ownership system
- Real-time budget update after purchase/sell

---

### 💰 Budget Management
- Each user has a budget
- Budget decreases when purchasing
- Budget increases when selling
- Budget displayed in navbar with animated badge

---

### 🎨 Premium UI / UX
- Ultra premium animated mesh background
- Glassmorphism product cards
- Smooth hover animations
- Animated buttons and modals
- Fully responsive design
- Modern ecommerce-style interface

---

### 📦 Product Management
- Display product image, name, barcode, price
- Product ownership tracking
- Product modal with details
- Buy / Sell confirmation modals

---

### 🧠 Backend Logic
- Item purchase validation
- Ownership assignment
- Budget validation before purchase
- Sell logic with ownership verification

---

### 🗄️ Database Integration
- SQLAlchemy ORM
- User table
- Item table
- Relationship between User and Item

---

### 🔒 Security Features
- Password hashing using bcrypt
- CSRF protection using Flask-WTF
- Secure login sessions
- Form validation

---

## 🛠️ Technologies Used

### Backend
- Flask
- SQLAlchemy
- Flask-Login
- Flask-WTF
- Bcrypt

### Frontend
- HTML
- CSS
- Bootstrap
- JavaScript
- Jinja2

### Database
- SQLite (can be upgraded to MySQL/PostgreSQL)

---

## 📂 Project Structure

```
FlaskMarket/
│
├── market/
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── welcome.html
│   │   ├── home.html
│   │   ├── market.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── includes/
│   │       ├── items_modals.html
│   │       └── owned_items_modals.html
│   │
│   ├── static/
│   │   ├── images/
│   │   │   ├── laptop.png
│   │   │   ├── phone.png
│   │   │   └── default.png
│   │   │
│   │   ├── css/
│   │   └── js/
│   │
│   ├── models.py
│   ├── forms.py
│   ├── routes.py
│   └── __init__.py
│
├── run.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation Guide

### Step 1: Clone the repository

```bash
git clone https://github.com/kunalkumar2001/flask-market.git
cd flask-market
```

---

## 🧠 How the System Works

### 👤 User Registration

- User enters username, email, and password  
- Password is hashed using bcrypt  
- User is saved in database  

---

### 🔐 User Login

- Username and password are verified  
- Session is created using Flask-Login  
- User is redirected to market page  

---

### 🛒 Purchase Item

- Check if item is available  
- Check if user has enough budget  
- Deduct budget from user  
- Assign item ownership to user  

---

### 💼 Sell Item

- Check item ownership  
- Remove ownership from user  
- Add budget back to user  

---

## 📸 Screens (Features)

### Welcome Page

- Animated premium background  
- Modern UI design  

### Market Page

- Product cards with image  
- Purchase and sell functionality  

### Login / Register Page

- Secure authentication  
- Form validation  

---

## 🎯 Skills Demonstrated

This project demonstrates:

- Full stack web development  
- Backend development using Flask  
- Database design using SQLAlchemy  
- Authentication system  
- UI/UX design  
- Animation and modern frontend design  
- MVC architecture  
- Secure coding practices  

---

## 🚀 Future Improvements

Possible upgrades:

- Add shopping cart system  
- Add payment gateway (Stripe / Razorpay)  
- Add admin dashboard  
- Add search and filter system  
- Add REST API version  
- Add product categories  
- Add order history  
- Add user profile page  

---

## 👨‍💻 Author

**Kunal Kumar**

Aspiring Data Scientist & AI and ML Developer 

### Skills:
- Python  
- Flask  
- SQL  
- Power BI  
- Web Development  

Portfolio:  
https://kunalkumar2001.github.io/

GitHub:  
https://github.com/kunalkumar2001

---

## ⭐ Support

If you like this project, please give it a ⭐ on GitHub.

---

## 📜 License

This project is open source and free to use.DME with badges, GIF demo, and professional formatting** that impresses recruiters.
