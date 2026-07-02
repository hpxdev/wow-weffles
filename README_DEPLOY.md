# 🧇 Wow Weffles - PythonAnywhere Deployment

## 🚀 Quick Start

Your project is ready for deployment! Follow these steps:

### 1️⃣ Push to GitHub (Do this first!)

```bash
# Create a new repository on GitHub.com called: wow-weffles
# Then run these commands:

git remote add origin https://github.com/YOUR_GITHUB_USERNAME/wow-weffles.git
git branch -M main
git push -u origin main
```

### 2️⃣ Follow the Complete Guide

Open **`DEPLOYMENT_STEPS.md`** - This has the FULL step-by-step instructions

OR use **`QUICK_COMMANDS.txt`** - This has just the commands to copy/paste

---

## 📚 Files Created for You

| File | Purpose |
|------|---------|
| **DEPLOYMENT_STEPS.md** | Complete step-by-step guide with explanations |
| **QUICK_COMMANDS.txt** | Quick reference - just the commands |
| **PYTHONANYWHERE_DEPLOY.md** | Detailed technical documentation |

---

## ⚡ Super Quick Summary

**On Your Computer:**
1. Create GitHub repo `wow-weffles`
2. Push code: `git push -u origin main`

**On PythonAnywhere:**
1. Delete old web app (Web tab)
2. Delete old files: `rm -rf old-folder`
3. Clone: `git clone https://github.com/YOUR_USERNAME/wow-weffles.git`
4. Setup: `mkvirtualenv --python=/usr/bin/python3.10 wowweffles-venv`
5. Install: `pip install -r requirements.txt`
6. Edit settings: Change `ALLOWED_HOSTS` and `DEBUG = False`
7. Setup: `python manage.py collectstatic --noinput`
8. Setup: `python manage.py migrate`
9. Setup: `python manage.py createsuperuser`
10. Create new web app (Manual config, Python 3.10)
11. Set virtualenv path
12. Configure WSGI file (see DEPLOYMENT_STEPS.md)
13. Configure static files mapping
14. Click **Reload**

**Done!** Visit: `https://YOUR_USERNAME.pythonanywhere.com`

---

## 🆘 Need Help?

- **Website error?** Check Error log and Server log on Web tab
- **CSS not loading?** Run `collectstatic` again and reload
- **Changes not showing?** Make sure to click Reload button

---

## 🎯 Your Repository URL

After creating on GitHub, it will be:
```
https://github.com/YOUR_GITHUB_USERNAME/wow-weffles
```

---

## ✅ Checklist

Before you start:
- [ ] Have a PythonAnywhere account
- [ ] Have a GitHub account  
- [ ] Know your PythonAnywhere username
- [ ] Know your GitHub username

Ready to deploy:
- [ ] Created GitHub repository
- [ ] Pushed code to GitHub
- [ ] Opened DEPLOYMENT_STEPS.md
- [ ] Following the steps!

---

Good luck! 🍀
