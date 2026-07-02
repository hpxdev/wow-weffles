# 🚀 Wow Weffles - Deployment Scripts

## 📋 Available Scripts

### 1. **setup.sh** - First Time Setup
Use this when setting up the project for the first time on PythonAnywhere.

```bash
bash setup.sh
```

**What it does:**
- Installs all requirements
- Runs database migrations
- Collects static files
- Creates superuser account
- Optionally loads sample menu data
- Verifies Django and WSGI configuration

### 2. **deploy.sh** - Update Deployment
Use this whenever you push updates from your local machine.

```bash
bash deploy.sh
```

**What it does:**
- Pulls latest code from GitHub
- Installs/updates requirements
- Runs any new migrations
- Collects static files
- Verifies configuration

---

## 🎯 Complete Deployment Guide for PythonAnywhere

### **STEP 1: Clone Repository (First Time Only)**

Open Bash console on PythonAnywhere:

```bash
cd ~
git clone https://github.com/hpxdev/wow-weffles.git
cd wow-weffles
```

### **STEP 2: Create Virtual Environment (First Time Only)**

```bash
mkvirtualenv --python=/usr/bin/python3.10 wowweffles-venv
```

### **STEP 3: Run Setup Script (First Time Only)**

```bash
bash setup.sh
```

Follow the prompts to create superuser and load sample data.

### **STEP 4: Update Settings**

```bash
nano wowweffles/settings.py
```

**Change these lines:**
```python
ALLOWED_HOSTS = ['Rexxuop.pythonanywhere.com', 'localhost', '127.0.0.1']
DEBUG = False
```

Save: `Ctrl+O`, `Enter`, `Ctrl+X`

### **STEP 5: Configure Web App**

Go to **Web** tab on PythonAnywhere:

#### **Virtualenv:**
```
/home/Rexxuop/.virtualenvs/wowweffles-venv
```

#### **WSGI Configuration File:**
Click the WSGI file link and replace ALL content with:

```python
import os
import sys

project_home = '/home/Rexxuop/wow-weffles'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'wowweffles.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

#### **Static Files:**
- URL: `/static/`
- Directory: `/home/Rexxuop/wow-weffles/staticfiles`

### **STEP 6: Reload Web App**

Click the green **Reload** button on Web tab.

**Your site is live!** 🎉
Visit: https://Rexxuop.pythonanywhere.com

---

## 🔄 Updating Your Site (After Initial Setup)

Whenever you make changes locally and push to GitHub:

### **On Your Computer:**
```bash
git add .
git commit -m "Your changes"
git push origin main
```

### **On PythonAnywhere Bash Console:**
```bash
cd ~/wow-weffles
workon wowweffles-venv
bash deploy.sh
```

### **Then:**
- Go to Web tab
- Click **Reload** button

Done! Changes are live.

---

## 🛠️ Manual Commands (If Needed)

### **Activate Virtual Environment:**
```bash
workon wowweffles-venv
```

### **Update Code:**
```bash
cd ~/wow-weffles
git pull origin main
```

### **Install Requirements:**
```bash
pip install -r requirements.txt
```

### **Run Migrations:**
```bash
python manage.py migrate
```

### **Collect Static Files:**
```bash
python manage.py collectstatic --noinput
```

### **Create Superuser:**
```bash
python manage.py createsuperuser
```

### **Load Sample Menu:**
```bash
python manage.py seed_menu
```

### **Test Django Settings:**
```bash
python manage.py check
```

---

## 📁 Important Paths

| Item | Path |
|------|------|
| Project Directory | `/home/Rexxuop/wow-weffles` |
| Virtual Environment | `/home/Rexxuop/.virtualenvs/wowweffles-venv` |
| Static Files | `/home/Rexxuop/wow-weffles/staticfiles` |
| Database | `/home/Rexxuop/wow-weffles/db.sqlite3` |
| WSGI File | `/var/www/rexxuop_pythonanywhere_com_wsgi.py` |

---

## 🐛 Troubleshooting

### **Check Error Logs:**
On Web tab, click:
- **Error log** - Python/Django errors
- **Server log** - Web server logs

### **Common Issues:**

**Import errors?**
```bash
workon wowweffles-venv
pip install -r requirements.txt
```

**Static files not loading?**
```bash
python manage.py collectstatic --noinput
```

**Database errors?**
```bash
python manage.py migrate
```

**WSGI import error?**
Check WSGI file configuration matches exactly as shown above.

---

## ✅ Deployment Checklist

### **First Time Setup:**
- [ ] Clone repository
- [ ] Create virtual environment
- [ ] Run `setup.sh`
- [ ] Update settings.py (ALLOWED_HOSTS, DEBUG)
- [ ] Configure virtualenv on Web tab
- [ ] Configure WSGI file
- [ ] Configure static files
- [ ] Reload web app
- [ ] Test website
- [ ] Login to admin

### **Updates:**
- [ ] Commit and push changes to GitHub
- [ ] Run `deploy.sh` on PythonAnywhere
- [ ] Reload web app
- [ ] Test changes

---

## 🌐 URLs

- **Website:** https://Rexxuop.pythonanywhere.com
- **Admin:** https://Rexxuop.pythonanywhere.com/admin/
- **GitHub:** https://github.com/hpxdev/wow-weffles

---

## 📞 Quick Help

**Need to update just CSS/JS?**
```bash
cd ~/wow-weffles
python manage.py collectstatic --noinput
```
Then reload web app.

**Need to reset database?**
```bash
cd ~/wow-weffles
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_menu
```

**Forgot superuser password?**
```bash
cd ~/wow-weffles
python manage.py changepassword your_username
```

---

## 🎊 Success!

Your Wow Weffles café website should now be live and running!

For detailed documentation, check:
- `PYTHONANYWHERE_CONFIG.md` - Complete configuration details
- `DEPLOYMENT_STEPS.md` - Step-by-step setup guide
- `QUICK_COMMANDS.txt` - Command reference
