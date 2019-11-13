import re

def valid_email(email):
    try:
        emails = re.search('\w{4,}([-.]\w+)*@\w+([-.]\w+)*\.(?!server)(?!net1)(?!coma)(br|com|net|in|az)', email).group()
        emails = True
    except:
        emails = False
    return emails


def filter_email(emails):
    total_email = []
    for e in emails:
        email = valid_email(e)
        if email == True:
            total_email.append(e)
        else:
            continue
    return total_email

