# Generated by Django 3.2.9 on 2022-01-12 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryEquipment', '0006_auto_20220110_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentinstance',
            name='equipment_status',
            field=models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='A', max_length=2, verbose_name='Equipment Status active/inactive/etc'),
        ),
        migrations.AlterField(
            model_name='equipmentinstance',
            name='location_status',
            field=models.CharField(choices=[('OH', 'On Hand'), ('PT', 'Patient'), ('RC', 'Repair Center'), ('RT', 'Retired'), ('MIA', 'Missing In Action')], default='OH', max_length=3, verbose_name='Location Status Of Equipment'),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_instance', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='InventoryEquipment.equipmentinstance', verbose_name='The equipment that this transaction is for')),
            ],
        ),
    ]