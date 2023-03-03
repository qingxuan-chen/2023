import sys
class DateFormat:
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    def out_date(self):
        return f"输入的时间为{self.year}-{self.month}-{self.day}"

    @classmethod
    def json_format(cls, json_data):
        year, month, day = json_data["year"], json_data["month"], json_data["day"]
        return cls(year, month, day)


# year, month, day = 2023, 3, 2
json_data = {"year": 2023, "month": 3, "day": 2}
# demo = DateFormat(year, month, day)
demo2 = DateFormat.json_format(json_data)
# print(demo.out_date())
print(demo2.out_date())

print(sys.path)