# Generated by Django 4.0.3 on 2023-03-15 02:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_rest', '0005_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='!kpv1Bn9RUeBgXltdze52dYqxxlX0z5XYZOYJ1mVn', max_length=128),
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip_code', models.IntegerField()),
                ('country', models.CharField(max_length=255)),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rentals', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toilet_paper', models.BooleanField(default=False)),
                ('soap', models.BooleanField(default=False)),
                ('towels', models.BooleanField(default=False)),
                ('bedding', models.BooleanField(default=False)),
                ('cleaning_supplies', models.BooleanField(default=False)),
                ('pool', models.BooleanField(default=False)),
                ('wifi', models.BooleanField(default=False)),
                ('kitchen', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
                ('jacuzzi', models.BooleanField(default=False)),
                ('washer_dryer', models.BooleanField(default=False)),
                ('ac_heat', models.BooleanField(default=False)),
                ('self_check_in', models.BooleanField(default=False)),
                ('workspace', models.BooleanField(default=False)),
                ('pets_allowed', models.BooleanField(default=False)),
                ('carbon_monoxide_detector', models.BooleanField(default=False)),
                ('smoke_detector', models.BooleanField(default=False)),
                ('first_aid_kit', models.BooleanField(default=False)),
                ('fire_extinguisher', models.BooleanField(default=False)),
                ('step_free_access', models.BooleanField(default=False)),
                ('wide_entryway', models.BooleanField(default=False)),
                ('wide_hallway_clearance', models.BooleanField(default=False)),
                ('accessible_bathroom', models.BooleanField(default=False)),
                ('rental', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='amenities', to='user_rest.rental')),
            ],
        ),
    ]
