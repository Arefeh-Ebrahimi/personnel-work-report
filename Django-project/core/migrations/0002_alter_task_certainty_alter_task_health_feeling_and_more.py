# Generated by Django 4.2.7 on 2023-12-31 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='certainty',
            field=models.CharField(choices=[('confident', 'Confident'), ('midst', 'Midst'), ('vague', 'Vague')], max_length=255),
        ),
        migrations.AlterField(
            model_name='task',
            name='health_feeling',
            field=models.CharField(choices=[('perfect', 'Perfect'), ('normal', 'Normal'), ('weakness', 'Weakness')], max_length=255),
        ),
        migrations.AlterField(
            model_name='task',
            name='productivity',
            field=models.CharField(choices=[('great', 'Great'), ('good', 'Good'), ('bad', 'Bad')], max_length=255),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.CharField(choices=[('all', 'All'), ('retail', 'Retail'), ('promotion', 'Promotion'), ('iesco', 'IESCO'), ('dR_hajitaghi_web', 'DR hajitaghi Web'), ('baraye_iran', 'Baraye Iran'), ('branding', 'Branding'), ('dR_hajitaghi_app', 'DR hajitaghi App'), ('setup_things', 'Setup things')], max_length=255),
        ),
        migrations.AlterField(
            model_name='task',
            name='stage',
            field=models.CharField(choices=[('r&d', 'R&D'), ('action_doing_task', 'Action(Doing Task)'), ('cominucating', 'Cominucating'), ('monitor', 'Monitor'), ('setup_things', 'Setup Things')], max_length=255),
        ),
    ]
