# Generated by Django 2.2.7 on 2019-11-08 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webelopers', '0003_remove_course_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('document', models.FileField(upload_to='media/')),
            ],
        ),
    ]