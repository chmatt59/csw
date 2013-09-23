# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Nonconformity.problem'
        db.add_column(u'qt_nonconformity', 'problem',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['qt.Problem'], null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field cost on 'Nonconformity'
        m2m_table_name = db.shorten_name(u'qt_nonconformity_cost')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('nonconformity', models.ForeignKey(orm[u'qt.nonconformity'], null=False)),
            ('cost', models.ForeignKey(orm[u'qt.cost'], null=False))
        ))
        db.create_unique(m2m_table_name, ['nonconformity_id', 'cost_id'])


    def backwards(self, orm):
        # Deleting field 'Nonconformity.problem'
        db.delete_column(u'qt_nonconformity', 'problem_id')

        # Removing M2M table for field cost on 'Nonconformity'
        db.delete_table(db.shorten_name(u'qt_nonconformity_cost'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'qt.action': {
            'Meta': {'object_name': 'Action'},
            'actor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['qt.Actor']"}),
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'external_reference': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['qt.Problem']"}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['qt.Status']"}),
            'target': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['qt.Target']"})
        },
        u'qt.actor': {
            'Meta': {'object_name': 'Actor'},
            'email_a': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'email_cc': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'email_cci': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'qt.cost': {
            'Meta': {'object_name': 'Cost'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['qt.CostCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'qt.costcategory': {
            'Meta': {'object_name': 'CostCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'qt.nonconformity': {
            'Meta': {'object_name': 'Nonconformity'},
            'assigned': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'assigned_tickets'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'created_tickets'", 'to': u"orm['auth.User']"}),
            'cost': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['qt.Cost']", 'null': 'True', 'blank': 'True'}),
            'date_creation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_short': ('django.db.models.fields.TextField', [], {}),
            'expected': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'observers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'observed_tickets'", 'blank': 'True', 'to': u"orm['auth.User']"}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['qt.Problem']", 'null': 'True', 'blank': 'True'}),
            'reproduction': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['qt.Status']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'qt.problem': {
            'Meta': {'object_name': 'Problem'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'root_cause': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['qt.Status']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'qt.status': {
            'Meta': {'ordering': "['order']", 'object_name': 'Status'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'qt.target': {
            'Meta': {'object_name': 'Target'},
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['qt.Status']"})
        }
    }

    complete_apps = ['qt']