from numpy import NaN
import pandas as pd
import sys
import math

def std(data, mean, len):
    ret = 0
    for d in data:
        if math.isnan(d) is False:
            ret = ret + (d - mean)**2
    return math.sqrt((ret / len))

def get_percentile(data, len, per):
    i = (per/100) * (len)
    if i.is_integer():
        return data[int(i) - 1]
    else:
        i_up = math.ceil(i) - 1
        return data[i_up]

def describe(data, i):
    if i < 6:
        return -1
    describe = {
        'Count': 0,
        'Mean':0,
        'Std':0,
        'Min': NaN,
        '25%':0,
        '50%':0,
        '75%':0,
        'Max': NaN,
    }
    check = []
    for d in data:
        if math.isnan(d) is False:
            describe['Mean'] = d + describe['Mean']
            check.append(d)
            if math.isnan(describe['Min']) or describe['Min'] > d:
                describe['Min'] = d
            if math.isnan(describe['Max']) or describe['Max'] < d:
                describe['Max'] = d
            describe['Count'] += 1
    describe['Mean'] = describe['Mean'] / (describe['Count'])
    describe['Std'] = std(data, describe['Mean'], describe['Count'])
    check = sorted(check)
    describe['25%'] = get_percentile(check, describe['Count'], 25)
    describe['50%'] = get_percentile(check, describe['Count'], 50)
    describe['75%'] = get_percentile(check, describe['Count'], 75)
    return describe

if __name__ == '__main__':
    result = pd.read_csv(sys.argv[1])
    count = 0
    i = 0
    result_describe = {}
    for features in result.columns:
        description = describe(result[features], i)
        i = i + 1
        if description != -1:
            result_describe[features] = description
    df = pd.DataFrame(result)
    print(pd.DataFrame(result_describe))
