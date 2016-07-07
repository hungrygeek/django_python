# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Comment.content_type'
        db.add_column('ticket_comment', 'content_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True),
                      keep_default=False)

        # Removing M2M table for field subcomments on 'Comment'
        db.delete_table('ticket_comment_subcomments')

        # Removing M2M table for field comments on 'Ticket'
        db.delete_table('ticket_ticket_comments')


    def backwards(self, orm):
        # Deleting field 'Comment.content_type'
        db.delete_column('ticket_comment', 'content_type_id')

        # Adding M2M table for field subcomments on 'Comment'
        db.create_table('ticket_comment_subcomments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_comment', models.ForeignKey(orm['ticket.comment'], null=False)),
            ('to_comment', models.ForeignKey(orm['ticket.comment'], null=False))
        ))
        db.create_unique('ticket_comment_subcomments', ['from_comment_id', 'to_comment_id'])

        # Adding M2M table for field comments on 'Ticket'
        db.create_table('ticket_ticket_comments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ticket', models.ForeignKey(orm['ticket.ticket'], null=False)),
            ('comment', models.ForeignKey(orm['ticket.comment'], null=False))
        ))
        db.create_unique('ticket_ticket_comments', ['ticket_id', 'comment_id'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'members.member': {
            'Meta': {'object_name': 'Member'},
            'bio': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200', 'blank': 'True'}),
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['ticket.File']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joindate': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
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
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True'}),
            'submittedby': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['members.Member']"}),
            'submittedtime': ('django.db.models.fields.DateTimeField', [], {}),
            'uid': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'})
        },
        'ticket.file': {
            'Meta': {'object_name': 'File'},
            'actualfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'createdby': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['members.Member']"}),
            'easyname': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'iconfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True'}),
            'iconlink': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'relfiles'", 'null': 'True', 'to': "orm['ticket.Icon']"}),
            'iconsource': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tags': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'ticket.icon': {
            'Meta': {'object_name': 'Icon'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'filetypes': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'ticket.ticket': {
            'Meta': {'object_name': 'Ticket'},
            'assignedto': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'tickets_assigned'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['members.Member']"}),
            'category': ('django.db.models.fields.CharField', [], {'default': "'GEN'", 'max_length': '3'}),
            'filedby': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['members.Member']"}),
            'filedtime': ('django.db.models.fields.DateTimeField', [], {}),
            'files': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['ticket.File']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incoming': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'outgoing': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'priority': ('django.db.models.fields.CharField', [], {'default': "'MD'", 'max_length': '2'}),
            'punts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['punts.Punt']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        }
    }

    complete_apps = ['ticket']