import os
import json

def generate_json(folder, output_file):
    # Get all image files
    files = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    files.sort()
    
    # Corrected: Paths are now relative to the root where index.html lives
    # We remove the '../' so the server can resolve the path correctly
    relative_paths = [f"{folder}/{f}" for f in files]
    
    with open(output_file, 'w') as f:
        json.dump(relative_paths, f, indent=2)
    
    print(f"Success: {output_file} created with {len(files)} images.")

if __name__ == "__main__":
    # Ensure directories exist
    os.makedirs('images/property', exist_ok=True)
    os.makedirs('images/community', exist_ok=True)

    # Generate the JSON files inside the images folder
    generate_json('images/property', 'images/property_photos.json')
    generate_json('images/community', 'images/community_photos.json')