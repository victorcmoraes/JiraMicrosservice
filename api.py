import requests
from requests.auth import HTTPBasicAuth
import json

auth = HTTPBasicAuth('victor.moraes@squadhub.com.br', 'ATATT3xFfGF0tcU6lt36oCRAXnfzXzEFAkfyHUn3pvXw6m8tvmY9kTKuo4lf5m8ZUNkhV3QyEAbpAaG_bS4ucrBixpSbi8sSd1H2msCflbLvDaO1b6T2lL6O670_ZMMXMGZP-D_OMvk9qNYVB59TRBC08P95P7MdgufZV1ZjB4a_cpKAjqJu4vQ=1A123A11')

url = 'https://course-example.atlassian.net/rest/api/3/issue'

headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

payload = json.dumps( {
    "fields": {
        "project": {
            "key": "KAN"
        },
        "summary": "hello world",
        "description": {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [
                        {
                            "text": "Detalhes apenas",
                            "type": "text"
                        }
                    ]
                }
            ]
        },
        "issuetype": {
            "name": "Tarefa"
        },  
        
        "duedate": "2020-12-01",  
        
    }
} )

response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))