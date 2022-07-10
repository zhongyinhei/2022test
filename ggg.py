class Date:

    def __init__(self, year, month, day):

        self.year = year

        self.month = month

        self.day = day

    @classmethod

    def now(cls):
        import time
        t = time.localtime()

        return cls(t.tm_year, t.tm_mon, t.tm_mday)

    def __str__(self):

        return '%s-%s-%s' % (self.year, self.month, self.day)

e = Date.now()

print(e)


class Date:

    def __init__(self, year, month, day):

        self.year = year

        self.month = month

        self.day = day

    @staticmethod

    def now():

        t = time.localtime()

        return Date(t.tm_year, t.tm_mon, t.tm_mday)

    def __str__(self):

        return '%s-%s-%s' % (self.year, self.month, self.day)

e = Date.now()

print(e)

