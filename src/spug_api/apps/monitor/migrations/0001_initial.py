# Generated by Django 3.2.20 on 2023-07-17 17:59

from django.db import migrations, models
import django.db.models.deletion
import libs.mixins
import libs.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('1', '站点检测'), ('2', '端口检测'), ('3', '进程检测'), ('4', '自定义脚本'), ('5', 'Ping检测')], max_length=2)),
                ('group', models.CharField(max_length=255, null=True)),
                ('targets', models.TextField()),
                ('extra', models.TextField(null=True)),
                ('desc', models.CharField(max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('rate', models.IntegerField(default=5)),
                ('threshold', models.IntegerField(default=3)),
                ('quiet', models.IntegerField(default=1440)),
                ('fault_times', models.SmallIntegerField(default=0)),
                ('notify_mode', models.CharField(max_length=255)),
                ('notify_grp', models.CharField(max_length=255)),
                ('latest_run_time', models.CharField(max_length=20, null=True)),
                ('created_at', models.CharField(default=libs.utils.human_datetime, max_length=20)),
                ('updated_at', models.CharField(max_length=20, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='account.user')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='account.user')),
            ],
            options={
                'db_table': 'detections',
                'ordering': ('-id',),
            },
            bases=(models.Model, libs.mixins.ModelMixin),
        ),
    ]
