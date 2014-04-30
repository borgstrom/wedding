# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Invitation.guests'
        db.delete_column(u'wedding_invitation', 'guests')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Invitation.guests'
        raise RuntimeError("Cannot reverse this migration. 'Invitation.guests' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Invitation.guests'
        db.add_column(u'wedding_invitation', 'guests',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


    models = {
        u'wedding.invitation': {
            'Meta': {'object_name': 'Invitation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'responded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'wedding.person': {
            'Meta': {'object_name': 'Person'},
            'attending': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'dietary_restrictions': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invitation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'people'", 'to': u"orm['wedding.Invitation']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['wedding']