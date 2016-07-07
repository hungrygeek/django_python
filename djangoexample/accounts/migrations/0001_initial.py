# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AccountItem'
        db.create_table('accounts_accountitem', (
            ('uid', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('createdby', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['members.Member'])),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('submittedtime', self.gf('django.db.models.fields.DateTimeField')()),
            ('ticket', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ticket.Ticket'])),
            ('transactionwith', self.gf('django.db.models.fields.TextField')()),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('account', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('balancewhendrawn', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal('accounts', ['AccountItem'])

        # Adding M2M table for field attachedfiles on 'AccountItem'
        db.create_table('accounts_accountitem_attachedfiles', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accountitem', models.ForeignKey(orm['accounts.accountitem'], null=False)),
            ('file', models.ForeignKey(orm['ticket.file'], null=False))
        ))
        db.create_unique('accounts_accountitem_attachedfiles', ['accountitem_id', 'file_id'])

        # Adding M2M table for field comments on 'AccountItem'
        db.create_table('accounts_accountitem_comments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accountitem', models.ForeignKey(orm['accounts.accountitem'], null=False)),
            ('comment', models.ForeignKey(orm['ticket.comment'], null=False))
        ))
        db.create_unique('accounts_accountitem_comments', ['accountitem_id', 'comment_id'])


    def backwards(self, orm):
        # Deleting model 'AccountItem'
        db.delete_table('accounts_accountitem')

        # Removing M2M table for field attachedfiles on 'AccountItem'
        db.delete_table('accounts_accountitem_attachedfiles')

        # Removing M2M table for field comments on 'AccountItem'
        db.delete_table('accounts_accountitem_comments')


    models = {
        'accounts.accountitem': {
            'Meta': {'object_name': 'AccountItem'},
            'account': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'attachedfiles': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ticket.File']", 'symmetrical': 'False'}),
            'balancewhendrawn': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ticket.Comment']", 'symmetrical': 'False'}),
            'createdby': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['members.Member']"}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'submittedtime': ('django.db.models.fields.DateTimeField', [], {}),
            'ticket': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ticket.Ticket']"}),
            'transactionwith': ('django.db.models.fields.TextField', [], {}),
            'uid': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
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

    complete_apps = ['accounts']