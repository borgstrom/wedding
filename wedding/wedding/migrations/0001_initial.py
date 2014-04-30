# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Invitation'
        db.create_table(u'wedding_invitation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('guests', self.gf('django.db.models.fields.IntegerField')()),
            ('responded', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'wedding', ['Invitation'])

        # Adding model 'Person'
        db.create_table(u'wedding_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('invitation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='people', to=orm['wedding.Invitation'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('attending', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('dietary_restrictions', self.gf('django.db.models.fields.TextField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'wedding', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Invitation'
        db.delete_table(u'wedding_invitation')

        # Deleting model 'Person'
        db.delete_table(u'wedding_person')


    models = {
        u'wedding.invitation': {
            'Meta': {'object_name': 'Invitation'},
            'guests': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'responded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'wedding.person': {
            'Meta': {'object_name': 'Person'},
            'attending': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'dietary_restrictions': ('django.db.models.fields.TextField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invitation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'people'", 'to': u"orm['wedding.Invitation']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['wedding']