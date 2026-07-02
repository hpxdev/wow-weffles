# 🔧 PythonAnywhere Complete Configuration

Replace `YOUR_USERNAME` with your actual PythonAnywhere username everywhere!

---

## 📁 Web App Configuration (Web Tab)

### **1. Source Code Path**
```
/home/YOUR_USERNAME/wow-weffles
```

### **2. Working Directory**
```
/home/YOUR_USERNAME/wow-weffles
```

### **3. Virtual Environment Path**
```
/home/YOUR_USERNAME/.virtualenvs/wowweffles-venv
```

### **4. WSGI Configuration File**
Path: `/var/www/YOUR_USERNAME_pythonanywhere_com_wsgi.py`

**DELETE ALL CONTENT and replace with this:**

```python
import os
import sys

# Add your project directory to the sys.path
project_home = '/home/YOUR_USERNAME/wow-weffles'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variable to tell Django where the settings module is
os.environ['DJANGO_SETTINGS_MODULE'] = 'wowweffles.settings'

# Import Django's WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### **5. Static Files Mapping**

**URL:**
```
/static/
```

**Directory:**
```
/home/YOUR_USERNAME/wow-weffles/staticfiles
```

### **6. Python Version**
```
Python 3.10
```

---

## 📝 Django Settings (wowweffles/settings.py)

Update these values in your settings.py file:

### **ALLOWED_HOSTS**
```python
ALLOWED_HOSTS = ['YOUR_USERNAME.pythonanywhere.com', 'localhost', '127.0.0.1']
```

### **DEBUG**
```python
DEBUG = False  # Set to False for production
```

### **STATIC_ROOT** (should already be set)
```python
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

### **STATIC_URL** (should already be set)
```python
STATIC_URL = 'static/'
```

---

## 🗂️ Complete Directory Structure on PythonAnywhere

```
/home/YOUR_USERNAME/
├── wow-weffles/                      ← Source code
│   ├── cafe/                         ← Django app
│   ├── static/                       ← Original static files
│   ├── staticfiles/                  ← Collected static files (created by collectstatic)
│   ├── templates/                    ← HTML templates
│   ├── wowweffles/                   ← Django project settings
│   │   ├── settings.py              ← Main settings file
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── manage.py
│   ├── db.sqlite3                    ← Database (created after migrate)
│   └── requirements.txt
│
└── .virtualenvs/
    └── wowweffles-venv/              ← Virtual environment
```

---

## ⚙️ Complete Setup Commands (Bash Console)

Run these in order on PythonAnywhere Bash console:

```bash
# 1. Navigate to home directory
cd ~

# 2. Clone repository
git clone https://github.com/hpxdev/wow-weffles.git

# 3. Enter project directory
cd wow-weffles

# 4. Create virtual environment
mkvirtualenv --python=/usr/bin/python3.10 wowweffles-venv

# 5. Install dependencies
pip install -r requirements.txt

# 6. Collect static files
python manage.py collectstatic --noinput

# 7. Run migrations (create database)
python manage.py migrate

# 8. Create superuser account
python manage.py createsuperuser
# Enter username, email, password when prompted

# 9. Load sample menu data (optional)
python manage.py seed_menu
```

---

## 🌐 Web App Settings Summary

| Setting | Value |
|---------|-------|
| **Source code** | `/home/YOUR_USERNAME/wow-weffles` |
| **Working directory** | `/home/YOUR_USERNAME/wow-weffles` |
| **Virtualenv** | `/home/YOUR_USERNAME/.virtualenvs/wowweffles-venv` |
| **Python version** | 3.10 |
| **WSGI file** | `/var/www/YOUR_USERNAME_pythonanywhere_com_wsgi.py` |
| **Static URL** | `/static/` |
| **Static directory** | `/home/YOUR_USERNAME/wow-weffles/staticfiles` |

---

## 🔐 Environment Variables (Optional)

If you need to set environment variables:

1. Go to **Web** tab
2. Scroll to **Environment variables** section
3. Click **"Add a new environment variable"**

Common variables:
```
DJANGO_SETTINGS_MODULE = wowweffles.settings
PYTHONPATH = /home/YOUR_USERNAME/wow-weffles
```

---

## 📋 Step-by-Step Web App Creation

### **Step 1: Create Web App**
1. Web tab → "Add a new web app"
2. Click "Next" (confirm domain)
3. Select "Manual configuration" (NOT Django!)
4. Select "Python 3.10"
5. Click "Next"

### **Step 2: Configure Code Location**
Scroll to **"Code"** section:
- **Source code:** `/home/YOUR_USERNAME/wow-weffles`
- **Working directory:** `/home/YOUR_USERNAME/wow-weffles`

### **Step 3: Configure Virtual Environment**
Scroll to **"Virtualenv"** section:
- Click "Enter path to a virtualenv"
- Enter: `/home/YOUR_USERNAME/.virtualenvs/wowweffles-venv`
- Click ✓ checkmark

### **Step 4: Configure WSGI File**
Scroll to **"Code"** section:
1. Click the blue WSGI configuration file link
2. Delete ALL content
3. Paste the WSGI configuration from above
4. Replace YOUR_USERNAME
5. Click "Save"

### **Step 5: Configure Static Files**
Scroll to **"Static files"** section:
1. Click "Enter URL" → Enter: `/static/`
2. Click "Enter path" → Enter: `/home/YOUR_USERNAME/wow-weffles/staticfiles`
3. Click ✓ checkmark

### **Step 6: Reload Web App**
- Scroll to top
- Click big green "Reload YOUR_USERNAME.pythonanywhere.com" button

---

## 🔄 Update Workflow (After Making Changes)

### **On Your Computer:**
```bash
git add .
git commit -m "Your change description"
git push origin main
```

### **On PythonAnywhere Bash:**
```bash
cd ~/wow-weffles
git pull origin main
python manage.py collectstatic --noinput
python manage.py migrate  # if you changed models
```

### **On Web Tab:**
- Click the green "Reload" button

---

## 🚨 Troubleshooting

### **Check Logs:**
- **Error log:** Web tab → Click "Error log" link
- **Server log:** Web tab → Click "Server log" link

### **Common Issues:**

**CSS/JS not loading?**
```bash
cd ~/wow-weffles
python manage.py collectstatic --noinput
# Then reload web app
```

**Import errors?**
```bash
workon wowweffles-venv
pip install -r requirements.txt
# Then reload web app
```

**Database errors?**
```bash
cd ~/wow-weffles
python manage.py migrate
# Then reload web app
```

**Changes not showing?**
- Make sure you ran `git pull`
- Make sure you clicked "Reload" button
- Clear browser cache (Ctrl + Shift + R)

---

## ✅ Configuration Checklist

Before you start:
- [ ] PythonAnywhere account created
- [ ] Code pushed to GitHub
- [ ] Know your PythonAnywhere username

During setup:
- [ ] Old web app deleted
- [ ] Old files removed
- [ ] Repository cloned
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] Settings.py updated (ALLOWED_HOSTS, DEBUG)
- [ ] Static files collected
- [ ] Database migrated
- [ ] Superuser created

Web app configuration:
- [ ] New web app created (Manual config, Python 3.10)
- [ ] Source code path set
- [ ] Working directory set
- [ ] Virtualenv path set
- [ ] WSGI file configured
- [ ] Static files mapping added
- [ ] Web app reloaded

Final checks:
- [ ] Website loads without errors
- [ ] CSS/JS working
- [ ] Images loading
- [ ] Admin panel accessible (/admin/)
- [ ] Can login to admin

---

## 🎯 Quick Copy-Paste Values

Replace YOUR_USERNAME with your actual username, then copy these:

```
Source code: /home/YOUR_USERNAME/wow-weffles
Working directory: /home/YOUR_USERNAME/wow-weffles
Virtualenv: /home/YOUR_USERNAME/.virtualenvs/wowweffles-venv
Static URL: /static/
Static directory: /home/YOUR_USERNAME/wow-weffles/staticfiles
```

---

## 📞 Your URLs

After deployment:
- **Website:** `https://YOUR_USERNAME.pythonanywhere.com`
- **Admin:** `https://YOUR_USERNAME.pythonanywhere.com/admin/`
- **GitHub:** `https://github.com/hpxdev/wow-weffles`

---

## 🎊 Success!

Once configured, your website will be live at:
### `https://YOUR_USERNAME.pythonanywhere.com`

Remember: Always click the **Reload** button after making any changes!
