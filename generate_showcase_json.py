import os
import json

showcase_dir = "docs/showcase"
image_files = [f for f in os.listdir(showcase_dir) if f.endswith("_web.jpg")]

images_json = []
for image_file in image_files:
    # This is a placeholder for reading metadata from a database or a sidecar file
    images_json.append({
        "src": f"showcase/{image_file}",
        "title": image_file.replace("_web.jpg", "").replace("_", " "),
        "description": "An AI-enriched image.",
        "keywords": ["ai", "enriched"]
    })

with open("docs/showcase/images.json", "w") as f:
    json.dump(images_json, f, indent=2)
