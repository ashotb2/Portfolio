import sys
import os
import requests
import json
from random import randint
from analytics import Research, Analytics

if __name__ == '__main__':
    try:
        result = ""
        res = Research()
        data = res.data
        result += str(data)

        calc = res.Calculations(data)
        counts = calc.counts(data)
        result += str(counts)
        frac = calc.fractions(*counts)
        result += str(frac)

        analyt = Analytics(data)
        pred = analyt.predict_random(3)
        result += str(pred)

        pred_count = analyt.pred_count(pred)
        result += str(analyt.predict_last())
        result += str(analyt.report(data, counts, frac, pred_count))

        analyt.save_file(result, 'end', 'txt')
        res.telegram('The report has been successfully created')
    except Exception as e:
        print(e)
