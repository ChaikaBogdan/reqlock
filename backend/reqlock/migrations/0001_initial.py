# Generated by Django 3.1.7 on 2021-03-14 17:54

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
                ('lock_status', models.CharField(blank=True, choices=[('LOCK', 'Locked'), ('UNLOCK', 'Unlocked'), ('AWAIT', 'Awaiting')], max_length=50, null=True)),
                ('contract_status', models.CharField(blank=True, choices=[('DRAFT', 'Draft'), ('DESIGN', 'In Design'), ('QA', 'QA'), ('DEV', 'DEV')], max_length=50, null=True)),
                ('tests_status', models.CharField(blank=True, choices=[('FAIL', 'Failing'), ('PASS', 'Passing'), ('FLAKY', 'Unstable'), ('NONE', 'None')], max_length=50, null=True)),
                ('components', models.ManyToManyField(blank=True, related_name='_contract_components_+', to='reqlock.Component')),
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
                ('members', models.ManyToManyField(blank=True, related_name='_organisation_members_+', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, choices=[('QA', 'QA'), ('DEV', 'Developer'), ('MAN', 'Manager'), ('DIR', 'Director'), ('SRE', 'SRE'), ('DEVOPS', 'DevOps'), ('DESIGN', 'Designer'), ('PO', 'Projects owner')], max_length=50, null=True)),
                ('sign_status', models.CharField(blank=True, choices=[('SIGNED', 'Signed'), ('AWAIT', 'Requested to sign'), ('REJECT', 'Reject to sign'), ('NAN', 'Sign not required')], max_length=50, null=True)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='reqlock.contract')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('members', models.ManyToManyField(blank=True, related_name='_project_members_+', to=settings.AUTH_USER_MODEL)),
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
