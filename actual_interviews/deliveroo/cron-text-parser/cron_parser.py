import sys
from exceptions import InvalidCronString
from cron_element import CronElement
from cron_element_type import CronElementType

class CronParser:
    def __init__(self) -> None:
        self.minutesElem: CronElement
        self.hoursElem: CronElement
        self.dayOfMonthElem: CronElement
        self.monthsElem: CronElement
        self.dayOfWeekElem: CronElement

    def parse(self, cronStr: str) -> str:
        cronStrElements = cronStr.split(" ")
        if len(cronStrElements) != 6:
            raise InvalidCronString(f"{cronStr} does not have required 5 elements")

        minutes, hour, dayOfMonth, month, dayOfWeek, command = cronStrElements
        self.minutesElem = CronElement(minutes, CronElementType.MINUTES)
        self.hoursElem = CronElement(hour, CronElementType.HOURS)
        self.dayOfMonthElem = CronElement(dayOfMonth, CronElementType.DAY_OF_MONTH)
        self.monthsElem = CronElement(month, CronElementType.MONTH)
        self.dayOfWeekElem = CronElement(dayOfWeek, CronElementType.DAY_OF_WEEK)

        return '\n'.join([
            "minutes       {}".format(self.minutesElem.decode()),
            "hours         {}".format(self.hoursElem.decode()),
            "day of month  {}".format(self.dayOfMonthElem.decode()),
            "month         {}".format(self.monthsElem.decode()),
            "day of week   {}".format(self.dayOfWeekElem.decode()),
            "command       {}".format(command)
        ])


def runner() -> None:
    cron_string = sys.argv[1]

    cronParser: CronParser = CronParser()
    parsed_value: str = cronParser.parse(cron_string)
    print(parsed_value)


if __name__ == "__main__":
    runner()
