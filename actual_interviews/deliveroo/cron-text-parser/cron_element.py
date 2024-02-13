from cron_element_type import CronElementType
from exceptions import InvalidRangeValueCronString, InvalidIntervalValueCronString, InvalidListValueCronString, InvalidCronString

class CronElement:
    def __init__(self, cron_elem_str: str, cron_elem_type: CronElementType):
        """
        Initialize CronElement object with the given cron element string and its type.

        :param cron_elem_str: The string representation of the cron element.
        :param cron_elem_type: The type of the cron element.
        """
        self.cron_elem_str = cron_elem_str
        self.cron_elem_type = cron_elem_type

    def decode(self) -> str:
        """
        Decode the cron element string into its individual values.

        :return: The decoded cron element values as a string.
        """
        # handle all value for datatype
        if self.cron_elem_str == "*":
            return self._decode_all_values()

        # handle range value
        if "-" in self.cron_elem_str:
            return self._decode_range()

        # handle intervals
        if self.cron_elem_str.startswith("*") and "/" in self.cron_elem_str:
            return self._decode_intervals()

        # handle list of values
        if "," in self.cron_elem_str:
            return self._decode_list_values()

        # handle single value
        return self._decode_single_value()

    def _decode_all_values(self) -> str:
        """
        Decode the cron element string representing all values.

        :return: The decoded cron element values as a string.
        """
        return " ".join(map(str, [v for v in range(self.cron_elem_type[0], self.cron_elem_type[1] + 1)]))

    def _decode_range(self) -> str:
        """
        Decode the cron element string representing a range of values.

        :return: The decoded cron element values as a string.
        """
        range_values = self.cron_elem_str.split("-")
        if len(range_values) != 2:
            raise InvalidRangeValueCronString(f"{self.cron_elem_str} does not have correct range values")
        else:
            try:
                start, end = int(range_values[0]), int(range_values[1])
                if start > end or start < self.cron_elem_type[0] or end > self.cron_elem_type[1]:
                    raise InvalidRangeValueCronString(f"{self.cron_elem_str} provided range is out of bound")
                return " ".join(map(str, range(start, end + 1)))
            except ValueError:
                raise InvalidRangeValueCronString(f"{self.cron_elem_str} does not have int type range values")

    def _decode_intervals(self) -> str:
        """
        Decode the cron element string representing intervals.

        :return: The decoded cron element values as a string.
        """
        interval_values = self.cron_elem_str.split("/")
        if len(interval_values) != 2:
            raise InvalidIntervalValueCronString(f"{self.cron_elem_str} does not have correct interval values")
        else:
            try:
                interval_val = int(interval_values[1])
                if interval_val == 0:
                    raise InvalidIntervalValueCronString(f"{self.cron_elem_str} has invalid interval value: "
                                                         f"{interval_val}")
                return " ".join(
                    map(str, [v for v in range(self.cron_elem_type[0], self.cron_elem_type[1] + 1)
                              if v % interval_val == 0])
                )
            except ValueError:
                raise InvalidIntervalValueCronString(f"{self.cron_elem_str} does not have int type interval value")

    def _decode_list_values(self) -> str:
        """
        Decode the cron element string representing a list of values.

        :return: The decoded cron element values as a string.
        """
        list_values = self.cron_elem_str.split(",")
        if len(list_values) <= 1:
            raise InvalidListValueCronString(f"{self.cron_elem_str} does not have enough list values")
        elif len(list_values) > (self.cron_elem_type[1] - self.cron_elem_type[0] + 1):
            raise InvalidListValueCronString(f"{self.cron_elem_str} have more values than expected for {self.cron_elem_type.__str__()}")
        else:
            try:
                list_int_values = [int(v) for v in list_values]
                return " ".join(map(str, [v for v in list_int_values]))
            except ValueError:
                raise InvalidListValueCronString(f"{self.cron_elem_str} does not all int values")

    def _decode_single_value(self) -> str:
        """
        Decode the cron element string representing a single value.

        :return: The decoded cron element values as a string.
        """
        try:
            single_val = int(self.cron_elem_str)
            if single_val < self.cron_elem_type[0] or single_val > self.cron_elem_type[1]:
                raise InvalidCronString(f"{self.cron_elem_str} provided range is out of bound")
            return self.cron_elem_str
        except ValueError:
            raise InvalidCronString(f"{self.cron_elem_str} is not valid")