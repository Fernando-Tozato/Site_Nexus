# Generated by Django 5.0 on 2023-12-08 20:56

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='prestador',
            name='especialidade',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='prestador',
            name='local_max',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='servico',
            name='local',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='solicitacao',
            name='local',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='carteira',
            name='prestador_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.prestador'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='cliente_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente_chats', to='core.cliente'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='prestador_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prestador_chats', to='core.prestador'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='usuario_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_cliente', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='cliente_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagamento_cliente', to='core.cliente'),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='prestador_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagamento_prestador', to='core.prestador'),
        ),
        migrations.AlterField(
            model_name='prestador',
            name='usuario_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_prestador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='cliente_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitacao_cliente', to='core.cliente'),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='prestador_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitacao_prestador', to='core.prestador'),
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
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
