import decimal

from django.db import models

from .managers import PlayerManager, BASE_EXP_AMOUNT


MULT_INCREASE = decimal.Decimal(1.1)
MULT_CONSECUTIVE = decimal.Decimal(1.12)


class Player(models.Model):

    '''Model defining a BVGS member and their stats'''

    name = models.CharField(max_length=120)
    level = models.PositiveIntegerField(default=0)
    exp = models.PositiveIntegerField(default=0)
    multiplier = models.DecimalField(decimal_places=2, max_digits=10, default=1.0)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = PlayerManager()

    def attend_event(self):
        self.exp += self.next_exp_amount

    def increase_multiplier(self):
        self.multiplier = round(self.multiplier * MULT_INCREASE, 2)

    def increase_multiplier_consecutive(self):
        self.multiplier = round(self.multiplier * MULT_CONSECUTIVE, 2)

    def calculate_level(self):
        for level, exp in enumerate(Player.objects.exp_table):
            self.req_exp = exp - self.exp
            if exp > self.exp:
                self.level = level
                break
        return self.level

    @property
    def next_exp_amount(self):
        if self.exp:
            return int(BASE_EXP_AMOUNT * (self.multiplier * MULT_INCREASE))
        else:
            return BASE_EXP_AMOUNT * self.multiplier

    def __str__(self):
        return self.name

    def save(self, *args, **kargs):
        self.calculate_level()
        super(Player, self).save(*args, **kargs)

    class Meta:
        ordering = ['-level', 'name']