# Generated by Django 4.0.8 on 2024-09-19 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_courseoffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('Daycear', 'Daycear'), ('Primary', 'Primary'), ('Junior Secondary', 'Junior Secondary'), ('Senior Secondary', 'Senior Secondary')], max_length=25, null=True),
        ),
    ]