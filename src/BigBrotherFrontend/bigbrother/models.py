'''
Created on Feb 26, 2011

@author: gpmidi
'''
import datetime
from django.db import models

class Bbdata(models.Model):
    id = models.IntegerField(
                             primary_key = True,
                             verbose_name = "PK",
                             help_text = "A unique identifier for the log line",
                             editable = False,
                             )
    date = models.IntegerField(
                               verbose_name = "Date/Time",
                               help_text = "The number of seconds since Unix epoc that the data point was collected",
                               editable = False,
                               )
    player = models.CharField(
                              max_length = 96,
                              verbose_name = "Player",
                              help_text = "The player that caused the event",
                              )
    action = models.IntegerField(
                                 verbose_name = "Action",
                                 choices = (
                                            (0, "BLOCK_BROKEN"),
                                            (1, "BLOCK_PLACED"),
                                            (2, "DESTROY_SIGN_TEXT"),
                                            (3, "TELEPORT"),
                                            (4, "DELTA_CHEST"),
                                            (5, "COMMAND"),
                                            (6, "CHAT"),
                                            (7, "DISCONNECT"),
                                            (8, "LOGIN"),
                                            (9, "DOOR_OPEN"),
                                            (10, "BUTTON_PRESS"),
                                            (11, "LEVER_SWITCH"),
                                            (12, "CREATE_SIGN_TEXT"),
                                            (13, "LEAF_DECAY"),
                                            (14, "FLINT_AND_STEEL"),
                                            (15, "TNT_EXPLOSION"),
                                            (16, "CREEPER_EXPLOSION"),
                                            (17, "MISC_EXPLOSION"),
                                            (18, "OPEN_CHEST"),
                                            (19, "BLOCK_BURN"),
                                            (20, "LAVA_FLOW"),
                                          ),
                                 )
    world = models.ForeignKey(
                              'Bbworlds',
                              db_column = 'world',
                              verbose_name = "World",
                              help_text = "",
                              )
    x = models.IntegerField(
                            verbose_name = "X",
                            )
    y = models.IntegerField(
                            null = True,
                            blank = True,
                            verbose_name = "Y",
                            help_text = "Height",
                            )
    z = models.IntegerField(
                            verbose_name = "Z",
                            )
    type = models.ForeignKey(
                               db_column = 'type',
                               'BlockType',
                               null = True,
                               blank = True,
                               verbose_name = "Block Type",
                               )
    data = models.CharField(
                            max_length = 1500,
                            default = '',
                            verbose_name = "Data",
                            )
    rbacked = models.BooleanField(
                                  verbose_name = "Backed Up",
                                  null = False,
                                  default = False,
                                  )
    class Meta:
        db_table = u'bbdata'
        
    def getDate(self):
        """ Return the dt as a datetime object """
        return datetime.datetime.fromtimestamp(self.date)

class Bbworlds(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 150)
    class Meta:
        db_table = u'bbworlds'

class BlockType(models.Model):
    id = models.BigIntegerField(
                                primary_key = True,
                                verbose_name = "ID",
                                help_text = "Block type ID number",
                                )
    name = models.CharField(
                            max_length = 255,
                            verbose_name = 'Name',
                            help_text = "Block type name",
                            )
    class Meta:
        db_table = u'items'
