'''from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from .views import process_video

class UploadAndSplittingTestCase(TestCase):
    def test_upload_video(self):
        # Test uploading functionality
        with open('path/to/test_video.mp4', 'rb') as f:
            file = SimpleUploadedFile('test_video.mp4', f.read(), content_type='video/mp4')
            response = self.client.post(reverse('upload_video'), {'video': file})
        self.assertEqual(response.status_code, 200)  # Check if the upload was successful
        # Add more assertions to check if the video was stored properly in the file system

    def test_process_video(self):
        # Test splitting functionality
        with open('path/to/test_video.mp4', 'rb') as f:
            video_clip, audio_clip = process_video(f)
        self.assertIsNotNone(video_clip)  # Check if video component is extracted
        self.assertIsNotNone(audio_clip)  # Check if audio component is extracted
        # Add more assertions to validate properties of video_clip and audio_clip


'''
from django.test import TestCase
from .views import process_video

class SplittingTestCase(TestCase):
    def test_process_video(self):
        # Use a sample video file for testing
        video_path = r"C:\Users\karth\Desktop\VID-20240114-WA0057.mp4"
        with open(video_path, 'rb') as f:
            video_clip, audio_clip = process_video(video_path)
       

        # Save output files to a known location for manual inspection
        video_clip.write_videofile(r"C:\Users\karth\Desktop\output_video.mp4")
        audio_clip.write_audiofile(r"C:\Users\karth\Desktop\output_audio.mp3")

        # Assertions to verify splitting process
        self.assertIsNotNone(video_clip)  # Check if video component is extracted
        self.assertIsNotNone(audio_clip)  # Check if audio component is extracted

# Add more comparisons as needed
