# Generated by Django 3.1.7 on 2021-02-25 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('tech_stack', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(blank=True, choices=[('FRONTEND', 'Frontend'), ('BACKEND', 'Backend'), ('MONOLITH', 'Monolith'), ('LAMBDA', 'Lambda'), ('PRODUCER', 'Producer'), ('CONSUMER', 'Consumer'), ('BROKER', 'Broker'), ('QUEUE', 'Queue'), ('WORKER', 'Worker'), ('DB', 'Database'), ('DS', 'Data Source')], max_length=50, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, choices=[('FRONTEND', 'Frontend'), ('BACKEND', 'Backend'), ('DESIGN', 'Design')], max_length=50, null=True)),
                ('lock_status', models.CharField(choices=[('LOCK', 'Locked'), ('UNLOCK', 'Unlocked'), ('AWAIT', 'Awaiting')], default='UNLOCK', max_length=50)),
                ('contract_status', models.CharField(choices=[('DRAFT', 'Draft'), ('DESIGN', 'In Design'), ('QA', 'QA'), ('DEV', 'DEV')], default='DRAFT', max_length=50)),
                ('tests_status', models.CharField(choices=[('FAIL', 'Failing'), ('PASS', 'Passing'), ('FLAKY', 'Unstable'), ('NONE', 'None')], default='NONE', max_length=50)),
                ('components', models.ManyToManyField(blank=True, related_name='component_in_contracts', to='reqlock.Component')),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('homepage', models.URLField(blank=True, max_length=255, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=255, null=True)),
                ('members', models.ManyToManyField(related_name='member_in_organisations', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, choices=[('QA', 'QA'), ('DEV', 'DEVELOPER'), ('MAN', 'Manager'), ('DIR', 'Director'), ('SRE', 'SRE'), ('DEVOPS', 'DEVOPS'), ('DESIGN', 'DESIGNER'), ('PO', 'PROJECT OWNER')], max_length=50, null=True)),
                ('sign_status', models.CharField(blank=True, choices=[('SIGNED', 'Signed'), ('AWAIT', 'Requested to sign'), ('REJECT', 'Reject to sign'), ('NAN', 'Sign not required')], max_length=50, null=True)),
                ('contracts', models.ManyToManyField(blank=True, related_name='contract_in_reviews', to='reqlock.Contract')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('members', models.ManyToManyField(related_name='member_in_projects', to=settings.AUTH_USER_MODEL)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.organisation')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jira_ticket', models.URLField(blank=True, max_length=255, null=True)),
                ('testrail_case', models.URLField(blank=True, max_length=255, null=True)),
                ('zeplin_mockup', models.URLField(blank=True, max_length=255, null=True)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.contract')),
            ],
        ),
        migrations.AddField(
            model_name='component',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.project'),
        ),
    ]
