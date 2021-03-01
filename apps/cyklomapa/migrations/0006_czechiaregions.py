# Generated by Django 2.2.19 on 2021-02-28 14:41

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyklomapa', '0005_auto_20161012_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='CzechiaRegions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gml_id', models.CharField(max_length=80)),
                ('kod', models.IntegerField()),
                ('nazev', models.CharField(max_length=80)),
                ('nespravny', models.CharField(max_length=80)),
                ('regionsoudrznostikod', models.IntegerField()),
                ('platiod', models.CharField(max_length=80)),
                ('platido', models.CharField(max_length=80)),
                ('idtransakce', models.BigIntegerField()),
                ('globalniidnavrhuzmeny', models.BigIntegerField()),
                ('nutslau', models.CharField(max_length=80)),
                ('datumvzniku', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]