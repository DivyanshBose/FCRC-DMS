# Generated by Django 4.2.3 on 2023-07-10 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dms', '0006_alter_component_doc_alter_component_doj_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='component',
            old_name='flt',
            new_name='fault',
        ),
        migrations.RenameField(
            model_name='component',
            old_name='gp',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='component',
            old_name='idt',
            new_name='indate',
        ),
        migrations.RenameField(
            model_name='component',
            old_name='ifo',
            new_name='info',
        ),
        migrations.RenameField(
            model_name='component',
            old_name='nm',
            new_name='nmc',
        ),
        migrations.RenameField(
            model_name='component',
            old_name='odt',
            new_name='outdate',
        ),
        migrations.RenameField(
            model_name='component',
            old_name='rm',
            new_name='remarks',
        ),
        migrations.RenameField(
            model_name='component',
            old_name='sbr',
            new_name='servicableber',
        ),
        migrations.RenameField(
            model_name='component',
            old_name='sn',
            new_name='srNo',
        ),
        migrations.RenameField(
            model_name='component',
            old_name='wk',
            new_name='work',
        ),
    ]