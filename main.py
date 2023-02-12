import os
from django.utils.timezone import localtime
from datetime import timedelta
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit  # noqa: E402

if __name__ == '__main__':
    active_passcards = Passcard.objects.filter(is_active=True)
    active_visits = Visit.objects.filter(leaved_at=None)
    print()

    for visit in active_visits:
        print('Зашёл в хранилище, время по Москве:', localtime(visit.entered_at))  # noqa: E501
        print('Текущее время:', localtime())
        print('Находится в хранилище:', localtime() - localtime(visit.entered_at))  # noqa: E501
    print()
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    print('Активных пропусков:', len(active_passcards))
    print('Визиты:', active_visits)
