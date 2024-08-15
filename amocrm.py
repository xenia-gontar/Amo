import requests
import logging
from requests.exceptions import JSONDecodeError

class AmoCRMWrapper:
    def _base_request(self, **kwargs):

	    access_token =  "Bearer " + ""

	    headers = {"Authorization": access_token}
	    req_type = kwargs.get("type")
	    response = ""
	    if req_type == "get":
	        try:
	            response = requests.get("https://test.amocrm.ru{}".format(kwargs.get("endpoint")), headers=headers).json()
	        except JSONDecodeError as e:
	            logging.exception(e)

	    elif req_type == "get_param":
	        url = "https://test.amocrm.ru{}?{}".format(kwargs.get("endpoint"), kwargs.get("parameters"))
	        response = requests.get(str(url), headers=headers).json()
	    elif req_type == "post":
	        response = requests.post("https://test.amocrm.ru{}".format(kwargs.get("endpoint")), headers=headers, json=kwargs.get("data")).json()
	    elif req_type == 'patch':
	        response = requests.patch("https://test.amocrm.ru{}".format(kwargs.get("endpoint")), headers=headers, json=kwargs.get("data")).json()     
	    return response

    def get_lead_by_id(self, lead_id):
	    url = "/api/v4/leads/" + str(lead_id)
	    return self._base_request(endpoint=url, type="get")

    def get_event_by_contact_id(self, contact_id):
	    url = "/api/v4/events" + "?filter[entity][]=contact&filter[entity_id][]=" + str(contact_id)
	    return self._base_request(endpoint=url, type="get")


    def set_field(self, contact_id):
	    data = [
	        {
	            "id": contact_id,
	            "last_name": "Smith"
            }
 	    ]

	    response = self._base_request(endpoint="/api/v4/contacts", type="patch", data=data)
	    return response
                                    


amocrm_wrapper_1 = AmoCRMWrapper() 

print(amocrm_wrapper_1.get_lead_by_id(16398559))
print(amocrm_wrapper_1.get_event_by_contact_id(24819649))
print(amocrm_wrapper_1.set_field(24819649))

