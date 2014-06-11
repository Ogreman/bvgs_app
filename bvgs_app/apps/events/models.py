from django.db import models


class Event(models.Model):

    name = models.CharField(max_length=120)
    starts = models.DateTimeField()
    ends = models.DateTimeField()
    capacity = models.PositiveIntegerField()
    attendees = models.ManyToManyField('players.Player', through="EventPlayer")
    last_event = models.ForeignKey('self', blank=True, null=True)

    def __str__(self):
        return self.name


class EventPlayer(models.Model):

    event = models.ForeignKey(Event)
    player = models.ForeignKey('players.Player')
    exp_given = models.BooleanField(default=False)

    class Meta:
        unique_together = ('event', 'player')

    def _increase_multiplier(self):
        if self.event.last_event is not None:
            if self.player in self.event.last_event.attendees.all():
                self.player.increase_multiplier_consecutive()
            else:
                self.player.increase_multiplier()
        else:
            self.player.increase_multiplier()

    def save(self, *args, **kargs):
        if self.id is None:
            self.player.attend_event()
            self._increase_multiplier()
            self.exp_given = True
            self.player.save()
        super(EventPlayer, self).save(*args, **kargs)