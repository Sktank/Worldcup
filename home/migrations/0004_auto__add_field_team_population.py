# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Team.population'
        db.add_column(u'home_team', 'population',
                      self.gf('django.db.models.fields.IntegerField')(default=30000000),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Team.population'
        db.delete_column(u'home_team', 'population')


    models = {
        u'home.team': {
            'Meta': {'object_name': 'Team'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'group': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manager': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'population': ('django.db.models.fields.IntegerField', [], {'default': '30000000'}),
            'rank': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['home']