# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Punt'
        db.create_table('punts_punt', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('purchasedate', self.gf('django.db.models.fields.DateField')()),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('punts', ['Punt'])

        # Adding M2M table for field maintenance on 'Punt'
        db.create_table('punts_punt_maintenance', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('punt', models.ForeignKey(orm['punts.punt'], null=False)),
            ('ticket', models.ForeignKey(orm['ticket.ticket'], null=False))
        ))
        db.create_unique('punts_punt_maintenance', ['punt_id', 'ticket_id'])


    def backwards(self, orm):
        # Deleting model 'Punt'
        db.delete_table('punts_punt')

        # Removing M2M table for field maintenance on 'Punt'
        db.delete_table('punts_punt_maintenance')


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
        'punts.punt': {
            'Meta': {'object_name': 'Punt'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maintenance': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ticket.Ticket']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'purchasedate': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'ticket.comment': {
            'Meta': {'object_name': 'Comment'},
            'attachedfiles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ticket.File']", 'symmetrical': 'False'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'subcomments': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ticket.Comment']", 'symmetrical': 'False'}),
            'submittedby': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['members.Member']"}),
            'submittedtime': ('django.db.models.fields.DateTimeField', [], {}),
            'uid': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        'ticket.file': {
            'Meta': {'object_name': 'File'},
            'actualfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'createdby': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['members.Member']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'ticket.ticket': {
            'Meta': {'object_name': 'Ticket'},
            'assignedto': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'tickets_assigned'", 'symmetrical': 'False', 'to': "orm['members.Member']"}),
            'category': ('django.db.models.fields.CharField', [], {'default': "'GEN'", 'max_length': '3'}),
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ticket.Comment']", 'symmetrical': 'False'}),
            'filedby': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['members.Member']"}),
            'filedtime': ('django.db.models.fields.DateTimeField', [], {}),
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ticket.File']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incoming': ('django.db.models.fields.TextField', [], {}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'outgoing': ('django.db.models.fields.TextField', [], {}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "'MD'", 'max_length': '2'}),
            'punts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['punts.Punt']", 'symmetrical': 'False'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        }
    }

    complete_apps = ['punts']