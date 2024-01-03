# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from log import *
import random
import smtplib
import copy


def matching(people):
    first_random = copy.deepcopy(people)
    snata_dict = dict()
    flag = True
    while flag:
        undone_match_list = list()
        random.shuffle(first_random)
        random.shuffle(people)
        for i in range(0, len(first_random)):
            if first_random[i] == people[i]:
                undone_match_list.append(first_random[i])
                break
        if not undone_match_list:
            flag = False
            for k in range(0, len(first_random)):
                snata_dict.setdefault(first_random[k], people[k])
    print(snata_dict)
    return snata_dict


def send(to_address, email_msg):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('mizuno870515@gmail.com', 'cjlaqwypjecwdekg')
    from_address = 'mizuno870515@gmail.com'
    status = smtp.sendmail(from_address, to_address, email_msg)
    smtp.quit()
    if status == {}:
        logmsg('mail sending result: Success')
        return True
    else:
        logmsg('mail sending result: Fail')
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        msg, content = '', ''
        p_num = input('How any people are participated?\n')
        # -*- coding: UTF-8 -*-
        if p_num.isdigit():
            match_dict = dict()
            name_list = list()
            for p in range(0, int(p_num)):
                temp_name = input('Name: ')
                temp_email = input('Email: ')
                name_list.append(temp_name)
                match_dict.setdefault(temp_name, temp_email)

            msg = 'match map: {}'.format(match_dict)
            logmsg(msg)
            snata = matching(name_list)
            for key in match_dict:
                to_email = match_dict[key]
                content = "Subject:Your Santa Result\nHey {} you are {}'s santa!\nDon't forget!\nBest regards.".format(key, snata[key])
                if send(to_email, content):
                    logmsg('Done!')
                else:
                    logmsg('Oops... Something went wrong')
        else:
            logmsg('Please type in an integer')

    except Exception as e:
        logError('__main__: {}'.format(str(e)))


