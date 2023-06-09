# Generated by Django 4.1.7 on 2023-05-04 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_group_person_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='group',
        ),
        migrations.CreateModel(
            name='PersonGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_person', to='crud.group')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_group', to='crud.person')),
            ],
        ),
    ]
