# -*- coding: utf-8 -*-
import os
import pickle

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "/home/marcin/.config/client_secret_965110620451-cqfriahvismvc4j6o02c33acemk86fth.apps.googleusercontent.com.json"
watch_later_id = "PLrtPE8xbZ5QazyF9yKlncouZNr3W33Po4"  # not really 'watch later'


def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    youtube = get_authenticated_service()
    token = None
    while True:
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=watch_later_id,
            pageToken=token
        )
        response = request.execute()
        for r in response["items"]:
            s = r['snippet']
            print("**", s["videoOwnerChannelTitle"], s["title"])
            print("[[https://youtube.com/watch?v=" +
                  s["resourceId"]["videoId"] + "][link]]")
            print(s["publishedAt"])
            print(s["description"][:350])
        try:
            token = response['nextPageToken']
        except:
            exit()


def get_authenticated_service():
    if os.path.exists("CREDENTIALS_PICKLE_FILE"):
        with open("CREDENTIALS_PICKLE_FILE", 'rb') as f:
            credentials = pickle.load(f)
    else:
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()
        with open("CREDENTIALS_PICKLE_FILE", 'wb') as f:
            pickle.dump(credentials, f)
    return googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)


if __name__ == "__main__":
    main()
