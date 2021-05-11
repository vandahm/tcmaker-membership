# Generated by Django 3.2.2 on 2021-05-11 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_auto_20191209_0646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='household',
            name='discount',
        ),
        migrations.AddField(
            model_name='duesplan',
            name='allow_adhoc_prices',
            field=models.BooleanField(default=False, help_text='Allow members who use this Dues Plan to choose how much they wish to pay, enabling community-supported memberships.', verbose_name='Allow ad-hoc prices'),
        ),
        migrations.AlterField(
            model_name='household',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='administered_household_set', to='membership.person'),
        ),
        migrations.AlterField(
            model_name='studentteam',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='administered_studentteam_set', to='membership.person'),
        ),
        migrations.DeleteModel(
            name='Discount',
        ),
    ]
