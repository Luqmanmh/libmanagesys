# 📚 Perpus Sido Mukti – Library Management System

A web-based library management system developed for **Desa Sido Mukti, Bakaran Wetan** as part of **KKN-T IPB University 2025**.  
This system allows users to view, search, and manage book collections online.

### 🌐 Live Site  
[https://perpussidomukti.up.railway.app](https://perpussidomukti.up.railway.app)

---

## 📌 Features

- 🗂️ Folder-based book categorization  
- 🔍 Search functionality for users and admins  
- 📤 Admin upload panel for books and images  
- 🖼️ Image hosting via Cloudinary  
- 📦 PostgreSQL database integration  
- 📁 File and folder management  
- 🌐 Sitemap and robots.txt for SEO  
- ⚡ Responsive UI built with TailwindCSS and Bootstrap  
- 🔐 Login system for admins  
- 📄 Dynamic meta tags for Open Graph and search visibility

---

## 🚀 Tech Stack

| Tool | Description |
|------|-------------|
| Django | Python Web Framework |
| Railway | Hosting & PostgreSQL |
| Cloudinary | Media storage (book covers) |
| Tailwind CSS | Utility-first CSS framework |
| Bootstrap | Additional responsive components |
| PostgreSQL | Relational database |
| Gunicorn & Whitenoise | Production WSGI server and static file serving |

---

## 📁 Project Structure

```
├── Bookselv/              # Main app
├── core/                  # App core
├── media/                 # Local image uploads (dev only)
├── static/                # Static files (source)
├── staticfiles/           # Collected static files (prod)
├── templates/             # HTML templates
├── requirements.txt       # Python dependencies
├── Procfile               # Railway start command
├── .env                   # Environment variables (local only)
├── manage.py              # Django CLI entry
```

---

## ⚙️ Setup (Local)

1. **Clone the repository**
   ```bash
   git clone https://github.com/Luqmanmh/libmanagesys.git
   cd yourrepo
   ```

2. **Install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

3. **Environment config**
   Create a `.env` file with:
   ```env
   DEBUG=True                         # true for development only
   SECRET_KEY=your-secret-key
   CLOUDINARY_CLOUD_NAME=xxx
   CLOUDINARY_API_KEY=xxx
   CLOUDINARY_API_SECRET=xxx
   DATABASE_URL=sqlite:///db.sqlite3  # or your PostgreSQL URL
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run locally**
   ```bash
   python manage.py runserver
   ```

---

## 🚢 Deployment (Railway)

- Push your code to GitHub
- Connect GitHub repo to Railway
- Set up environment variables in Railway dashboard
- Ensure you have:
  - `Procfile` with `web: gunicorn core.wsgi`
  - Static files collected: `python manage.py collectstatic`
  - Tailwind compiled if used locally # if tailwind cant work, manually place on and refer tailwind style to static folder (i havent found an answer to this problem) #

---

## 🔍 SEO & Discoverability

- `robots.txt` is served at `/robots.txt`
- Sitemap available at `/sitemap.xml`
- Open Graph and Twitter meta tags included
- Verified with Google Search Console

---

## 📷 Credits

- Built by: **Luqman Mohammad Hakim**  
            https://www.linkedin.com/in/luqman-m-hakim-0250741a5/
- Built by: **Muhammad Agal Lulanika**  
            https://www.linkedin.com/in/muhammad-agal-lulanika-709490264/
- Built by: **Fikri Aulia Rahman** 
            https://www.linkedin.com/in/fikri-aulia-rahman-572556248/
- KKN-T IPB University 2025 Bakaran Wetan PATIKAB06