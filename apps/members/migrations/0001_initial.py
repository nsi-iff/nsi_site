# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Member'
        db.create_table('members_member', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('current_team', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('currently_does', self.gf('django.db.models.fields.TextField')()),
            ('life_and_work', self.gf('django.db.models.fields.TextField')()),
            ('site', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('github', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('twitter', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('slideshare', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('lattes', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('project_memberships', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('started_nsi_date', self.gf('django.db.models.fields.DateField')()),
            ('desertion_nsi_date', self.gf('django.db.models.fields.DateField')(null=True)),
        ))
        db.send_create_signal('members', ['Member'])


    def backwards(self, orm):
        
        # Deleting model 'Member'
        db.delete_table('members_member')


    models = {
        'members.member': {
            'Meta': {'object_name': 'Member'},
            'current_team': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'currently_does': ('django.db.models.fields.TextField', [], {}),
            'desertion_nsi_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'github': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lattes': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'life_and_work': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'project_memberships': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'slideshare': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'started_nsi_date': ('django.db.models.fields.DateField', [], {}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['members']
