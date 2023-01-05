import re

def match_postgres_con_regex(con_url):
    check = re.fullmatch('^postgresql://.*[a-z0-9]+:[a-z0-9]+@([a-z\.]+|[0-9\.]+)/[A-z]+', con_url)
    return True if check else False
