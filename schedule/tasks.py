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


class InputType(object):
    summary: str
    description: str


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
    # creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    creds = Credentials.from_authorized_user_info(user_json, SCOPES)

    service = build('calendar', 'v3', credentials=creds)
    event = service.events().insert(calendarId='primary', body=event,
                                    conferenceDataVersion=1, sendUpdates='all').execute()
    print('Event created: %s' % (event.get('htmlLink')))


# create_event()


# def main():
#     """Shows basic usage of the Google Calendar API.
#     Prints the start and name of the next 10 events on the user's calendar.
#     """
#     creds = None
#     # The file token.json stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'cred.json', SCOPES)
#             creds = flow.run_local_server(host='localhost',port=8080)
#             print(creds)
#         # Save the credentials for the next run
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())

#     #create credentials from access
#     try:
#         service = build('calendar', 'v3', credentials=creds)

#         # Call the Calendar API
#         now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
#         print('Getting the upcoming 10 events')
#         events_result = service.events().list(calendarId='primary', timeMin=now,
#                                               maxResults=10, singleEvents=True,
#                                               orderBy='startTime').execute()
#         events = events_result.get('items', [])

#         if not events:
#             print('No upcoming events found.')
#             return

#         # Prints the start and name of the next 10 events
#         for event in events:
#             start = event['start'].get('dateTime', event['start'].get('date'))
#             print(start, event)

#         event = {
#         'summary': 'Nandan Test',
#         'location': 'Lovely professional university',
#         'description': 'A chance to hear more about Google\'s developer products.',
#         'start': {
#             'dateTime': '2022-09-05T09:00:00-07:00',
#             'timeZone': 'America/Los_Angeles',
#         },
#         'end': {
#             'dateTime': '2022-09-05T09:00:00-08:00',
#             'timeZone': 'America/Los_Angeles',
#         },
#         # 'recurrence': [
#         #     'RRULE:FREQ=DAILY;COUNT=2'
#         # ],
#         'attendees': [
#             {'email': 'hardeepabove18@example.com'},
#             # {'email': 'sbrin@example.com'},
#         ],
#         'reminders': {
#             'useDefault': False,
#             'overrides': [
#             {'method': 'email', 'minutes': 24 * 60},
#             {'method': 'popup', 'minutes': 10},
#             ],
#         },
#         # "conferenceDataVersion": 1,
#         "conferenceData": {
#       "createRequest": {
#         "conferenceSolutionKey": {
#           "type": "hangoutsMeet"
#         },
#         "requestId": "7qxalsvy0exxaje"
#       }}


#         }

#         # event = service.events().insert(calendarId='primary', body=event,conferenceDataVersion=1).execute()
#         # print(event)

#         print('Event created: %s' % (event.get('htmlLink')))

#         # Call the Calendar API
#         # now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
#         # print('Getting the upcoming 10 events')
#         # events_result = service.events().list(calendarId='primary', timeMin=now,
#         #                                       maxResults=10, singleEvents=True,
#         #                                       orderBy='startTime').execute()
#         # events = events_result.get('items', [])

#         # if not events:
#         #     print('No upcoming events found.')
#         #     return

#         # # Prints the start and name of the next 10 events
#         # for event in events:
#         #     start = event['start'].get('dateTime', event['start'].get('date'))
#         #     print(start, event)

#         # calendar = service.calendars().get(calendarId='primary').execute()
#         # print(f'{calendar=}')

#     except HttpError as error:
#         print('An error occurred: %s' % error)


# if __name__ == '__main__':
#     main()

#     # ya29.a0AVA9y1t-6BxwKfxbR1JbEkAZRKAJ_6n5O4Z_nmD-mgVz1OM7PjtAW1rLUxAKHAxO_6owXiOjTwW9Jn8Nml1uevx7BFaiuuD8mDiBzGky9p7Aen2kHMGRl0vapFc83UOvTexG0F6Qw3YcoaDWfewtMfgYigbRaCgYKATASAQASFQE65dr8pCvSDx6ca4Ts5J0RWSAdlQ0163
