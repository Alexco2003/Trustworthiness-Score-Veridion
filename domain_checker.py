import whois
from datetime import datetime

def domainChecker(domain, year_founded=None):
    total = 0
    value = 1
    try:
        w = whois.whois(domain)
        creation_date, expiration_date = w.creation_date, w.expiration_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]
        registration_period = expiration_date.year - creation_date.year
        if registration_period < 1:
            total += value
        domain_creation_year = creation_date.year
        if domain_creation_year != year_founded:
            total += value
    except Exception as e:
        return str(e)
    return total

def main():
    print(domainChecker('rootsag.in', 2019))
    print(domainChecker('harborsidefarms.com', 1923))

if __name__ == '__main__':
    main()

# Change value to make sense