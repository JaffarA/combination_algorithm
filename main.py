from csv import reader
from pprint import pprint
from itertools import product
from datetime import datetime

reader = reader(open('MOCK_DATA.csv'))
db = []

for row in reader:
    db.append({
        'id': len(db),
        'product': row[0],
        'pet_sex': row[1],
        'pet_name': row[2],
        'pet_age': row[3]
    })


def get_value_set(table, target):
    """Returns a set (unique) of values for a target"""
    s = set()
    [s.add(entry[target]) for entry in table]
    return s


def factor_combinations(table, factors_list, skip_zero=True):
    """
    Returns a list with all possible combinations of values for a table based\n
    on the values present in factors_list. \n
    Optional parameter 'skip_zero' skips values where the total is 0.
    """

    filtered_table = []
    for entry in table:
        r = []
        for f in factors_list:
            r.append(entry[f])
        filtered_table.append(r)

    factors_value_list = []
    [factors_value_list.append(get_value_set(table, f)) for f in factors_list]

    result = [factors_list]
    result[0].append('total')

    combinations = product(*factors_value_list)
    for template in combinations:
        template_list = [v for v in template]
        t = 0
        for entry in filtered_table:
            if entry == template_list:
                t += 1
        if skip_zero == True:
            if t == 0:
                pass
            else:
                template_list.append(t)
                result.append(template_list)
        else:
            template_list.append(t)
            result.append(template_list)

    return result


if __name__ == "__main__":

    timestart = datetime.now()

    result = factor_combinations(
        db,
        ['product', 'pet_sex', 'pet_age']
    )

    timeend = datetime.now()

    pprint(result)

    difference = timeend - timestart
    print(f'Time taken: {difference.seconds}s.')
