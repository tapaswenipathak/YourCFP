# Generated by Django 2.2 on 2019-06-06 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProposalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proposal_status', models.CharField(choices=[('to_be_reviewed', 'Is yet to be reviewed'), ('under_review', 'Being Reviewed'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='to_be_reviewed', max_length=10)),
                ('proposal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='proposals.Proposal')),
            ],
        ),
    ]
