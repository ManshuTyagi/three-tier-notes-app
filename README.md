# 📝 Three-Tier Notes App

A simple **three-tier web application** built with:

- **Frontend/UI**: Flask + HTML/CSS + Bootstrap  
- **Backend**: Flask (Python) with SQLAlchemy ORM  
- **Database**: MySQL  
- **Reverse Proxy**: Nginx (for routing `/` → Flask app running on port 5000)

This app allows users to **create, view, and delete colorful notes** through a web UI.  
It demonstrates the classic **three-tier architecture**:  
**Client → Nginx → Flask Backend → MySQL Database**

---

## 🚀 Features
- Add, view, and delete notes with a **colorful UI**
- Persistent storage in **MySQL**
- Uses **SQLAlchemy ORM** (no raw SQL needed for CRUD)
- **.env** support for configuration
- Ready for **Docker + Docker Compose** deployment

---

## 📂 Project Structure
