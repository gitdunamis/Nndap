import datetime

class FeedingSchema(object):
    amount_kg : int
    cron_schedule: str
    last_measured: datetime

    def __json__(self) :
        return self.__dict__

