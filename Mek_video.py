from pymediainfo import MediaInfo

"""
pymediainfo
"""


def get_video_info(file):
    media_info = MediaInfo.parse(file)
    media_data = media_info.to_data().get('tracks')
    if media_data is not None:
        # print(media_data[0].get('codecs_video'))
        '''print(len(media_data))
        for i in media_data[0].items():
            print(i)
            pass
        print('-' * 100)
        for i in media_data[2].items():
            print(i)
            pass'''

        return {'file_name': media_data[0].get('file_name'),
                'codecs_video': media_data[0].get('codecs_video'),
                'file_size': media_data[0].get('file_size'),
                'bit_rate': media_data[0].get('overall_bit_rate'),
                'frame_rate': media_data[0].get('frame_rate'),
                'audio_codecs': media_data[0].get('audio_codecs'),
                'audio_bit_rate': media_data[2].get('bit_rate'),
                'width': media_data[1].get('width'),
                'height': media_data[1].get('height'),
                'raw': media_data}
    return None


if __name__ == '__main__':
    print(get_video_info('FC2-1415477.mp4'))
