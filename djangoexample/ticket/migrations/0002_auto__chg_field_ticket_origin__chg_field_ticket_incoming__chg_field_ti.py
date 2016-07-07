# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Ticket.origin'
        db.alter_column('ticket_ticket', 'origin', self.gf('django.db.models.fields.CharField')(max_length=400, null=True))

        # Changing field 'Ticket.incoming'
        db.alter_column('ticket_ticket', 'incoming', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Ticket.outgoing'
        db.alter_column('ticket_ticket', 'outgoing', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Ticket.status'
        db.alter_column('ticket_ticket', 'status', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Ticket.origin'
        raise RuntimeError("Cannot reverse this migration. 'Ticket.origin' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Ticket.incoming'
        raise RuntimeError("Cannot reverse this migration. 'Ticket.incoming' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Ticket.outgoing'
        raise RuntimeError("Cannot reverse this migration. 'Ticket.outgoing' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Ticket.status'
        raise RuntimeError("Cannot reverse this migration. 'Ticket.status' and its values cannot be restored.")

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
            'assignedto': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'tickets_assigned'", 'null': 'True', 'to': "orm['members.Member']"}),
            'category': ('django.db.models.fields.CharField', [], {'default': "'GEN'", 'max_length': '3'}),
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ticket.Comment']", 'null': 'True', 'symmetrical': 'False'}),
            'filedby': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['members.Member']"}),
            'filedtime': ('django.db.models.fields.DateTimeField', [], {}),
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ticket.File']", 'null': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incoming': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True'}),
            'outgoing': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "'MD'", 'max_length': '2'}),
            'punts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['punts.Punt']", 'null': 'True', 'symmetrical': 'False'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        }
    }

    complete_apps = ['ticket']