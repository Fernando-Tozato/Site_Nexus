# Generated by Django 5.0 on 2023-12-15 23:06

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carteira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saldo_disponivel', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
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
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos/')),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('bairro', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=2)),
                ('celular', models.CharField(max_length=11)),
                ('groups', models.ManyToManyField(blank=True, related_name='usuarios_groups', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='usuarios_user_permissions', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_servicos', models.IntegerField()),
                ('num_solicitacoes', models.IntegerField()),
                ('usuario_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_cliente', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Extrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField()),
                ('descricao', models.CharField(max_length=255)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('carteira_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extratos', to='core.carteira')),
            ],
        ),
        migrations.CreateModel(
            name='Prestador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio', models.CharField(max_length=255)),
                ('ramo', models.CharField(max_length=255)),
                ('especialidade', models.CharField(max_length=255, null=True)),
                ('local_max', models.IntegerField(null=True)),
                ('num_servicos', models.IntegerField()),
                ('num_solicitacoes', models.IntegerField()),
                ('usuario_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_prestador', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_hora', models.DateTimeField()),
                ('metodo', models.CharField(max_length=255)),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagamento_cliente', to='core.cliente')),
                ('prestador_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagamento_prestador', to='core.prestador')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagens', models.TextField()),
                ('data_hora', models.DateTimeField()),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente_chats', to='core.cliente')),
                ('prestador_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prestador_chats', to='core.prestador')),
            ],
        ),
        migrations.AddField(
            model_name='carteira',
            name='prestador_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.prestador'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField()),
                ('pontuacao', models.IntegerField()),
                ('data_hora', models.DateTimeField()),
                ('avaliado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliado_reviews', to=settings.AUTH_USER_MODEL)),
                ('avaliador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliador_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('local', models.CharField(max_length=255, null=True)),
                ('data_hora', models.DateTimeField()),
                ('status', models.CharField(max_length=255)),
                ('pagamento_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='servico_pagamento', to='core.pagamento')),
            ],
        ),
        migrations.AddField(
            model_name='pagamento',
            name='servico_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pagamento', to='core.servico'),
        ),
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('local', models.CharField(max_length=255, null=True)),
                ('data_hora_solicitacao', models.DateTimeField()),
                ('data_hora_servico', models.DateTimeField()),
                ('status', models.CharField(max_length=255)),
                ('cliente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitacao_cliente', to='core.cliente')),
                ('prestador_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitacao_prestador', to='core.prestador')),
                ('servico_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='solicitacao_servico', to='core.servico')),
            ],
        ),
        migrations.AddField(
            model_name='servico',
            name='solicitacao_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='servico', to='core.solicitacao'),
        ),
    ]
