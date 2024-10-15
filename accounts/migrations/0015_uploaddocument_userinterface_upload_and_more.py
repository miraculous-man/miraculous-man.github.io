# Generated by Django 4.0.8 on 2023-12-26 17:51

import accounts.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_courseoffer'),
        ('accounts', '0014_alter_user_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='Student_files/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'docx', 'doc', 'xls', 'xlsx', 'ppt', 'pptx', 'zip', 'rar', '7zip'])])),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('upload_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Userinterface_upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(null=True, upload_to='images')),
                ('news_feed', models.CharField(max_length=200)),
                ('event_feed', models.CharField(max_length=200)),
                ('contact_us', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='StudentApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField(max_length=30)),
                ('LG_origin', models.CharField(max_length=30)),
                ('state_origin', models.CharField(max_length=30)),
                ('parent_name', models.CharField(max_length=30)),
                ('parent_adress', models.CharField(max_length=30)),
                ('parent_number', models.CharField(max_length=30)),
                ('emergency_contact', models.CharField(max_length=30)),
                ('relationship', models.CharField(max_length=30)),
                ('emergency_address', models.CharField(max_length=30)),
                ('emergency_number', models.CharField(max_length=30)),
                ('level', models.CharField(choices=[('Bachloar', 'Bachloar Degree'), ('Master', 'Master Degree')], max_length=25, null=True)),
                ('student_files', models.FileField(upload_to='Student_files/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'docx', 'doc', 'xls', 'xlsx', 'ppt', 'pptx', 'zip', 'rar', '7zip'])])),
                ('student_certificate_waec_image', models.ImageField(default='default.png', null=True, upload_to='student_certificate_img')),
                ('student_certificate_jamb_image', models.ImageField(default='default.png', null=True, upload_to='student_certificate_img')),
                ('student_certificate_other_image', models.ImageField(default='default.png', null=True, upload_to='student_certificate_img')),
                ('student_passport', models.ImageField(default='default.png', null=True, upload_to='student_passport')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.program')),
            ],
        ),
        migrations.CreateModel(
            name='ApplyingStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('date_of_birth', models.DateField(max_length=30)),
                ('LG_origin', models.CharField(max_length=30)),
                ('state_origin', models.CharField(max_length=30)),
                ('parent_name', models.CharField(max_length=30)),
                ('parent_adress', models.CharField(max_length=30)),
                ('Parent_number', models.CharField(max_length=30)),
                ('Emergency_contact', models.CharField(max_length=30)),
                ('relationship', models.CharField(max_length=30)),
                ('emergency_address', models.CharField(max_length=30)),
                ('emergency_number', models.CharField(max_length=30)),
                ('level', models.CharField(choices=[('Bachloar', 'Bachloar Degree'), ('Master', 'Master Degree')], max_length=25, null=True)),
                ('file', models.FileField(upload_to='Student_files/', validators=[django.core.validators.FileExtensionValidator(['pdf', 'docx', 'doc', 'xls', 'xlsx', 'ppt', 'pptx', 'zip', 'rar', '7zip'])])),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('upload_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('student_certificate_waec_image', models.ImageField(default='default.png', null=True, upload_to='student_certificate_img')),
                ('student_certificate_jamb_image', models.ImageField(default='default.png', null=True, upload_to='student_certificate_img')),
                ('student_certificate_other_image', models.ImageField(default='default.png', null=True, upload_to='student_certificate_img')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.program')),
            ],
            managers=[
                ('objects', accounts.models.ApplyingStudentManager()),
            ],
        ),
    ]