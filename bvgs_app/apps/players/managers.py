from django.db import models


LEVELS = list(range(1, 90))
BASE_EXP_AMOUNT = 1000


class PlayerQuerySet(models.query.QuerySet):

    def are_active(self):
        return self.filter(active=True)


class PlayerManager(models.Manager):

    def get_query_set(self):
        return PlayerQuerySet(self.model, using=self._db)

    def are_active(self):
        return self.get_query_set().are_active()

    def create_player(self, name):
        player = self.create(name=name, level=0, exp=0, multiplier=0)
        return player

    @property
    def exp_table(self):
        if not hasattr(self, '_exp_table'):
            self._exp_table = [BASE_EXP_AMOUNT]
            for i in LEVELS:
                self._exp_table.append(
                    int(self._exp_table[i - 1] + BASE_EXP_AMOUNT * (i / 10.0))
                )
        return self._exp_table