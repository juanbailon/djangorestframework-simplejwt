# Generated by Django 5.1.7 on 2025-03-23 06:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("token_blacklist", "0012_alter_outstandingtoken_user"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blacklistedtoken",
            options={
                "verbose_name": "Blacklisted Token",
                "verbose_name_plural": "Blacklisted Tokens",
            },
        ),
        migrations.AlterModelOptions(
            name="outstandingtoken",
            options={
                "ordering": ("user",),
                "verbose_name": "Outstanding Token",
                "verbose_name_plural": "Outstanding Tokens",
            },
        ),
    ]
