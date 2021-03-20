import requests

IPINFO_URL = 'http://ipinfo.io/{ip}/json'


def get_ip_country(ip_address):
    """Receives ip address string, use IPINFO_URL to get geo data,
       parse the json response returning the country code of the IP"""
    r = requests.get(IPINFO_URL.format(ip=ip_address))
    r.raise_for_status()
    try:
        res = r.json()
        return res['country']
    except ValueError as err:
        pass



print(get_ip_country('84.237.165.153'))
