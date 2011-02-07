# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Member.current_team'
        db.alter_column('members_member', 'current_team', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Member.current_team'
        raise RuntimeError("Cannot reverse this migration. 'Member.current_team' and its values cannot be restored.")


    models = {
        'members.member': {
            'Meta': {'object_name': 'Member'},
            'current_team': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
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
