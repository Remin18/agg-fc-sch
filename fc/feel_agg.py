# -*- coding: utf-8 -*-
import requests
import itertools
import datetime
import ConfigParser

HEADERS = {
    'content-type': 'application/x-www-form-urlencoded',
    'cookie' : 'Paste here'
}

RESERVE_URL = 'https://www.feelcycle.com/feelcycle_reserve/reserve.php'

class STATUS_CODE:
    NEXT = 0
    END = 1

def main():
    now = datetime.datetime.now()

    conf = ConfigParser.SafeConfigParser()
    conf.read('./config.txt')
    joindate_str = conf.get('settings', 'joindate')
    tenpo = conf.get('settings', 'tenpo_ids')

    joindate = datetime.datetime.strptime(joindate_str, '%Y/%m/%d')
    tenpo_ids = tenpo.split(',')

    aggdate = joindate - datetime.timedelta(days=7)

    prg_dict = {}
    ins_dict = {}

    status = STATUS_CODE.NEXT

    while (status == STATUS_CODE.NEXT):
        for tenpoid in [int(tnp) for tnp in tenpo_ids]:
            data = {
                'tenpo' : tenpoid,
                'lesson' : 0,
                'teacher' : 0,
                'setdate' : aggdate.strftime('%Y/%m/%d'),
                'selectweek': 'next',
                'ref' : '',
            }

            status = aggregate_fc(now, data, prg_dict, ins_dict, aggdate)

        aggdate += datetime.timedelta(days=7)

    for key, val in sorted(prg_dict.items(), key=lambda x:x[1], reverse=True):
        print key, val

    for key, val in sorted(ins_dict.items(), key=lambda x:x[1], reverse=True):
        print key, val

def aggregate_fc(now, data, prg_dict={}, ins_dict={}, aggdate=None):

    if aggdate is None:
        return

    response = requests.post(RESERVE_URL, data=data, headers=HEADERS)
    phptext = response.text.encode('utf_8')

    is_reserved = False
    for line in phptext.splitlines():
        if 'title_week' in line:
            day = get_item(line)[:-8]
            day = '%s/%s' % (aggdate.year, day)
            if datetime.datetime.strptime(day, '%Y/%m/%d') > now:
                return STATUS_CODE.END

        if is_reserved:
            ins = get_item(line)
            print ins
            if ins in ins_dict:
                ins_dict[ins] += 1
            else:
                ins_dict[ins] = 1

            is_reserved = False

        if line.find("BE7980") >= 0:
            prg = get_item(line)
            print prg
            if prg in prg_dict:
                prg_dict[prg] += 1
            else:
                prg_dict[prg] = 1

            is_reserved = True

    return STATUS_CODE.NEXT

def get_item(text):
    start = text.find(">") + 1
    end = text.find("</")
    return text[start:end]

if __name__ == "__main__":
    main()
