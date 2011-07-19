# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models
from django.template.defaultfilters import slugify

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Project.slug'
        db.add_column('projects_project', 'slug', self.gf('django.db.models.fields.SlugField')(db_index=True, default='', max_length=100, blank=True), keep_default=False)

        # Changing field 'Project.logo'
        db.alter_column('projects_project', 'logo', self.gf('thumbs.ImageWithThumbsField')(name='logo', sizes=((200, 200), (90, 90)), max_length=100, null=True))

        for project in orm.Project.objects.all():
            project.slug = slugify(project.name)
            project.save()

    def backwards(self, orm):
        
        # Deleting field 'Project.slug'
        db.delete_column('projects_project', 'slug')

        # User chose to not deal with backwards NULL issues for 'Project.logo'
        raise RuntimeError("Cannot reverse this migration. 'Project.logo' and its values cannot be restored.")


    models = {
        'projects.document': {
            'Meta': {'object_name': 'Document'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.Project']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('thumbs.ImageWithThumbsField', [], {'name': "'logo'", 'sizes': '((200, 200), (90, 90))', 'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '100', 'blank': 'True'}),
            'sponsor': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['projects']
