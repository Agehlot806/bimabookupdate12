# Generated by Django 4.0.6 on 2022-11-09 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bima_policy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rtotables',
            fields=[
                ('rto_id', models.CharField(default='F884E', editable=False, max_length=5, primary_key=True, serialize=False, unique=True)),
                ('RegNo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StateRtos',
            fields=[
                ('stateid', models.CharField(default='1FE3FC19DF', editable=False, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('state', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='agents',
            name='login_id',
            field=models.CharField(default='0F0A22FD63', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='bankdetail',
            name='id',
            field=models.CharField(default='B47555', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='brokercode',
            name='id',
            field=models.CharField(default='F4E501', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='insurancecompany',
            name='id',
            field=models.CharField(default='23556F', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='payout',
            name='payoutid',
            field=models.CharField(default='AF92246', editable=False, max_length=7, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='policy',
            name='policyid',
            field=models.CharField(default='808D49A', editable=False, max_length=7, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='id',
            field=models.CharField(default='DC79EECD25354C0', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='rtoconversionmodel',
            name='id',
            field=models.CharField(default='EBE5A9', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='id',
            field=models.CharField(default='A6246C', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='staffmodel',
            name='login_id',
            field=models.CharField(default='B36EBDB2B4', editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='user_id',
            field=models.CharField(default='5151612E3C96493', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='vehiclecategory',
            name='id',
            field=models.CharField(default='24E16F', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='vehiclemakeby',
            name='id',
            field=models.CharField(default='74C15E', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='vehiclemodelname',
            name='id',
            field=models.CharField(default='6627C4', editable=False, max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.DeleteModel(
            name='rtotable',
        ),
        migrations.DeleteModel(
            name='StateRto',
        ),
        migrations.AddField(
            model_name='rtotables',
            name='sid_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bima_policy.statertos'),
        ),
    ]
