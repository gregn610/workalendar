# -*- coding: utf-8 -*-
from workalendar.core import WesternCalendar, ChristianMixin


class Estonia(WesternCalendar, ChristianMixin):
    "Estonia"
    include_good_friday = True
    include_easter_sunday = True
    include_whit_sunday = True
    whit_sunday_label = 'Nelipühade 1. püha'
    include_christmas_eve = True
    include_christmas = True
    include_boxing_day = True
    boxing_day_label = "Teine jõulupüha"

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (2, 24, "Independence Day"),
        (5, 1, "Kevadpüha"),
        (6, 23, "Võidupüha"),
        (6, 24, "Jaanipäev"),
        (8, 20, "Taasiseseisvumispäev")
    )

    def get_fixed_holidays(self, year):
        """Return the fixed days according to the FIXED_HOLIDAYS class property
        """
        days = []
        # EE Independence
        if year >= 1991:
            return super(Estonia, self).get_fixed_holidays(year)
        return days
