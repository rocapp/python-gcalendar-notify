#!/usr/bin/env python
# exec("${pygcal_python_path}" "$0.py" "$@") # use custom python
from __future__ import print_function
import datetime
import pickle
import os.path
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import gi
gi.require_version('Gio', '2.0')
from gi.repository import Gio

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                os.environ.get('pygcal_credentials'), SCOPES)
            creds = flow.run_local_server(port=5000)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    nday = datetime.datetime.utcnow().isoformat().split('T')[0] # today's date
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    print('items gotten.')
    if not events:
        print('No upcoming events found.')
        return

    app = Gio.Application.new("python.gcalendar.notify", Gio.ApplicationFlags.FLAGS_NONE)
    app.register()
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
        if start.split("T")[0]==nday:
            notif = Gio.Notification.new(start)
            notif.set_body(event['summary'])
            Icon = Gio.ThemedIcon.new('dialog-information')
            notif.set_icon(Icon)
            app.send_notification(None, notif)
        


if __name__ == '__main__':
    main()
