# Wow Weffles · Café Website (Django)

A modern café website for **Wow Weffles**, Dulera, serving Tea/Chai, Coffee,
Juice/Health and Waffles. Built with **Django 5.2**, with a **database-driven menu**,
an **admin panel** for the owner, a **working contact form**, a matching **logo** (SVG),
and a **printable bifold menu**.

The design stays exactly as the original static build, with an earthy palette, orange accent,
and Fraunces + Manrope type, now powered by a backend.

---

## Why Django (what the backend gives you)

- **Menu managed from the admin**: add items, change prices, mark things "featured"
  or "sold out", all from a browser login. No code edits.
- **Editable café info**: address, hours, phone, socials and the Google Maps embed
  live in the admin and update the whole site (footer, contact, print menu).
- **Real contact form**: submissions are validated, saved to the database, and emailed.
- Room to grow: online ordering, table booking, blog, etc.

---

## Project layout

```
Wow weffles/
├─ manage.py
├─ requirements.txt
├─ db.sqlite3                 (created after migrate)
├─ wowweffles/                Project config
│  ├─ settings.py             App, templates, static, timezone, email
│  └─ urls.py
├─ cafe/                      Main app
│  ├─ models.py               CafeInfo, Category, MenuItem, ContactMessage
│  ├─ admin.py                Owner-facing admin (inline prices, filters)
│  ├─ views.py                home / menu / about / gallery / contact / print
│  ├─ urls.py
│  ├─ forms.py                ContactForm
│  ├─ context_processors.py   Injects café info + categories into every page
│  └─ management/commands/seed_menu.py   Loads the placeholder menu
├─ templates/
│  ├─ base.html              Shared header + footer + nav (one place!)
│  └─ cafe/                  home, menu, about, gallery, contact, print_menu
└─ static/
   ├─ css/styles.css   css/print.css
   ├─ js/main.js
   ├─ img/*.svg             Placeholder images
   └─ logo/*.svg            Logo variants
```

---

## Run it locally

From the project folder (Windows PowerShell shown; use the matching path on macOS/Linux):

```powershell
# 1. activate the virtual environment
venv\Scripts\activate            # macOS/Linux: source venv/bin/activate

# 2. (first time only) install + set up
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_menu       # loads the placeholder menu

# 3. run
python manage.py runserver
```

Open <http://127.0.0.1:8000/>. The admin is at <http://127.0.0.1:8000/admin/>.

> You can also run it without activating: `venv\Scripts\python.exe manage.py runserver`.

### Admin login (dev)

A development superuser was created:

- **username:** `admin`
- **password:** `wowweffles@123`

**⚠ Change this before deploying.** Create your own and/or update the password:
`python manage.py changepassword admin` (or `createsuperuser` for a new one).

---

## Editing content

| To change… | Where |
| --- | --- |
| Menu items / prices / sold-out / featured | **Admin → Menu items** (or **Categories** to reorder) |
| Address, hours, phone, email, socials, map embed | **Admin → Café info** |
| Read contact-form messages | **Admin → Contact messages** |
| Page copy (hero text, about story, testimonials) | `templates/cafe/*.html` |
| Colors / fonts | `static/css/styles.css` → `:root` variables |
| Logo | replace files in `static/logo/` |
| Photos | drop real images into `static/img/` and update the `{% static %}` tags |

The **menu page, home "featured" list, and the print menu all read from the database**:
edit once in the admin and every page updates.

---

## Contact form email

In development, submitted messages **print to the console** (the `runserver` terminal).
To send real email in production, edit the email settings in `wowweffles/settings.py`:
swap `EMAIL_BACKEND` to SMTP and add your host/user/password (e.g. a Gmail app password
or a service like SendGrid/Mailgun). Set `CONTACT_NOTIFY_EMAIL` to where you want messages.

---

## The print menu (bifold)

Visit **/menu/print/** (or the "Print Menu" button). It's a live, database-driven,
A4-landscape **4-panel** layout: front cover, two inside menu panels, back cover.

Click **🖨 Print / Save as PDF** → in the dialog choose **A4**, **Landscape**,
margins **None**, and enable **Background graphics**. For a physical fold, print
**double-sided (flip on long edge)** and fold in half.

---

## Deploy

This is a standard Django app. Good free/cheap hosts: **Render**, **Railway**,
**PythonAnywhere**, **Fly.io**.

Production checklist:
1. Set `DEBUG = False` and a real `SECRET_KEY` (use an environment variable).
2. Set `ALLOWED_HOSTS` to your domain.
3. `python manage.py collectstatic` and serve `staticfiles/` (WhiteNoise is the easy option).
4. Use Postgres instead of SQLite for anything beyond a demo.
5. Run behind a production server (Gunicorn/Uvicorn), not `runserver`.

---

## Brand quick-reference

| Token | Value | Use |
| --- | --- | --- |
| Brown | `#5A3E2B` | Headings, primary |
| Deep brown | `#3A281B` | Text, footer |
| Tan | `#D8C3A5` | Warm surfaces |
| Olive | `#7A7A52` | Accents, "veg" tags |
| Orange | `#E8720C` | Buttons, highlights |
| Cream | `#FAF6EF` | Page background |

Fonts: **Fraunces** (headings) + **Manrope** (body), from Google Fonts.

---

## Still to finalize (client to provide)

- Real menu items + prices → enter them in the **admin** (placeholders are loaded now)
- Exact Dulera address, phone, email, hours, socials, Google Maps embed → **Café info** in admin
- Real café photos → `static/img/`
- QR code image for the print menu back cover
