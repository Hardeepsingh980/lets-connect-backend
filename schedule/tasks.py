from __future__ import print_function

import datetime
import os.path
from uuid import uuid4
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.events',
          'https://www.googleapis.com/auth/calendar']


user_json = {
        "token": "ya29.a0AVA9y1uVmYWNWqKYp52M-3kTzZ8s948n0O3h9fZPjNaXHqK9Kz95Kssmw_PCDib7VsoTdOvOqCdmgROF-JWAHP-gcLXF4hnMMQ-1i779JVsG-U8_RDApzmz8CzTVOF9YLLsAG9hZBxrYKY1VVCMnaBzl6FwRaCgYKATASAQASFQE65dr814Ia1J6L-RMKE6SJLdaLBg0163",
        "refresh_token": "1//0gA_PSLlUuweTCgYIARAAGBASNwF-L9IrNWfeOLQYaUm38DhI58CqcuIKTcy0ESMPw9N1oOcallzAjUIsnvMa7YTdx6u0XJaMISM",
        "token_uri": "https://oauth2.googleapis.com/token",
        "client_id": "554243705012-s79vtcu5s6t6i03odh8795ihhodjp0e4.apps.googleusercontent.com",
        "client_secret": "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",
        "scopes": [
            "https://www.googleapis.com/auth/calendar.events",
            "https://www.googleapis.com/auth/calendar"
        ],
        "expiry": "2022-09-03T18:46:29.325016Z"
    }

creds = Credentials.from_authorized_user_info(user_json, SCOPES)

service = build('calendar', 'v3', credentials=creds)


def create_event(description, start_datetime, end_datetime, attandees: list):
    attandees = [{'email': email} for email in attandees]
    event = {
        'summary': 'Lets connect',
        'location': 'Lets connect meet',
        'description': description,
        'start': {
            'dateTime': start_datetime,
            # 'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': end_datetime,
            # 'timeZone': 'America/Los_Angeles',
        },
        # 'recurrence': [
        #     'RRULE:FREQ=DAILY;COUNT=2'
        # ],
        'attendees': attandees,
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
        # "conferenceDataVersion": 1,
        "conferenceData": {
            "createRequest": {
                "conferenceSolutionKey": {
                    "type": "hangoutsMeet"
                },
                "requestId": uuid4().hex,
            }},

        "sendNotifications": True

    }

    # creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    event = service.events().insert(calendarId='primary', body=event,
                                    conferenceDataVersion=1, sendUpdates='all').execute()
    print('Event created: %s' % (event.get('htmlLink')))
    print(event['id'])
    return event['id']


def update_event(event_id,email):
    
    event = service.events().get(calendarId='primary',eventId=event_id).execute()
    attendees = event['attendees']
    attendees.append({'email':email})
    event['attendees'] = attendees
    updated_event = service.events().update(calendarId='primary',eventId=event_id,body=event).execute()



