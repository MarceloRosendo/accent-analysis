from youtube_transcript_api import YouTubeTranscriptApi
import pandas as pd

def download_transcriptions(path, video_id_list):
    for index, id in enumerate(video_id_list):
        try:
            response = pd.DataFrame(YouTubeTranscriptApi.get_transcript(id, languages=['pt']))
            response.to_json(f'data/{path}/{index}.json')
            print('transcripting', index)
        except:
            continue

def get_list_ids_from_file(src):
    with open(f'data/{src}.txt') as f:
        lines = f.readlines()
        return list(map(lambda line: line.replace('\n', ''),lines))

#baiano
#accent_list_1 = get_list_ids_from_file('subject_accent_1_ids')
#accent_list_2 = get_list_ids_from_file('subject_accent_1_2_ids')

#fluminense
#accent_list_3 = get_list_ids_from_file('subject_accent_2_ids')
#accent_list_4 = get_list_ids_from_file('subject_accent_2_2_ids')

#mineiro
accent_list_5 = get_list_ids_from_file('subject_accent_3_ids')
accent_list_6 = get_list_ids_from_file('subject_accent_3_2_ids')

#fluminense = accent_list_1 + accent_list_2
#baiano = accent_list_3 + accent_list_4
mineiro = accent_list_5 + accent_list_6

#download_transcriptions('fluminense', fluminense)
#download_transcriptions('baiano', baiano)
download_transcriptions('mineiro', mineiro)
