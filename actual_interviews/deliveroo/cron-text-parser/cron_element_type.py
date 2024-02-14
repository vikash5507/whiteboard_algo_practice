
class CronElementType:
    """
        CronElementType with fixed Min and Max value
    """
    MINUTES = (0, 59)
    HOURS = (0, 23)
    DAY_OF_MONTH = (1, 31)
    MONTH = (1, 12)
    DAY_OF_WEEK = (1, 7)
    YEAR = (1970, 2099)
