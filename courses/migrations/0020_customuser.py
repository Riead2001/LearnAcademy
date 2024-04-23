# Generated by Django 3.1.14 on 2024-03-31 17:48

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('courses', '0019_delete_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('education', models.CharField(blank=True, max_length=100, null=True)),
                ('college_name', models.CharField(blank=True, max_length=100, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
                ('role', models.CharField(blank=True, choices=[('student', 'Student'), ('instructor', 'Instructor')], max_length=20, null=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_set', related_query_name='custom_user', to='auth.Group', verbose_name='groups')),
                ('preferred_courses', models.ManyToManyField(blank=True, related_name='preferred_by', to='courses.Course')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_set', related_query_name='custom_user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'permissions': (('can_view_custom', 'Can view custom'),),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
