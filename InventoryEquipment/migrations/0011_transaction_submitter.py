# Generated by Django 3.2.9 on 2022-01-12 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('InventoryEquipment', '0010_auto_20220112_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='submitter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='requester', to='InventoryUsers.customuser', verbose_name=''),
            preserve_default=False,
        ),
    ]
