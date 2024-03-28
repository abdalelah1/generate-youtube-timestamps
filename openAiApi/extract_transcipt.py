import json
from youtube_transcript_api import YouTubeTranscriptApi
def extract_transcript(youtube_url):
    video_id = youtube_url.split("=")[-1]
    transcript=YouTubeTranscriptApi.get_transcript(video_id)
    json_transcript = json.dumps(transcript)
    return json_transcript







