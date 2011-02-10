# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Member.current_team'
        db.delete_column('members_member', 'current_team')

        # Adding M2M table for field current_team on 'Member'
        db.create_table('members_member_current_team', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('member', models.ForeignKey(orm['members.member'], null=False)),
            ('team', models.ForeignKey(orm['teams.team'], null=False))
        ))
        db.create_unique('members_member_current_team', ['member_id', 'team_id'])


    def backwards(self, orm):
        
        # Adding field 'Member.current_team'
        db.add_column('members_member', 'current_team', self.gf('django.db.models.fields.CharField')(max_length=100, null=True), keep_default=False)

        # Removing M2M table for field current_team on 'Member'
        db.delete_table('members_member_current_team')


    models = {
        'members.member': {
            'Meta': {'object_name': 'Member'},
            'current_team': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['teams.Team']", 'symmetrical': 'False'}),
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
        },
        'teams.team': {
            'Meta': {'object_name': 'Team'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['members']
