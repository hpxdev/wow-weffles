# Deploy Wow Weffles to PythonAnywhere

## Step 1: Push to GitHub

First, create a new repository on GitHub named `wow-weffles`, then:

```bash
git remote add origin https://github.com/YOUR_USERNAME/wow-weffles.git
git branch -M main
git push -u origin main
```

## Step 2: Delete Old Website on PythonAnywhere

1. Log in to PythonAnywhere: https://www.pythonanywhere.com
2. Go to **Web** tab
3. Click on your existing web app
4. Scroll down and click **Delete web app** button
5. Confirm deletion

## Step 3: Delete Old Files

Open a **Bash console** on PythonAnywhere and run:

```bash
# List your current directories
ls -la

# Delete old project directory (replace 'old-project-name' with your actual folder name)
rm -rf old-project-name

# Clean up old virtual environment if exists
rm -rf venv
rm -rf virtualenv
```

## Step 4: Clone New Project

In the same Bash console:

```bash
# Clone your repository
git clone https://github.com/YOUR_USERNAME/wow-weffles.git

# Navigate to project
cd wow-weffles
```

## Step 5: Create Virtual Environment

```bash
# Create virtual environment with Python 3.10
mkvirtualenv --python=/usr/bin/python3.10 wowweffles-venv

# Install dependencies
pip install -r requirements.txt
```

## Step 6: Create New Web App

1. Go to **Web** tab
2. Click **Add a new web app**
3. Choose **Manual configuration**
4. Select **Python 3.10**
5. Click **Next**

## Step 7: Configure Web App

### A. Set Virtual Environment Path

In the **Virtualenv** section, enter:
```
/home/YOUR_USERNAME/.virtualenvs/wowweffles-venv
```
Click the checkmark to save.

### B. Configure WSGI File

1. Click on the **WSGI configuration file** link (something like `/var/www/YOUR_USERNAME_pythonanywhere_com_wsgi.py`)
2. **Delete all content** and replace with:

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

**Important**: Replace `YOUR_USERNAME` with your actual PythonAnywhere username.

3. Click **Save**

## Step 8: Update Django Settings

Open another Bash console and edit settings:

```bash
cd wow-weffles
nano wowweffles/settings.py
```

Make these changes:

1. **Update ALLOWED_HOSTS**:
```python
ALLOWED_HOSTS = ['YOUR_USERNAME.pythonanywhere.com', 'localhost', '127.0.0.1']
```

2. **Update DEBUG** (for production):
```python
DEBUG = False
```

3. **Add STATIC_ROOT**:
```python
STATIC_ROOT = '/home/YOUR_USERNAME/wow-weffles/staticfiles'
```

Save with `Ctrl+O`, `Enter`, then exit with `Ctrl+X`.

## Step 9: Set Up Static Files

In Bash console:

```bash
# Collect static files
python manage.py collectstatic --noinput
```

Then in **Web** tab:

1. Scroll to **Static files** section
2. Click **Add a new static files mapping**
3. Enter:
   - URL: `/static/`
   - Directory: `/home/YOUR_USERNAME/wow-weffles/staticfiles`

## Step 10: Set Up Database

In Bash console:

```bash
cd wow-weffles

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Seed menu data (optional)
python manage.py seed_menu
```

## Step 11: Reload Web App

1. Go back to **Web** tab
2. Click the big green **Reload** button at the top
3. Wait for reload to complete

## Step 12: Test Your Site

Visit: `https://YOUR_USERNAME.pythonanywhere.com`

## Step 13: Access Admin Panel

1. Visit: `https://YOUR_USERNAME.pythonanywhere.com/admin/`
2. Login with superuser credentials
3. Add/edit menu items, cafe information, etc.

---

## Troubleshooting

### If you see errors:

1. Check **Error log** on Web tab (click the link)
2. Check **Server log** on Web tab

### Common fixes:

```bash
# Reload web app after any code changes
# (Go to Web tab and click Reload button)

# Update code from GitHub
cd wow-weffles
git pull origin main

# Reinstall requirements if changed
workon wowweffles-venv
pip install -r requirements.txt

# Recollect static files if CSS/JS changed
python manage.py collectstatic --noinput

# Always reload after changes!
```

---

## Quick Update Commands

When you make changes locally and want to update PythonAnywhere:

```bash
# 1. On your local machine
git add .
git commit -m "Your changes"
git push origin main

# 2. On PythonAnywhere Bash console
cd wow-weffles
git pull origin main
python manage.py collectstatic --noinput
# Then reload web app from Web tab
```

---

## Important Notes

- Replace `YOUR_USERNAME` with your actual PythonAnywhere username everywhere
- Free PythonAnywhere accounts have limitations (1 web app, limited bandwidth)
- Database file (db.sqlite3) is local to PythonAnywhere - won't sync with GitHub
- Always reload web app after making changes
