class make_month(object):

    def __init__(self, year, month):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        diff = year - 2000
        num_days = diff % 7
        if year > 2000:
            num_days += (diff >> 2) + 1
        assert month > 0
        num_days += sum(days[:month-1])
        self.week = ["Su", "Mo", "Tu", "We", "Th", "Fr", "Sa"]
        self.days = num_days % 7
        self.month = month

    def day(self, x):
        y = (self.days + x + 5) % 7
        return self.week[y]


def test_day():
    a = make_month(2000, 2)
    assert a.day(1) == "Tu"
    a = make_month(2014, 2)
    assert a.day(1) == "Sa"
    assert a.day(14) == "Fr"
    a = make_month(2015, 10)
    assert a.day(5) == "Mo"
    a = make_month(2016, 10)
    assert a.day(5) == "We"
    print "tests pass"


if __name__ == "__main__":
    test_day()