# Generated by Django 5.2 on 2025-04-16 19:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ticker', models.CharField(blank=True, max_length=10, null=True)),
                ('type', models.CharField(choices=[('ACTION', 'Action'), ('ETF', 'ETF'), ('OPC', 'OPCVM'), ('CASH', 'Liquidité'), ('CRYPTO', 'Cryptocurrency')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('CTO', 'Compte-titres ordinaire'), ('PEA', "Plan d'Épargne en Actions"), ('AV', 'Assurance Vie'), ('CP', 'Compte Courant')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=12)),
                ('price_at_buy', models.DecimalField(decimal_places=2, max_digits=12)),
                ('date', models.DateField()),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.asset')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='core.portfolio')),
            ],
        ),
    ]
