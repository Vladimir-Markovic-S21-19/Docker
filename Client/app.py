import json
import http.client

conn = http.client.HTTPConnection("localhost:5000")
seed = json.dumps(
  {'ime': 'Vladimir',
  'prezime': 'Markovic',
  'username': 'vladimir',
  'smer': 'IT',
  'predmeti':
    [{'ime': 'Web sistemi i tehnologije', 'espb': 8},
     {'ime': 'Poslovni softver', 'espb': 8}
    ]}
)
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/users", seed, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
