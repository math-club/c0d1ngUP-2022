import requests
import time
import re
import json

__version__ = "1.2a"


class DefisUrl():
    def __init__(self, urlget, urlpost=None, debug=False, proxy=None, verify=False):
        self.urlget = urlget
        self.urlpost = urlpost
        self.signature = None
        self.text = None
        self.debug = debug
        self.proxies = dict()
        self.verify = verify
        if proxy is not None:
            self.proxies['http'] = proxy
            self.proxies['https'] = proxy
        if self.urlpost == None:
            self.urlpost = re.sub('/get/', '/post/', self.urlget)

    def get(self):
        question = requests.get(
            self.urlget, verify=self.verify, proxies=self.proxies)
        if self.debug:  # on peut afficher le code de retour de la requête :
            print('GET:', question)
            # et le texte récupéré (qui contient la signature et l'énoncé) :
            print('TEXT:', question.text)
        # on sépare les lignes de l'entrée
        #print(lignes)
        # la première ligne contient la signature
        return question.text

    def post(self, reponse):
        res = requests.post(self.urlpost, verify=self.verify,
                            data={"sig": self.signature, "rep": reponse},
                            proxies=self.proxies)
        if self.debug:
            print(res)
            print(res.text)
        return res.text

# d = DefisUrl('https://api.blockcypher.com/v1/btc/main/blocks/600996',
#              verify=True)
# string = d.get()

# print(string)

# block = json.JSONDecoder().decode(s=string)

# print(block["txids"][1])

with open("netwatch", "r") as f:
    lines = list(map(lambda x: x.strip().split(","), f.readlines()))


hash_list = []
for elem in lines:
    string = DefisUrl(f'https://api.blockcypher.com/v1/btc/main/blocks/{elem[0]}', verify=True).get()
    block = json.JSONDecoder().decode(s=string)
    print(block)
    hash_list.append(block["txids"][int(elem[1])])
    print(hash_list)

    print(len(hash_list))

print(hash_list)
