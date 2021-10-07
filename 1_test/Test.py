
import requests
import pytest

l = ['/posts','/comments','/albums']
@pytest.mark.parametrize('param', l)
def test_lin(param):
    link = f'https://jsonplaceholder.typicode.com{param}'
    r=requests.get(link)
    print(r.status_code)
    if r.status_code == 200:
        print("COOL")
    else:
        print('BUE')
    assert r.status_code == 200

#print(r.text)
# print(r.json())/albums for i in (1,2,3,4,5):
#     if i == 3:
#         print(i)
#     else:
#         print('jkb')
#
# count = 0
# while count<5:
#     count+=1
#     print(count)
# else:
#     print("blablala")

# with open('data.csv', 'r', encoding='1251') as t:
#     gen = (100*i for i in t)
#
#     for item in gen:
#         print(item)