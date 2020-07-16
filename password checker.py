import requests
import hashlib
import sys
def request_api_data(query_char):
    url='https://api.pwnedpasswords.com/range/'+query_char
    res=requests.get(url)
    if res.status_code!=200:
        print("error in status code")
    return res
def getpasswordleakcounts(hashes,hashestocheck):
    hashes=(line.split(':') for line in hashes.text.splitlines())
    for i,t in hashes:
        if i==hashestocheck:
            return t
    return 0




def pwned_api_check(password):
    sha1password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    frst5char=sha1password[:5]
    tail=sha1password[5:]
    response=request_api_data(frst5char)
    return getpasswordleakcounts(response,tail)
def dd():
    c=input("write the password")
    d=pwned_api_check(c)
    print(f'your password is hacked{d} time')

dd()

