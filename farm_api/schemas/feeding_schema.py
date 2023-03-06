
class FeedingSchema(object):
    amount_kg : int
    cron_schedule: str
    last_measured: str

    def __json__(self) :
        return self.__dict__

