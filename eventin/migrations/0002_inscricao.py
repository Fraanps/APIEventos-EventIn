# Generated by Django 5.1.5 on 2025-02-04 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inscricao', models.DateTimeField(auto_now_add=True)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscricoes', to='eventin.evento')),
                ('participante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inscricoes', to='eventin.participante')),
            ],
        ),
    ]
