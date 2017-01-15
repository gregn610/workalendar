# -*- coding: utf-8 -*-
from datetime import date
from workalendar.core import WesternCalendar, ChristianMixin, SUN


class Lithuania(WesternCalendar, ChristianMixin):
    "Lithuania"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (2, 16,  "Day of Restoration of the State of Lithuania"),
        (5,  1,  "International Working Day"),
        (6, 24, "St. John's Day"),
        (7,  6, "Statehood Day"),
    )

    include_easter_sunday = True
    include_easter_monday = True
    include_assumption = True
    include_all_saints = True
    include_christmas_eve = True
    include_christmas = True
    include_boxing_day = True
    boxing_day_label = 'Christmas Day'

    def get_mothers_day(self, year):
        actual_date = self.get_nth_weekday_in_month(year, 5, SUN, n=1)
        return (actual_date, "Mother's Day")

    def get_fathers_day(self, year):
        actual_date = self.get_nth_weekday_in_month(year, 6, SUN, n=1)
        return (actual_date, "Father's Day")

    def get_independence_day(self, year):
        """Might reutn empty so use with .extend()"""
        days = []
        if year > 1990:
            days = [(date(year, 3, 11), "Restoration of Independence")]
        return days

    def get_variable_days(self, year):
        days = super(Lithuania, self).get_variable_days(year)
        days.append(self.get_mothers_day(year))
        days.append(self.get_fathers_day(year))
        days.extend(self.get_independence_day(year))
        return days
