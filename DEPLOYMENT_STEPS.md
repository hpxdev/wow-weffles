# 🚀 Deploy Wow Weffles to PythonAnywhere - Complete Guide

## 📋 Prerequisites
- PythonAnywhere account (free or paid)
- GitHub account
- Your PythonAnywhere username

---

## 🎯 STEP BY STEP GUIDE

### **Step 1: Push to GitHub** (Do this on your computer)

1. Go to GitHub.com and create a new repository called `wow-weffles`
2. **DO NOT** initialize with README (your project already has files)
3. Copy the repository URL: `https://github.com/YOUR_USERNAME/wow-weffles.git`

4. In your terminal/PowerShell, run:
```bash
git remote add origin https://github.com/YOUR_USERNAME/wow-weffles.git
git branch -M main
git push -u origin main
```

✅ Your code is now on GitHub!

---

### **Step 2: Delete Old Website** (On PythonAnywhere)

1. Login to **PythonAnywhere.com**
2. Click **Web** tab
3. Scroll down and click **"Delete [your old domain]"** button
4. Confirm deletion

---

### **Step 3: Clean Up Old Files** (PythonAnywhere Bash Console)

1. Click **"Consoles"** tab → **"Bash"**
2. Run these commands:

```bash
# See what folders you have
ls -la

# Delete old project (replace with your actual folder name)
rm -rf your-old-project-folder

# Delete old virtual environments
rm -rf venv
rm -rf virtualenv
```

---

### **Step 4: Clone Your New Project** (PythonAnywhere Bash)

```bash
# Clone from GitHub (replace YOUR_USERNAME)
git clone https://github.com/YOUR_USERNAME/wow-weffles.git

# Enter the project
cd wow-weffles

# Check it worked
ls -la
```

---

### **Step 5: Create Virtual Environment** (PythonAnywhere Bash)

```bash
# Create virtual environment
mkvirtualenv --python=/usr/bin/python3.10 wowweffles-venv

# Install all requirements
pip install -r requirements.txt
```

⏳ Wait for installation to complete (may take 1-2 minutes)

---

### **Step 6: Update Django Settings** (PythonAnywhere Bash)

```bash
# Open settings file
nano wowweffles/settings.py
```

Find and change these lines:

**Change line ~27:**
```python
ALLOWED_HOSTS = ['YOUR_USERNAME.pythonanywhere.com', 'localhost', '127.0.0.1']
```

**Change line ~25:**
```python
DEBUG = False
```

**Save and exit:**
- Press `Ctrl + O` (save)
- Press `Enter` (confirm)
- Press `Ctrl + X` (exit)

---

### **Step 7: Setup Database & Static Files** (PythonAnywhere Bash)

```bash
# Collect all static files (CSS, JS, images)
python manage.py collectstatic --noinput

# Create database tables
python manage.py migrate

# Create admin user
python manage.py createsuperuser
# Enter username, email, password when prompted

# Load sample menu data (optional)
python manage.py seed_menu
```

---

### **Step 8: Create New Web App** (PythonAnywhere Web Tab)

1. Go to **Web** tab
2. Click **"Add a new web app"**
3. Click **"Next"** (confirm domain)
4. Select **"Manual configuration"** (NOT Django!)
5. Select **"Python 3.10"**
6. Click **"Next"**

---

### **Step 9: Configure Web App Settings** (PythonAnywhere Web Tab)

#### A. **Set Virtual Environment:**

Scroll to **"Virtualenv"** section
Click **"Enter path to a virtualenv"**
Paste (replace YOUR_USERNAME):
```
/home/YOUR_USERNAME/.virtualenvs/wowweffles-venv
```
Click ✓ checkmark

#### B. **Configure WSGI File:**

1. Click the **blue WSGI configuration file link** (looks like: `/var/www/YOUR_USERNAME_pythonanywhere_com_wsgi.py`)
2. **DELETE ALL THE CONTENT** in the file
3. **PASTE THIS** (replace YOUR_USERNAME):

```python
import os
import sys

# Add project to path
project_home = '/home/YOUR_USERNAME/wow-weffles'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'wowweffles.settings'

# Import Django WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

4. Click **"Save"** (top right)

#### C. **Configure Static Files:**

Scroll to **"Static files"** section
Click **"Enter URL"** and **"Enter path"**:

```
URL: /static/
Directory: /home/YOUR_USERNAME/wow-weffles/staticfiles
```

Click ✓ checkmark

---

### **Step 10: Reload & Launch!** 🎉

1. Scroll to the top of the **Web** tab
2. Click the big green **"Reload YOUR_USERNAME.pythonanywhere.com"** button
3. Wait for it to say "All done!"
4. Click on your website link: **YOUR_USERNAME.pythonanywhere.com**

✅ **Your website is now LIVE!**

---

## 🔧 Access Admin Panel

1. Visit: `https://YOUR_USERNAME.pythonanywhere.com/admin/`
2. Login with the superuser credentials you created
3. You can now:
   - Add/edit menu items
   - Update cafe information
   - Manage categories

---

## 🔄 Update Website Later

When you make changes on your computer:

**On your computer:**
```bash
git add .
git commit -m "Description of changes"
git push origin main
```

**On PythonAnywhere Bash:**
```bash
cd wow-weffles
git pull origin main
python manage.py collectstatic --noinput
```

**Then:** Click **"Reload"** button on Web tab

---

## 🐛 Troubleshooting

### Website shows error?
- Check **Error log** (Web tab, click the link)
- Check **Server log** (Web tab, click the link)

### Static files not loading?
```bash
cd wow-weffles
python manage.py collectstatic --noinput
# Then reload web app
```

### Database issues?
```bash
cd wow-weffles
python manage.py migrate
# Then reload web app
```

### Code changes not showing?
- Make sure you ran `git pull origin main`
- Make sure you clicked **Reload** button on Web tab
- Try hard refresh in browser: `Ctrl + Shift + R`

---

## 📝 Important Notes

- **Replace YOUR_USERNAME** with your actual PythonAnywhere username everywhere
- Free accounts have 1 web app limit
- Database is separate on PythonAnywhere (doesn't sync with GitHub)
- Always **Reload** web app after ANY changes
- For production, consider using PostgreSQL instead of SQLite
- Set up a custom domain if you have a paid account

---

## ✅ Checklist

- [ ] Created GitHub repository
- [ ] Pushed code to GitHub
- [ ] Deleted old PythonAnywhere web app
- [ ] Cleaned up old files
- [ ] Cloned new repository
- [ ] Created virtual environment
- [ ] Updated settings.py
- [ ] Collected static files
- [ ] Ran migrations
- [ ] Created superuser
- [ ] Created new web app
- [ ] Set virtualenv path
- [ ] Configured WSGI file
- [ ] Configured static files
- [ ] Reloaded web app
- [ ] Tested website
- [ ] Accessed admin panel

---

## 🎊 Success!

Your Wow Weffles café website is now live on the internet!

Share your link: `https://YOUR_USERNAME.pythonanywhere.com`

