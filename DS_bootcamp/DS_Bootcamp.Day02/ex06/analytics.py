import sys
import os
import logging
import requests
import json
from random import randint
from config import num_of_steps, report_template, token, id

class Research:
    def __init__(self):
        logging.basicConfig(filename='analytics.log', level=logging.INFO, 
                    format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        file = sys.argv[1]
        if os.path.isfile(file):
            self.data = self.file_reader(file)
            logging.info('File opened')
        else:
            raise Exception('File path does not exist')
    
    def file_reader(self, file, has_header=True):
        with open(file, "r") as f:
            lines = f.readlines()
        logging.info('Reading file')
        if all(cell.isalpha() for cell in lines[0].strip().split(',')):
            lines = lines[1:]
            logging.info('Removing header')
        content = [list(map(int, line.strip().split(','))) for line in lines]
        return content
    
    def telegram(self, message):
        url = f'https://api.telegram.org/bot{token}/sendMessage'
        url2 = f'https://api.telegram.org/bot{token}/getUpdates'
        payload = {
            "chat_id": id,
            "text": message
        }
        response = requests.post(url, data=payload)
        logging.info('Sending message to telegram')
        return response.json()
    
    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self, content):
            heads = sum(row[0] for row in content)
            tails = sum(row[1] for row in content)
            logging.info(f'heads={heads}, tails={tails}')
            return heads, tails
            
        def fractions(self, heads, tails):
            total = heads + tails
            headratio = heads/total*100
            tailsratio = tails/total*100
            logging.info(f'heads fraction={headratio:.2f}, tails fraction={tailsratio:.2f}')
            return(headratio, tailsratio)
        
class Analytics(Research.Calculations):
    def predict_random(self, num_predict):
        pred = []
        for _ in range(num_predict):
            rand = randint(0,1)
            pred.append([rand, 1 - rand])
        logging.info('creating prediction')
        return pred
    
    def pred_count(self, pred):
        heads = sum(row[0] for row in pred)
        tails = sum(row[1] for row in pred)
        logging.info(f'Prediction count: heads={heads}, tails={tails}')
        return heads, tails
        
    def predict_last(self):
        logging.info('Last throw')
        return self.data[-1]
    
    def save_file(self, data, file, extention):
        filepath = f'{file}.{extention}'
        with open(filepath, "w") as f:
            f.write(str(data))
        logging.info(f'Saving file to {file}')
        
    def report(self, data, counts, fractions, pred_count):

        report = report_template.format(
            total_count = len(data),
            tails = counts[1],
            heads = counts[0],
            tails_fraction = fractions[1],
            heads_fraction = fractions[0],
            num_of_steps = num_of_steps,
            predicted_tails = pred_count[1],
            predicted_heads = pred_count[0]
        )
        logging.info('Creating report')
        return report