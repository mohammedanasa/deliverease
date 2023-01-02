# Generated by Django 3.2.16 on 2023-01-02 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20230102_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('creating', 'Creating'), ('processing', 'Processing'), ('picking', 'Picking'), ('delivering', 'Delivering'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='creating', max_length=20),
        ),
    ]