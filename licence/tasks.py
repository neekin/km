import logging
from django.utils import timezone
from datetime import timedelta
from .models import Licence

logger = logging.getLogger(__name__)

def set_offline():
    ten_minutes_ago = timezone.now() - timedelta(minutes=1)
    updated_count = Licence.objects.filter(update_time__lt=ten_minutes_ago).update(status=0)
    logger.info(f"set_offline executed. Updated {updated_count} records.")