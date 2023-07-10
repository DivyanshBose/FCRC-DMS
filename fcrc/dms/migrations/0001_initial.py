# Generated by Django 4.2.2 on 2023-07-07 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Components',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SNo', models.CharField(max_length=50)),
                ('Work', models.CharField(max_length=50)),
                ('Grp', models.CharField(max_length=50)),
                ('Nomenclature', models.CharField(max_length=100)),
                ('Indate', models.CharField(max_length=50)),
                ('OutDate', models.CharField(max_length=50)),
                ('ServicableBER', models.CharField(max_length=50)),
                ('Fault', models.CharField(max_length=50)),
                ('DateofCompletion', models.CharField(max_length=50)),
                ('Remarks', models.CharField(max_length=50)),
                ('Information', models.CharField(max_length=50)),
                ('DateofJoining', models.CharField(max_length=50)),
            ],
        ),
    ]