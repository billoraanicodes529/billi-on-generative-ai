# 8) Write a Python program to input a text prompt from the user 
# and generate an image using a pre-trained text-to-image model 
# (runwayml/stable-diffusion-v1-5)
# → pip install diffusers

from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5"
)
pipe = pipe.to("cpu")

prompt = input("Enter image prompt: ")

image = pipe(prompt).images[0]

image.save("output1.png")

print("Image generated successfully!")

# Ultra-detailed cinematic masterpiece of a Koenigsegg Agera hypercar parked on a wet neon-lit cyberpunk city street at night, dramatic low angle perspective, aggressive stance, glossy exposed carbon fiber bodywork reflecting vibrant blue and purple lights, glowing headlights cutting through light rain mist, ultra realistic reflections on wet asphalt, volumetric fog, ray-traced global illumination, 8K resolution, extreme sharpness, hyper realistic textures, professional automotive photography, HDR, dynamic depth of field, motion blur light streaks in background, breathtaking composition, award winning photography, insanely detailed, photorealistic, rendered in the absolute best quality possible, masterpiece, stunning, amazing, cinematic lighting, Unreal Engine 5, Octane render, perfect shadows, perfect reflections, ultra high definition, sharp focus, no noise, no blur, crystal clear details