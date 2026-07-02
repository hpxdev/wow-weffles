# 🧇 Foldable/Accordion Menu Guide

## 📋 What's New?

I've created a beautiful **foldable accordion menu** for your Wow Weffles website!

---

## 🎯 Features

✅ **Click to Expand** - Each category can be expanded/collapsed by clicking
✅ **Smooth Animations** - Beautiful slide and rotate animations
✅ **Item Counter** - Shows how many items in each category
✅ **Expand/Collapse All** - Buttons to open or close all categories at once
✅ **Hover Effects** - Nice hover animations on items
✅ **Mobile Responsive** - Works perfectly on phones and tablets
✅ **Accessible** - ARIA labels for screen readers
✅ **First Category Open** - First category starts expanded by default

---

## 🌐 How to Access

### **URL for Accordion Menu:**
```
https://YOUR_DOMAIN.com/menu/accordion/
```

Or locally:
```
http://127.0.0.1:8000/menu/accordion/
```

### **Regular Menu (Old Style):**
```
https://YOUR_DOMAIN.com/menu/
```

---

## 🎨 Design Features

### **Category Headers:**
- Large icon with colored background
- Category name in big, bold text
- Item count display (e.g., "8 items")
- Animated arrow that rotates when opened
- Hover effect changes background color

### **Menu Items:**
- Clean card design with white background
- Item name in bold
- Item description in smaller text
- Price in orange on the right
- Hover effect slides item slightly to the right
- VEG badge for vegetarian items

### **Controls:**
- **Expand All** button - Opens all categories
- **Collapse All** button - Closes all categories
- Buttons have nice hover animations

---

## 🔧 Technical Details

### **Files Created:**

1. **Template:** `templates/cafe/menu_accordion.html`
   - Full accordion menu layout
   - Embedded CSS styles
   - JavaScript for interactions

2. **View:** Added `menu_accordion()` function in `cafe/views.py`

3. **URL:** Added route in `cafe/urls.py`
   - Path: `/menu/accordion/`
   - Name: `menu_accordion`

---

## 🚀 How to Use on Your Site

### **Option 1: Replace Regular Menu**

To make the accordion menu your default menu:

**In `cafe/urls.py`**, change:
```python
path("menu/", views.menu, name="menu"),
```

To:
```python
path("menu/", views.menu_accordion, name="menu"),
```

### **Option 2: Add Link in Navigation**

Add a link to the accordion menu in your navigation:

**In `templates/base.html`**, add:
```html
<a href="{% url 'menu_accordion' %}">Menu (Accordion)</a>
```

### **Option 3: Keep Both Versions**

Keep both and let users choose:
- Regular menu: `/menu/`
- Accordion menu: `/menu/accordion/`

---

## 🎯 Customization

### **Change Colors:**

In `menu_accordion.html`, find the `<style>` section and modify:

```css
.menu-accordion-toggle {
  background: var(--orange);  /* Change this */
}

.accordion-item-price {
  color: var(--orange);  /* Change this */
}
```

### **Change Animation Speed:**

```css
.menu-accordion-content {
  transition: max-height 0.4s;  /* Make it faster/slower */
}
```

### **Start All Closed:**

In `menu_accordion.html`, remove the `active` classes from the first item:

Find:
```html
<div class="menu-accordion-header active" ...>
```

Change to:
```html
<div class="menu-accordion-header" ...>
```

And:
```html
<div class="menu-accordion-content active" ...>
```

Change to:
```html
<div class="menu-accordion-content" ...>
```

---

## 📱 Mobile Responsive

The accordion menu automatically adjusts for mobile:
- Smaller icons and text
- Stacked layout for items
- Touch-friendly tap areas
- Smooth scrolling

---

## ♿ Accessibility

The accordion menu includes:
- ARIA labels for screen readers
- Keyboard navigation support
- Focus states
- Proper semantic HTML

---

## 🔄 Deploying to PythonAnywhere

After I commit and push these changes:

```bash
cd ~/wow-weffles
workon wowweffles-venv
bash deploy.sh
```

Then click **Reload** on Web tab.

---

## 🎨 Preview

The accordion menu will look like this:

```
╔════════════════════════════════════╗
║  [Expand All ▼]  [Collapse All ▲]  ║
╠════════════════════════════════════╣
║  ☕  Tea & Chai         [▼]        ║  ← Click to expand
╠════════════════════════════════════╣
║  Masala Chai       ₹40             ║  ← Menu items
║  Ginger Chai       ₹45             ║
║  Kulhad Chai       ₹50             ║
╠════════════════════════════════════╣
║  ☕  Coffee             [▼]        ║  ← Click to expand
╠════════════════════════════════════╣
║  🥤  Juice & Health    [▼]        ║  ← Click to expand
╠════════════════════════════════════╣
║  🧇  Waffles           [▼]        ║  ← Click to expand
╚════════════════════════════════════╝
```

---

## 💡 Tips

1. **First impression:** The first category opens automatically so users see content immediately
2. **Quick access:** "Expand All" lets users see everything at once
3. **Clean look:** "Collapse All" keeps the page tidy
4. **Smooth:** Animations make the experience feel premium
5. **Fast:** Lightweight code, no external libraries needed

---

## ✅ What to Do Now

1. **Test locally:**
   - Visit: `http://127.0.0.1:8000/menu/accordion/`
   - Click on categories to expand/collapse
   - Test "Expand All" and "Collapse All" buttons

2. **If you like it:**
   - Deploy to PythonAnywhere using `deploy.sh`
   - Decide if you want it as default or alternate menu
   - Update navigation links if needed

3. **Customize:**
   - Change colors to match your brand
   - Adjust animation speeds
   - Modify starting state (all open/closed)

---

## 🎉 Enjoy!

Your customers will love the clean, interactive menu experience!

