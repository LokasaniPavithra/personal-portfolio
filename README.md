# Personal Portfolio Website

## Overview

A full-stack personal portfolio website built using Flask and MongoDB. The website showcases my skills, projects, certifications, and provides a contact form for visitors to connect with me.

The project includes an admin dashboard where contact messages can be securely viewed after authentication.

---

## Features

* Modern Responsive Portfolio Design
* About Me Section
* Skills Showcase
* Projects Showcase
* Certifications Section
* Contact Form
* MongoDB Atlas Integration
* Admin Login Authentication
* Protected Admin Dashboard
* Message Timestamp Tracking
* Logout Functionality

---

## Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Flask

### Database

* MongoDB Atlas

### Other Tools

* Python
* PyMongo
* Python Dotenv

---

## Project Structure

personal-portfolio/

├── templates/

│   ├── index.html

│   ├── success.html

│   ├── admin.html

│   └── admin_login.html

│

├── static/

│   ├── css/

│   └── js/

│

├── app.py

├── database.py

├── config.py

├── requirements.txt

├── .env

├── .gitignore

└── README.md


## Projects Included

## Certifications

## Installation

### Clone Repository

git clone <repository-url>

cd personal-portfolio

### Create Virtual Environment

python -m venv venv

### Activate Virtual Environment

Windows:

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Configure Environment Variables

Create a .env file and add:

MONGO_URI=your_mongodb_connection_string

ADMIN_USERNAME=your_username

ADMIN_PASSWORD=your_password

SECRET_KEY=your_secret_key

### Run Application

python app.py

---

## Admin Dashboard

Admin Login:

/admin-login

Admin Dashboard:

/admin

The dashboard allows authenticated administrators to:

* View all contact messages
* View submission timestamps
* Monitor visitor inquiries
* Logout securely

---

## Future Enhancements

* Project Image Gallery
* Email Notifications
* Resume Download Feature
* Advanced Dashboard Analytics
* Search and Filter Messages
* Dark/Light Theme Toggle

---

## Author

Pavithra Lokasani

B.Tech CSE (Artificial Intelligence & Machine Learning)

Malla Reddy Engineering College for Women
