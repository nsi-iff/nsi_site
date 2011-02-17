# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Participation'
        db.create_table('members_participation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.Member'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projects.Project'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True)),
        ))
        db.send_create_signal('members', ['Participation'])

        # Deleting field 'Member.project_memberships'
        db.delete_column('members_member', 'project_memberships')

        # Removing M2M table for field current_team on 'Member'
        db.delete_table('members_member_current_team')


    def backwards(self, orm):
        
        # Deleting model 'Participation'
        db.delete_table('members_participation')

        # User chose to not deal with backwards NULL issues for 'Member.project_memberships'
        raise RuntimeError("Cannot reverse this migration. 'Member.project_memberships' and its values cannot be restored.")

        # Adding M2M table for field current_team on 'Member'
        db.create_table('members_member_current_team', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('member', models.ForeignKey(orm['members.member'], null=False)),
            ('team', models.ForeignKey(orm['teams.team'], null=False))
        ))
        db.create_unique('members_member_current_team', ['member_id', 'team_id'])


    models = {
        'members.member': {
            'Meta': {'object_name': 'Member'},
            'currently_does': ('django.db.models.fields.TextField', [], {}),
            'desertion_nsi_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'github': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lattes': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'life_and_work': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'slideshare': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'started_nsi_date': ('django.db.models.fields.DateField', [], {}),
            'twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
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
