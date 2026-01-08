from PIL import Image
from collections import Counter
import sys

def get_dominant_color(image_path, num_colors=10):
    try:
        image = Image.open(image_path)
        image = image.convert('RGB')
        image = image.resize((50, 50))  # Resize for speed
        pixels = list(image.getdata())
        
        filtered_pixels = []
        for p in pixels:
             r, g, b = p
             
             # Filter black/white/gray
             # Exclude very white
             if r > 230 and g > 230 and b > 230: continue
             # Exclude very black
             if r < 30 and g < 30 and b < 30: continue
             
             filtered_pixels.append((r, g, b))
             
        if not filtered_pixels:
             filtered_pixels = pixels

        counts = Counter(filtered_pixels)
        most_common = counts.most_common(num_colors)
        
        if most_common:
            for color, count in most_common:
                print(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x} (Count: {count})")
            return most_common[0][0]
        return None
    except ImportError:
        print("Pillow not installed")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        return None

get_dominant_color('logo.jpg')
