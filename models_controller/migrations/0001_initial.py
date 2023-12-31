# Generated by Django 4.1.2 on 2023-03-15 10:49

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MidPokemonType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_slot', models.SmallIntegerField()),
                ('created_user', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_user', models.CharField(max_length=50)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'mid_pokemon_type',
            },
        ),
        migrations.CreateModel(
            name='TblType',
            fields=[
                ('type_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=5)),
                ('color_code', models.CharField(max_length=6)),
                ('created_user', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_user', models.CharField(max_length=50)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tbl_type',
                'ordering': ['type_id'],
            },
        ),
        migrations.CreateModel(
            name='TblPokemon',
            fields=[
                ('pokedex_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('pokemon_name', models.CharField(max_length=10)),
                ('genus', models.CharField(default='未分類', max_length=15, null=True)),
                ('characteristic', models.CharField(default='未登録', max_length=100, null=True)),
                ('generation', models.SmallIntegerField()),
                ('image_path', models.CharField(max_length=300)),
                ('created_user', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_user', models.CharField(max_length=50)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('types', models.ManyToManyField(through='models_controller.MidPokemonType', to='models_controller.tbltype')),
            ],
            options={
                'db_table': 'tbl_pokemon',
                'ordering': ['pokedex_id'],
            },
        ),
        migrations.AddField(
            model_name='midpokemontype',
            name='pokedex_id',
            field=models.ForeignKey(db_column='pokedex_id', on_delete=django.db.models.deletion.CASCADE, to='models_controller.tblpokemon'),
        ),
        migrations.AddField(
            model_name='midpokemontype',
            name='type_id',
            field=models.ForeignKey(db_column='type_id', on_delete=django.db.models.deletion.CASCADE, to='models_controller.tbltype'),
        ),
        migrations.CreateModel(
            name='TblAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'tbl_account',
                'verbose_name_plural': 'tbl_accounts',
                'db_table': 'tbl_account',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
