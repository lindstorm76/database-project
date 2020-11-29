# Generated by Django 3.1 on 2020-11-29 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='databasesite.department', verbose_name='Department ID')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('amount', models.IntegerField()),
                ('lott_id', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('datetime', models.DateTimeField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emp_order', to='databasesite.employee', verbose_name='Employee ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_order', to='databasesite.item', verbose_name='Item ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proj_order', to='databasesite.project', verbose_name='Project ID')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='databasesite.warehouse', verbose_name='Warehouse ID'),
        ),
    ]
