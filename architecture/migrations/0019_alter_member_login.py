# Generated by Django 4.2.4 on 2023-09-14 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('architecture', '0018_alter_booking_member_id_alter_booking_ticket_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='login',
            field=models.CharField(blank=True, default=None, help_text='Логин участника в Telegram', max_length=200, null=True, verbose_name='Логин'),
        ),
    ]
