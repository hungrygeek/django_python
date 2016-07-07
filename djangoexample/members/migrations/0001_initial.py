# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Member'
        db.create_table('members_member', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=200)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('joindate', self.gf('django.db.models.fields.DateField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('bio', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('members', ['Member'])

        # Adding M2M table for field files on 'Member'
        db.create_table('members_member_files', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('member', models.ForeignKey(orm['members.member'], null=False)),
            ('file', models.ForeignKey(orm['ticket.file'], null=False))
        ))
        db.create_unique('members_member_files', ['member_id', 'file_id'])


    def backwards(self, orm):
        # Deleting model 'Member'
        db.delete_table('members_member')

        # Removing M2M table for field files on 'Member'
        db.delete_table('members_member_files')


    models = {
        'members.member': {
            'Meta': {'object_name': 'Member'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ticket.File']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joindate': ('django.db.models.fields.DateField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'ticket.file': {
            'Meta': {'object_name': 'File'},
            'actualfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'createdby': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['members.Member']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['members']