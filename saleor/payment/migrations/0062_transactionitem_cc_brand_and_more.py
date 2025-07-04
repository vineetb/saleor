# Generated by Django 5.2.1 on 2025-06-11 07:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payment", "0061_merge_20250527_1210"),
    ]

    operations = [
        migrations.AddField(
            model_name="transactionitem",
            name="cc_brand",
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name="transactionitem",
            name="cc_exp_month",
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(12),
                ],
            ),
        ),
        migrations.AddField(
            model_name="transactionitem",
            name="cc_exp_year",
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                validators=[django.core.validators.MinValueValidator(2000)],
            ),
        ),
        migrations.AddField(
            model_name="transactionitem",
            name="cc_first_digits",
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name="transactionitem",
            name="cc_last_digits",
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name="transactionitem",
            name="payment_method_name",
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="transactionitem",
            name="payment_method_type",
            field=models.CharField(
                blank=True,
                choices=[("card", "Card"), ("other", "Other")],
                max_length=32,
                null=True,
            ),
        ),
    ]
