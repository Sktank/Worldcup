# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Stadium.longitude'
        db.alter_column(u'home_stadium', 'longitude', self.gf('django.db.models.fields.FloatField')())

        # Changing field 'Stadium.latitude'
        db.alter_column(u'home_stadium', 'latitude', self.gf('django.db.models.fields.FloatField')())

    def backwards(self, orm):

        # Changing field 'Stadium.longitude'
        db.alter_column(u'home_stadium', 'longitude', self.gf('django.db.models.fields.IntegerField')())

        # Changing field 'Stadium.latitude'
        db.alter_column(u'home_stadium', 'latitude', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'home.stadium': {
            'Meta': {'object_name': 'Stadium'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'seats': ('django.db.models.fields.IntegerField', [], {})
        },
        u'home.team': {
            'Meta': {'object_name': 'Team'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'group': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '50'}),
            'manager': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'population': ('django.db.models.fields.IntegerField', [], {'default': '30000000'}),
            'rank': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['home']