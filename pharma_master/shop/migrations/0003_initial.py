# Generated by Django 4.2.4 on 2023-09-03 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0002_remove_medicine_link'),
        ('security', '0001_initial'),
        ('shop', '0002_delete_retailerdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.medicine')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='security.retailerdetails')),
            ],
        ),
    ]
