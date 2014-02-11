# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Stadium'
        db.create_table(u'home_stadium', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('seats', self.gf('django.db.models.fields.IntegerField')()),
            ('latitude', self.gf('django.db.models.fields.IntegerField')()),
            ('longitude', self.gf('django.db.models.fields.IntegerField')()),
            ('image_url', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'home', ['Stadium'])

        # Adding field 'Team.image_url'
        db.add_column(u'home_team', 'image_url',
                      self.gf('django.db.models.fields.CharField')(default='none', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Stadium'
        db.delete_table(u'home_stadium')

        # Deleting field 'Team.image_url'
        db.delete_column(u'home_team', 'image_url')


    models = {
        u'home.stadium': {
            'Meta': {'object_name': 'Stadium'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'latitude': ('django.db.models.fields.IntegerField', [], {}),
            'longitude': ('django.db.models.fields.IntegerField', [], {}),
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