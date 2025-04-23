from django.utils import timezone
from datetime import timedelta
from .models import Licence

def set_offline():
    ten_minutes_ago = timezone.now() - timedelta(minutes=10)
    Licence.objects.filter(update_time__lt=ten_minutes_ago).update(status=0)