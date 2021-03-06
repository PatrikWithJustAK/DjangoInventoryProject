# Generated by Django 3.2.9 on 2022-01-10 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryEquipment', '0005_auto_20220110_1633'),
        ('InventoryStores', '0002_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentinstance',
            name='sale',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='InventoryStores.sale', verbose_name='The Sale Data for when this was sold'),
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
    ]
