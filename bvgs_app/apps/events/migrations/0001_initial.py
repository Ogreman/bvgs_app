# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'events_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('starts', self.gf('django.db.models.fields.DateTimeField')()),
            ('ends', self.gf('django.db.models.fields.DateTimeField')()),
            ('capacity', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('last_event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Event'], null=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['Event'])

        # Adding model 'EventPlayer'
        db.create_table(u'events_eventplayer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Event'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['players.Player'])),
            ('exp_given', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'events', ['EventPlayer'])

        # Adding unique constraint on 'EventPlayer', fields ['event', 'player']
        db.create_unique(u'events_eventplayer', ['event_id', 'player_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'EventPlayer', fields ['event', 'player']
        db.delete_unique(u'events_eventplayer', ['event_id', 'player_id'])

        # Deleting model 'Event'
        db.delete_table(u'events_event')

        # Deleting model 'EventPlayer'
        db.delete_table(u'events_eventplayer')


    models = {
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'attendees': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['players.Player']", 'through': u"orm['events.EventPlayer']", 'symmetrical': 'False'}),
            'capacity': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'ends': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'starts': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'events.eventplayer': {
            'Meta': {'unique_together': "(('event', 'player'),)", 'object_name': 'EventPlayer'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            'exp_given': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['players.Player']"})
        },
        u'players.player': {
            'Meta': {'ordering': "['-level', 'name']", 'object_name': 'Player'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'exp': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'multiplier': ('django.db.models.fields.DecimalField', [], {'default': '1.0', 'max_digits': '10', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        }
    }

    complete_apps = ['events']