from django.db import models

from .managers import PlayerManager, BASE_EXP_AMOUNT


# Models
class Player(models.Model):

    '''Model defining a BVGS member and their stats'''

    name = models.CharField(max_length=120)
    level = models.PositiveIntegerField(default=0)
    exp = models.PositiveIntegerField(default=0)
    multiplier = models.DecimalField(decimal_places=2, max_digits=10, default=1.0)
    # events = models.ManyToManyField(event)
    # date_joined = models.DateTimeField()
    # date_modified = models.DateTimeField()

    objects = PlayerManager()

    def attend_event(self):
        self.exp += self.next_exp_amount

    def increase_multiplier(self):
        self.multiplier = round(self.multiplier * 1.1, 2)

    def increase_multiplier_consecutive(self):
        self.multiplier = round(self.multiplier * 1.12, 2)

    def calculate_level(self):
        for level, exp in enumerate(Player.objects.exp_table):
            self.req_exp = exp - self.exp
            if exp > self.exp:
                self.level = level
                break
        return self.level

    @property
    def next_exp_amount(self):
        return int(BASE_EXP_AMOUNT * (self.multiplier * 1.1))

    def __unicode__(self):
        return self.name

    def save(self, *args, **kargs):
        self.calculate_level()
        super(Player, self).save(*args, **kargs)