# Generated by Django 4.1.2 on 2022-10-24 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('statusNaNf', models.BooleanField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='equipamentos')),
                ('classeTensao', models.DecimalField(decimal_places=1, max_digits=5)),
                ('correnteNominal', models.IntegerField()),
                ('fabricante', models.CharField(max_length=20)),
                ('numSerie', models.CharField(max_length=20)),
                ('dataFabricacao', models.DateField()),
            ],
        ),
    ]