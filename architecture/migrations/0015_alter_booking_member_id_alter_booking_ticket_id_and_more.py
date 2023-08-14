# Generated by Django 4.2.4 on 2023-08-14 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('architecture', '0014_alter_member_name_alter_member_surname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='member_id',
            field=models.ForeignKey(help_text="Участник встречи из таблицы 'Участники'", on_delete=django.db.models.deletion.CASCADE, related_name='member', to='architecture.member', verbose_name='Участник'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='ticket_id',
            field=models.ForeignKey(help_text="Билет на встречу из таблицы 'Билеты на встречи'", on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='architecture.ticket', verbose_name='Билет на встречу'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='place_id',
            field=models.ForeignKey(default=None, help_text="Место встречи из таблицы 'Места для встреч'", on_delete=django.db.models.deletion.SET_DEFAULT, related_name='place', to='architecture.place', verbose_name='Место'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='meeting_id',
            field=models.ForeignKey(help_text="Встреча из таблицы 'Встречи'", on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='architecture.meeting', verbose_name='Встреча'),
        ),
    ]
