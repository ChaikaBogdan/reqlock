# Generated by Django 3.1.7 on 2021-05-25 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('components', models.ManyToManyField(blank=True, related_name='_contract_components_+', to='reqlock.Component')),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('members', models.ManyToManyField(blank=True, related_name='_organisation_members_+', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.organisation')),
            ],
        ),
        migrations.CreateModel(
            name='SignStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.organisation')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.contract')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.companyrole')),
                ('sign_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.signstatus')),
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
            name='LockStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.organisation')),
            ],
        ),
        migrations.CreateModel(
            name='CustomField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Custom Field',
                'verbose_name_plural': 'Custom Fields',
            },
        ),
        migrations.CreateModel(
            name='ContractType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.organisation')),
            ],
        ),
        migrations.CreateModel(
            name='ContractStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.organisation')),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='contract_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.contractstatus'),
        ),
        migrations.AddField(
            model_name='contract',
            name='lock_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.lockstatus'),
        ),
        migrations.AddField(
            model_name='contract',
            name='tests_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.teststatus'),
        ),
        migrations.AddField(
            model_name='contract',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.contracttype'),
        ),
        migrations.CreateModel(
            name='ComponentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='reqlock.organisation')),
            ],
        ),
        migrations.AddField(
            model_name='component',
            name='components_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='reqlock.componenttype'),
        ),
        migrations.AddField(
            model_name='component',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='component',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.project'),
        ),
        migrations.AddField(
            model_name='component',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.componenttype'),
        ),
        migrations.AddField(
            model_name='companyrole',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.organisation'),
        ),
    ]
