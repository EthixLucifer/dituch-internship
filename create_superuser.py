import os
import django
from django.contrib.auth import get_user_model

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_time_tracking.settings')
django.setup()

def create_superuser():
    User = get_user_model()
    username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'adminpassword')

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f"Superuser '{username}' created successfully!")
    else:
        print(f"Superuser '{username}' already exists.")

if __name__ == '__main__':
    create_superuser()