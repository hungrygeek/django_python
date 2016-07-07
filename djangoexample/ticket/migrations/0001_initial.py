# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comment'
        db.create_table('ticket_comment', (
            ('uid', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('submittedby', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.Member'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('submittedtime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('ticket', ['Comment'])

        # Adding M2M table for field attachedfiles on 'Comment'
        db.create_table('ticket_comment_attachedfiles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comment', models.ForeignKey(orm['ticket.comment'], null=False)),
            ('file', models.ForeignKey(orm['ticket.file'], null=False))
        ))
        db.create_unique('ticket_comment_attachedfiles', ['comment_id', 'file_id'])

        # Adding M2M table for field subcomments on 'Comment'
        db.create_table('ticket_comment_subcomments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_comment', models.ForeignKey(orm['ticket.comment'], null=False)),
            ('to_comment', models.ForeignKey(orm['ticket.comment'], null=False))
        ))
        db.create_unique('ticket_comment_subcomments', ['from_comment_id', 'to_comment_id'])

        # Adding model 'File'
        db.create_table('ticket_file', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('createdby', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.Member'])),
            ('actualfile', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('ticket', ['File'])

        # Adding model 'Ticket'
        db.create_table('ticket_ticket', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('priority', self.gf('django.db.models.fields.CharField')(default='MD', max_length=2)),
            ('category', self.gf('django.db.models.fields.CharField')(default='GEN', max_length=3)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('filedtime', self.gf('django.db.models.fields.DateTimeField')()),
            ('filedby', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.Member'])),
            ('origin', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('incoming', self.gf('django.db.models.fields.TextField')()),
            ('outgoing', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('ticket', ['Ticket'])

        # Adding M2M table for field punts on 'Ticket'
        db.create_table('ticket_ticket_punts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ticket', models.ForeignKey(orm['ticket.ticket'], null=False)),
            ('punt', models.ForeignKey(orm['punts.punt'], null=False))
        ))
        db.create_unique('ticket_ticket_punts', ['ticket_id', 'punt_id'])

        # Adding M2M table for field files on 'Ticket'
        db.create_table('ticket_ticket_files', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ticket', models.ForeignKey(orm['ticket.ticket'], null=False)),
            ('file', models.ForeignKey(orm['ticket.file'], null=False))
        ))
        db.create_unique('ticket_ticket_files', ['ticket_id', 'file_id'])

        # Adding M2M table for field assignedto on 'Ticket'
        db.create_table('ticket_ticket_assignedto', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ticket', models.ForeignKey(orm['ticket.ticket'], null=False)),
            ('member', models.ForeignKey(orm['members.member'], null=False))
        ))
        db.create_unique('ticket_ticket_assignedto', ['ticket_id', 'member_id'])

        # Adding M2M table for field comments on 'Ticket'
        db.create_table('ticket_ticket_comments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ticket', models.ForeignKey(orm['ticket.ticket'], null=False)),
            ('comment', models.ForeignKey(orm['ticket.comment'], null=False))
        ))
        db.create_unique('ticket_ticket_comments', ['ticket_id', 'comment_id'])


    def backwards(self, orm):
        # Deleting model 'Comment'
        db.delete_table('ticket_comment')

        # Removing M2M table for field attachedfiles on 'Comment'
        db.delete_table('ticket_comment_attachedfiles')

        # Removing M2M table for field subcomments on 'Comment'
        db.delete_table('ticket_comment_subcomments')

        # Deleting model 'File'
        db.delete_table('ticket_file')

        # Deleting model 'Ticket'
        db.delete_table('ticket_ticket')

        # Removing M2M table for field punts on 'Ticket'
        db.delete_table('ticket_ticket_punts')

        # Removing M2M table for field files on 'Ticket'
        db.delete_table('ticket_ticket_files')

        # Removing M2M table for field assignedto on 'Ticket'
        db.delete_table('ticket_ticket_assignedto')

        # Removing M2M table for field comments on 'Ticket'
        db.delete_table('ticket_ticket_comments')


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

    complete_apps = ['ticket']