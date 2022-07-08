import os
import google_apis_oauth
from django.shortcuts import HttpResponseRedirect, HttpResponse
from rest_framework.response import Response
import google_apis_oauth
from googleapiclient.discovery import build
from django.core.exceptions import ValidationError, PermissionDenied


REDIRECT_URI = 'http://localhost:8000/rest/v1/google_oauth/callback/'

# Authorization scopes required
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Path of the "client_id.json" file
JSON_FILEPATH = os.path.join(os.getcwd(), 'client_id.json')


def RedirectOauthView(request):
    oauth_url = google_apis_oauth.get_authorization_url(
        JSON_FILEPATH, SCOPES, REDIRECT_URI)
    return HttpResponseRedirect(oauth_url)


def CallbackView(request):

    try:
        credentials = google_apis_oauth.get_crendentials_from_callback(
            request,
            JSON_FILEPATH,
            SCOPES,
            REDIRECT_URI
        )

        stringified_token = google_apis_oauth.stringify_credentials(credentials)
        creds, refreshed = google_apis_oauth.load_credentials(stringified_token)

        # Using credentials to access Upcoming Events
        service = build('calendar', 'v3', credentials=creds)
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        print('Getting the upcoming 5 events')

        events_result = service.events().list(
            calendarId='primary', timeMin=now,
            maxResults=5, singleEvents=True,
            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])


        return Response("Displayed all the upcoming events!")


    except PermissionDenied:
        return HttpResponse("Invalid Login")
