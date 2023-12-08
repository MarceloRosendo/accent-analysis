from youtube_transcript_api import YouTubeTranscriptApi
import pandas as pd

fluminense = ['jONU1tRzzAw', '6vS1P0jq_vg']
baiano = ['cEABmOirX48', 'hQupTegyebw', 'BQY0E9k67VY']
mineiro = ['Z8wnqhpO3Hs']

def download_transcriptions(path, video_id_list):
    for index, id in enumerate(video_id_list):
        response = pd.DataFrame(YouTubeTranscriptApi.get_transcript(id, languages=['pt']))
        response.to_json(f'data/{path}/{index}.json')
download_transcriptions('fluminense', fluminense)
download_transcriptions('baiano', baiano)
download_transcriptions('mineiro', mineiro)