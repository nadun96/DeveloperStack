import os
import time
import requests
import replicate
from pathlib import Path

class VideoGenerator:
    def __init__(self, api_key):
        """
        Initialize the video generator with your Replicate API key
        """
        self.api_key = api_key
        os.environ["REPLICATE_API_TOKEN"] = api_key
        
    def generate_video(self, script, output_path="output_video.mp4", num_frames=16, fps=8):
        """
        Generate a video based on the input script
        
        Parameters:
        script (str): The text description to generate the video from
        output_path (str): Where to save the output video
        num_frames (int): Number of frames to generate
        fps (int): Frames per second for the output video
        """
        try:
            # Initialize the model
            model = replicate.models.get("stability-ai/stable-video-diffusion")
            version = model.versions.get("3f0457e4619daac51351b5cc5f7e7ccb4e89bc36ba248e8c1714009e0fc23c9a")
            
            # Start the generation
            output = version.predict(
                prompt=script,
                num_frames=num_frames,
                fps=fps
            )
            
            # The output will be a URL where the video can be downloaded
            if output and isinstance(output, str):
                # Download the video
                response = requests.get(output)
                if response.status_code == 200:
                    with open(output_path, 'wb') as f:
                        f.write(response.content)
                    print(f"Video successfully generated and saved to {output_path}")
                    return True
                else:
                    print(f"Failed to download video: Status code {response.status_code}")
                    return False
            else:
                print("No output URL received from the model")
                return False
                
        except Exception as e:
            print(f"Error generating video: {str(e)}")
            return False
            
    def generate_video_with_progress(self, script):
        """
        Generate a video with progress updates
        """
        try:
            print("Starting video generation...")
            print("Processing script:", script)
            
            # Start generation
            success = self.generate_video(script)
            
            if success:
                print("Video generation completed successfully!")
            else:
                print("Video generation failed.")
                
        except Exception as e:
            print(f"Error during video generation: {str(e)}")

def main():
    # Replace with your actual API key
    API_KEY = "your_replicate_api_key_here"
    
    # Create the generator
    generator = VideoGenerator(API_KEY)
    
    # Example script
    script = """A serene lake surrounded by tall pine trees at sunset, 
                with gentle ripples on the water surface and warm golden light 
                filtering through the branches"""
    
    # Generate the video
    generator.generate_video_with_progress(script)

if __name__ == "__main__":
    main()
