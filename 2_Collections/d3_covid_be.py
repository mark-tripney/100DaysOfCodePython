from collections import Counter
from collections import defaultdict
from collections import namedtuple
import csv

covid_data = "COVID19BE_CASES_AGESEX.csv"
Case = namedtuple("Case", "date province region age_group sex cases")


def filter_cases_by_province(data=covid_data):
    cases_be = defaultdict(list)
    with open(data) as file:
        for line in csv.DictReader(file):
            try:
                date = line["DATE"]
                province = line["PROVINCE"]
                region = line["REGION"]
                age_group = line["AGEGROUP"]
                sex = line["SEX"]
                cases = int(line["CASES"])
            except ValueError:
                continue

            c = Case(
                date=date,
                province=province,
                region=region,
                age_group=age_group,
                sex=sex,
                cases=cases,
            )
            cases_be[province].append(c)

    return cases_be


cases_be = filter_cases_by_province(covid_data)
counter = Counter()

for province, cases in cases_be.items():
    counter[province] += len(cases)

print(counter.most_common(5))