# Django App Test

## 📌 Project Description
Django App Test Automax is a web application built with Django, aimed at sellers of used cars since it is an easy to use platform and the logic is pretty straight forward, as you can see:

Create your account ---> Login ---> List the vehicle you want to sell or ask for information ---> Put your contact info. 

This project is easily adaptable to similar projects. It is mostly used as a template since it's very adaptable and friendly.

## 🛠️ Features
- User authentication: login, logout, register
- CRUD operations for the internal models, which can be edited
- Responsive frontend with Bootstrap
- Database integration (SQLite)
- Reports implemented
- Minimalist version deployed with Docker
- Friendly, reliable and easy to maintain

## 🚀 Installation Guide

### **1. Clone the Repository**
```bash
git clone https://github.com/Ivanbo420/Django_App_Test.git
```

### **2. Install Dependencies**
**In case you don't have Python and Django installed, please execute the following commands (Windows Users - CMD):**
```bash
winget install Python
```
```bash
pip install django
```
**In case you don't have Python and Django installed, please execute the following commands (Debian Users - Terminal):**
```bash
sudo apt install python3 python3-pip -y
```
```bash
pip3 install django
```

### **3. Change to the project's directory**
```bash
cd Django_App_Test
```

### **4. Create and Activate Virtual Environment for running the app**
```bash
python -m venv venv
```
```bash
.\venv\Scripts\activate
```

### **5. Install Specific Requirements for the Project**
```bash
pip install -r requirements.txt
```

### **6. Change to the src directory**
```bash
cd src
```

### **7. Collect Static Files**
```bash
python manage.py collectstatic --noinput
```

### **8. Run the Django project**
```bash
python manage.py runserver
```

### **9. Open the Web User Interface and test**
- Go to http://127.0.0.1:8000 or http://localhost:8000
- Test all the features once the Django server is running
