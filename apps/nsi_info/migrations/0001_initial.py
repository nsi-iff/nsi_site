# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding model 'NSIInfo'
        db.create_table('nsi_info_nsiinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('about', self.gf('django.db.models.fields.TextField')()),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('nsi_info', ['NSIInfo'])


    def backwards(self, orm):

        # Deleting model 'NSIInfo'
        db.delete_table('nsi_info_nsiinfo')


    models = {
        'nsi_info.nsiinfo': {
            'Meta': {'object_name': 'NSIInfo'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['nsi_info']
