# Generated by Django 3.1 on 2022-02-01 15:55

from django.db import migrations, models
import django.db.models.deletion
import grimoirelab_toolkit.datetime
import sortinghat.core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_rename_matchingblacklist_to_recommenderexclusionterms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('created_at', sortinghat.core.models.CreationDateTimeField(default=grimoirelab_toolkit.datetime.datetime_utcnow, editable=False)),
                ('last_modified', sortinghat.core.models.LastModificationDateTimeField(default=grimoirelab_toolkit.datetime.datetime_utcnow, editable=False)),
                ('name', models.CharField(max_length=191)),
                ('type', models.CharField(choices=[('organization', 'Organization'), ('team', 'Team')], max_length=12)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='core.group')),
            ],
            options={
                'db_table': 'groups',
                'unique_together': {('name', 'organization')},
            },
        ),
    ]
