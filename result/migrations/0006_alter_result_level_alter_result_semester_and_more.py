# Generated by Django 4.0.8 on 2024-09-19 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0005_alter_result_id_alter_takencourse_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='level',
            field=models.CharField(choices=[('Daycear', 'Daycear'), ('Primary', 'Primary'), ('Junior Secondary', 'Junior Secondary'), ('Senior Secondary', 'Senior Secondary')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='semester',
            field=models.CharField(choices=[('First Term', 'First Term'), ('Second', 'Second Term'), ('Third', 'Third Term')], max_length=100),
        ),
        migrations.AlterField(
            model_name='takencourse',
            name='comment',
            field=models.CharField(blank=True, choices=[('Excellent', 'Excellent'), ('Very Good', 'Very good'), ('Good', 'Good'), ('Average', 'Average'), ('Bellow Average', 'Bellow Average'), ('FAIL', 'FAIL')], max_length=200),
        ),
        migrations.AlterField(
            model_name='takencourse',
            name='grade',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('NG', 'NG')], max_length=2),
        ),
    ]
