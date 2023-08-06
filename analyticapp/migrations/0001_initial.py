# Generated by Django 4.2.3 on 2023-08-05 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('video', models.FileField(null=True, upload_to='assets/video/')),
                ('images', models.FileField(null=True, upload_to='assets/img/')),
                ('adress', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]
