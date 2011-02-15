# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Member.function'
        db.add_column('members_member', 'function', self.gf('django.db.models.fields.CharField')(default='nao informado', max_length=100), keep_default=False)

        # Changing field 'Member.slideshare'
        db.alter_column('members_member', 'slideshare', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Member.twitter'
        db.alter_column('members_member', 'twitter', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Member.github'
        db.alter_column('members_member', 'github', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))


    def backwards(self, orm):
        
        # Deleting field 'Member.function'
        db.delete_column('members_member', 'function')

        # Changing field 'Member.slideshare'
        db.alter_column('members_member', 'slideshare', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Member.twitter'
        db.alter_column('members_member', 'twitter', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Member.github'
        db.alter_column('members_member', 'github', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))


    models = {
        'members.member': {
            'Meta': {'object_name': 'Member'},
            'currently_does': ('django.db.models.fields.TextField', [], {}),
            'desertion_nsi_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'function': ('django.db.models.fields.CharField', [], {'default': "'nao informado'", 'max_length': '100'}),
            'github': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lattes': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'life_and_work': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slideshare': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'started_nsi_date': ('django.db.models.fields.DateField', [], {}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'members.participation': {
            'Meta': {'object_name': 'Participation'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['members.Member']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sponsor': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['members']
