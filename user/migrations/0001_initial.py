# Generated by Django 2.2.11 on 2022-05-29 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=10, verbose_name='性别')),
                ('birthday', models.DateField(verbose_name='生日')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('info', models.CharField(help_text='一句话介绍自己，不超过250个字', max_length=255, verbose_name='个人简介')),
                ('grade', models.CharField(max_length=4, verbose_name='年级')),
                ('number', models.CharField(max_length=6, verbose_name='年级子学号')),
                ('password', models.CharField(max_length=30, verbose_name='密码')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=10, verbose_name='性别')),
                ('birthday', models.DateField(verbose_name='生日')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('info', models.CharField(help_text='不超过250个字', max_length=255, verbose_name='教师简介')),
                ('department_nu', models.CharField(max_length=3, verbose_name='院系号')),
                ('number', models.CharField(max_length=7, verbose_name='院内编号')),
                ('password', models.CharField(max_length=30, verbose_name='密码')),
            ],
        ),
        migrations.AddConstraint(
            model_name='teacher',
            constraint=models.UniqueConstraint(fields=('department_nu', 'number'), name='teacher_id'),
        ),
        migrations.AddConstraint(
            model_name='student',
            constraint=models.UniqueConstraint(fields=('grade', 'number'), name='student_id'),
        ),
    ]