# Generated by Django 3.2.4 on 2021-08-14 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('components', models.ManyToManyField(blank=True, related_name='_reqlock_contract_components_+', to='reqlock.Component')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('members', models.ManyToManyField(blank=True, related_name='_reqlock_organisation_members_+', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganisationRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.organisation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TestStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.organisation')),
            ],
            options={
                'verbose_name': 'Test status',
                'verbose_name_plural': 'Test statuses',
            },
        ),
        migrations.CreateModel(
            name='SignStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.organisation')),
            ],
            options={
                'verbose_name': 'Sign status',
                'verbose_name_plural': 'Sign statuses',
            },
        ),
        migrations.CreateModel(
            name='ReviewCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.contract')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.organisationrole')),
                ('sign_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.signstatus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('linked_projects', models.ManyToManyField(blank=True, related_name='_reqlock_project_linked_projects_+', to='reqlock.Project')),
                ('members', models.ManyToManyField(blank=True, related_name='_reqlock_project_members_+', to=settings.AUTH_USER_MODEL)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.organisation')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LockStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.organisation')),
            ],
            options={
                'verbose_name': 'Lock status',
                'verbose_name_plural': 'Lock statuses',
            },
        ),
        migrations.CreateModel(
            name='CustomField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Custom field',
                'verbose_name_plural': 'Custom fields',
            },
        ),
        migrations.CreateModel(
            name='ContractType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.organisation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContractStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reqlock.organisation')),
            ],
            options={
                'verbose_name': 'Contract status',
                'verbose_name_plural': 'Contract statuses',
            },
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
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='reqlock.organisation')),
            ],
            options={
                'abstract': False,
            },
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
    ]
