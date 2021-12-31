from googleapiclient.discovery import build
import os, isodate, time, csv
import pandas as pd
api_key = os.environ.get("YT_API_KEY")  # you have to create your own API key
youtube = build("youtube", "v3", developerKey=api_key)
nextPageToken = None
permListForIDS = []
permListForDuration = []
permListForTitles = []
total_seconds_current_playlist = 0
start_time = time.time()
def convert_seconds_to_time(asd):
    hours = int(asd) // 3600
    minutes = (int(asd) % 3600) // 60
    seconds = int(asd) % 60
    string_to_hold_them = f"{hours}h:{minutes}m:{seconds}s"
    string_without_colons = f"{hours}h{minutes}m{seconds}s"
    return string_to_hold_them, string_without_colons
while True:
    pl_request = youtube.playlistItems().list(
        part="contentDetails,snippet,status",
        playlistId="PLmNMakH9YANUQLEl4klcQ5aQJ2mviEP4U",  # example playlist
        maxResults=50,
        pageToken=nextPageToken,)
    pl_response = pl_request.execute()
    vid_ids = []
    for i in pl_response["items"]:
        getVidID = i["contentDetails"]["videoId"]
        getVidTitle = i["snippet"]["title"]
        getVidStatus = i["status"]["privacyStatus"]
        if getVidStatus == "privacyStatusUnspecified" or getVidStatus == "private":
            continue
        if getVidStatus == "public" or getVidStatus == "unlisted":
            vid_ids.append(getVidID)
            permListForIDS.append(getVidID)
            permListForTitles.append(getVidTitle)
    vid_request = youtube.videos().list(part="contentDetails", id=",".join(vid_ids))
    vid_response = vid_request.execute()
    for i in vid_response["items"]:
        duration = i["contentDetails"]["duration"]
        permListForDuration.append(isodate.parse_duration(duration).seconds)
        total_seconds_current_playlist += isodate.parse_duration(duration).seconds
    if os.path.isfile("./totalCSV.csv") == False:
        outputFile = open("totalCSV.csv", "w", newline="", encoding="utf-16")
        outputDictWriter = csv.DictWriter(outputFile, ["VIDID", "LENGTH", "TITLE"])
        outputDictWriter.writeheader()
        outputFile.close()
    lines = open("totalCSV.csv", "r", encoding="utf-16").read()
    with open("totalCSV.csv", "a+", newline="", encoding="utf-16") as fp:
        writer = csv.writer(fp)
        for i in range(len(permListForIDS)):
            if permListForIDS[i] in lines:
                continue
            else:
                content = [
                    permListForIDS[i],
                    permListForDuration[i],
                    permListForTitles[i],]
                writer.writerow(content)
    nextPageToken = pl_response.get("nextPageToken")
    if not nextPageToken:
        break
df = pd.read_csv("totalCSV.csv", encoding="utf-16")
totalsecondsPandas = int(df["LENGTH"].sum())
print(f"Duration of the playlist: {convert_seconds_to_time(total_seconds_current_playlist)[0]}")
print(f"Duration of the videos in the csv file: {convert_seconds_to_time(totalsecondsPandas)[0]}")
print(f"\nTime it took: {time.time() - start_time}s")
