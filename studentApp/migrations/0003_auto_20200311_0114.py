# Generated by Django 2.2.1 on 2020-03-10 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentApp', '0002_auto_20200311_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfeedbackmodel',
            name='Rate_us',
            field=models.CharField(blank=True, choices=[('Verygood', '👍Verygood'), ('good', '👌awesome'), ('Average', '🙌average'), ('Bad', '😒poor')], max_length=64),
        ),
    ]
