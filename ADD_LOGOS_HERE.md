# 📸 How to Add Your Logo Images

## 📁 Step 1: Copy Images to Project

1. **Copy all your 62 logo images** from `D:\Downloads\IMG_6352` folder

2. **Paste them into:**
```
b:\f-work\Wow weffles\static\img\logos\
```

3. **Rename them:**
```
logo-1.png
logo-2.png
logo-3.png
logo-4.png
...
logo-62.png
```

---

## 📝 Step 2: Update the HTML (if you have more than 6)

The page currently shows 6 logo placeholders. To add more:

1. Open: `templates/cafe/logo_selection.html`

2. Find the last logo card (Logo Option 6)

3. Copy this block for each additional logo:

```html
<!-- Logo Option 7 -->
<div class="logo-card" data-logo-id="7" onclick="openLightbox(this)">
  <div class="logo-number">7</div>
  <div class="logo-image-container">
    <img src="{% static 'img/logos/logo-7.png' %}" alt="Logo Option 7" class="logo-image" data-name="Logo Name Here" data-desc="Description here">
  </div>
  <div class="logo-info">
    <div class="logo-name">Logo Name Here</div>
    <div class="logo-description">Description here</div>
  </div>
</div>
```

4. Change these for each logo:
   - `data-logo-id="7"` → 8, 9, 10, etc.
   - `logo-7.png` → logo-8.png, logo-9.png, etc.
   - `Logo Option 7` → Logo Option 8, 9, 10, etc.
   - `data-name="..."` → Your logo name
   - `data-desc="..."` → Your logo description
   - Logo name and description in the card

---

## 🚀 Step 3: Test Locally

Visit: `http://127.0.0.1:8000/logo-selection/`

Click on any logo - it should open in full-screen zoom mode!

---

## 📤 Step 4: Deploy

```bash
# Push to GitHub (local computer)
git add .
git commit -m "Add logo images"
git push origin main

# On PythonAnywhere Bash
cd ~/wow-weffles
workon wowweffles-venv
bash deploy.sh

# Then click Reload on Web tab
```

---

## ✨ Features Now Working:

✅ Click logo → Opens in full-screen zoom
✅ Press ESC or click X to close
✅ Click outside to close
✅ Shows logo name and description
✅ Smooth zoom animation
✅ No selection buttons (removed)
✅ Just "Back to Website" button

---

## 💡 Image Tips:

- **Format:** PNG or JPG works
- **Size:** Under 1MB each for fast loading
- **Resolution:** At least 500px width recommended
- **Background:** Transparent PNG looks best

---

Done! Your client can now browse and zoom all logos easily! 🎨
