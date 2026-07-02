#!/bin/bash

echo "🚀 Wow Weffles - Initial Setup Script"
echo "======================================"

# Check if we're in the right directory
if [ ! -f "manage.py" ]; then
    echo "❌ Error: manage.py not found. Make sure you're in the project directory."
    exit 1
fi

echo "📦 Installing requirements..."
pip install -r requirements.txt

echo "🗄️ Running migrations..."
python manage.py migrate

echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput

echo "👤 Creating superuser..."
echo "Please enter superuser details:"
python manage.py createsuperuser

echo "🍽️ Do you want to load sample menu data? (y/n)"
read -r response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    echo "📝 Loading sample menu data..."
    python manage.py seed_menu
    echo "✅ Sample menu data loaded!"
else
    echo "⏭️ Skipping sample data..."
fi

echo ""
echo "🔍 Verifying Django Settings..."
python -c "import os; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wowweffles.settings'); from django.conf import settings; print('✅ Settings Module:', settings.SETTINGS_MODULE)"

echo ""
echo "🌐 Verifying WSGI Import..."
python -c "from wowweffles.wsgi import application; print('✅ WSGI IMPORT SUCCESS')"

echo ""
echo "✅ Setup Complete!"
echo "=================="
echo ""
echo "📝 Next Steps:"
echo "1. Update wowweffles/settings.py:"
echo "   - Set ALLOWED_HOSTS = ['Rexxuop.pythonanywhere.com', 'localhost']"
echo "   - Set DEBUG = False"
echo ""
echo "2. Configure your WSGI file on PythonAnywhere"
echo "3. Set up static files mapping"
echo "4. Reload your web app"
echo ""
echo "🌐 Your site will be live at: https://Rexxuop.pythonanywhere.com"
