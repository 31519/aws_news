import requests
import json
from django.conf import settings




MAILCHIMP_API_KEY = getattr(settings, 'MAILCHIMP_API_KEY', None)
MAILCHIMP_DATA_CENTER = getattr(settings, 'MAILCHIMP_DATA_CENTER', None)
MAIL_CHIMP_EMAIL_LIST_ID =getattr(settings, 'MAIL_CHIMP_EMAIL_LIST_ID', None)


api_url = f"https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0"
members_endpoint = f'{api_url}/lists/{MAIL_CHIMP_EMAIL_LIST_ID}/members'


def subscribe(email):
            
        
        data= {
            'email_address':email,
            'status':'subscribed'
        }
        
        r = requests.post(members_endpoint, auth=("", MAILCHIMP_API_KEY), data=json.dumps(data))
        return r.status_code, json()
def email_list_signup(request):
    pass


class Mailchimp(object):
    def __init__(self):
        super(Mailchimp, self).__init__()
        self.key = MAILCHIMP_API_KEY
        self.api_url = "https://{dc}.api.mailchimp.com/3.0".format(
            dc=MAILCHIMP_DATA_CENTER
        )
        self.list_id = MAIL_CHIMP_EMAIL_LIST_ID
        self.list_endpoint  = '{api_url}/lists/{list_id}'.format(api_url = self.api_url, list_id = self.list_id)

    def check_subscription_status(self, email):
        #endpoint
        # method
        # data
        # auth
        endpoint = self.api_url
        r = requests.get(endpoint, auth=("", self.key))
        return r.json()

    def check_valid_status(self, status):
        choices = ['subscribed', 'unsubscribed', 'cleaned', 'pending']
        if status not in choices:
            raise ValueError("Not a valid choice for email status")
        return status

    def add_email(self, email):
        #endpoint
        # method
        # data
        # auth
        status = "subscribed"
        self.check_subscription_status(status)
        data= {
            'email_address':email,
            'status':status
        }
        endpoint = self.list_endpoint + "/members"
        r = requests.post(endpoint, auth=("", self.key), data=json.dumps(data))
        return r.json()

