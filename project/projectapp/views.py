from django.shortcuts import render
from moviepy.editor import VideoFileClip

def process_video(video_file):
    # Split video into video and audio components
    temp_file_path = 'temp_video.mp4'
    with open(temp_file_path, 'wb') as temp_file:
        for chunk in video_file.chunks():
            temp_file.write(chunk)

    # Split video into video and audio components
    video_clip = VideoFileClip(temp_file_path)
    audio_clip = video_clip.audio
    video_clip = VideoFileClip(temp_file_path, audio=False)
    
    # Write the video and audio components to separate files
    output_video_path = 'output_video.mp4'
    output_audio_path = 'output_audio.mp3'
    video_clip.write_videofile(output_video_path)
    audio_clip.write_audiofile(output_audio_path)
    
    # Delete the temporary video file
    os.remove(temp_file_path)
    return print("sucess")
    '''return output_video_path, output_audio_path'''

    '''video_clip = VideoFileClip(video_file)
    audio_clip = video_clip.audio
    video_clip = VideoFileClip(video_file,audio=False)
    video_clip.write_videofile(r"C:/Users/karth/Desktop/output_video.mp4")
    audio_clip.write_audiofile(r"C:/Users/karth/Desktop/output_audio.mp3")
    return 
    return video_clip, audio_clip'''


def detect_deepfake(video_clip, audio_clip):
    # Perform video and audio detection using separate models
    # Example:
    video_detection_result = video_detection_model.detect(video_clip)
    audio_detection_result = audio_detection_model.detect(audio_clip)
    return video_detection_result, audio_detection_result

def upload_video(request):
    if request.method == 'POST':
        print("hi")
        video_file = request.FILES['video']
        video_clip, audio_clip = process_video(video_file)
        print("success")
        # Perform deepfake detection
        ''''video_detection_result, audio_detection_result = detect_deepfake(video_clip, audio_clip)

        return render(request, 'result.html', {'video_result': video_detection_result, 'audio_result': audio_detection_result})'''
    else:
        print("error")
    return render(request, 'upload.html')
