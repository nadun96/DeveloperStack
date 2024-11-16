import os
from pathlib import Path
import torch
import numpy as np
from PIL import Image
import imageio

class LocalVideoGenerator:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.output_dir = Path("output_videos")
        self.output_dir.mkdir(exist_ok=True)
        
    def setup_model(self):
        """
        Setup the open source text-to-video model
        Using Text2Video-Zero as an example
        """
        try:
            from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
            
            # Initialize base image model
            pipe = StableDiffusionPipeline.from_pretrained(
                "runwayml/stable-diffusion-v1-5",
                torch_dtype=torch.float16
            )
            pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
            pipe = pipe.to(self.device)
            
            return pipe
            
        except Exception as e:
            print(f"Error setting up model: {e}")
            return None
            
    def generate_video(self, prompt, num_frames=16, fps=8):
        """
        Generate video frames from text prompt
        """
        try:
            pipe = self.setup_model()
            if pipe is None:
                return False
                
            # Generate base image
            base_image = pipe(
                prompt,
                num_inference_steps=25,
                guidance_scale=7.5
            ).images[0]
            
            # Generate video frames (simplified example)
            frames = []
            for i in range(num_frames):
                # Add simple motion to base image
                frame = base_image.copy()
                # Apply some transformation (e.g., slight movement)
                frame = self.add_motion(frame, i, num_frames)
                frames.append(frame)
            
            # Save as video
            output_path = self.output_dir / f"generated_video_{len(list(self.output_dir.glob('*.mp4')))}.mp4"
            imageio.mimsave(str(output_path), frames, fps=fps)
            
            print(f"Video saved to {output_path}")
            return True
            
        except Exception as e:
            print(f"Error generating video: {e}")
            return False
    
    def add_motion(self, image, frame_idx, total_frames):
        """
        Add simple motion to frame (example implementation)
        """
        # Convert PIL to numpy
        frame = np.array(image)
        
        # Add simple horizontal movement
        shift = int((frame_idx / total_frames) * 20)  # 20 pixels total movement
        frame = np.roll(frame, shift, axis=1)
        
        return Image.fromarray(frame)

def main():
    # Setup
    generator = LocalVideoGenerator()
    
    # Generate video
    prompt = "A serene mountain landscape with flowing clouds"
    generator.generate_video(prompt)

if __name__ == "__main__":
    main()



from diffusers import DiffusionPipeline
import torch

pipeline = DiffusionPipeline.from_pretrained(
    "damo-vilab/text-to-video-ms-1.7b",
    torch_dtype=torch.float16,
    variant="fp16"
)
if torch.cuda.is_available():
    pipeline = pipeline.to("cuda")

prompt = "A beautiful sunset over mountains"
video_frames = pipeline(prompt).frames

pip install torch torchvision diffusers transformers accelerate imageio pillow