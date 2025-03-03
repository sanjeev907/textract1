# Generated by Django 5.0.4 on 2024-05-04 13:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_rename_ocrlabels_documentset_ocr_labels'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(blank=True, choices=[('Kaushik', 'Kaushik'), ('Kumar', 'Kumar'), ('Choudhary', 'Choudhary'), ('Gupta', 'Gupta'), ('Guar', 'Guar')], max_length=100, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('nationality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nationality', to='accounts.country')),
            ],
        ),
    ]
