from PIL import Image
import os

def convert_jpeg_to_png(input_path):
    try:
        # Open the JPEG image
        with Image.open(input_path) as img:
            # Convert the image to RGB if it's not already
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Process image (in this case, just return the image)
            processed_img = img
            
            # Assess image quality (simplified version)
            # Here we're using image size as a proxy for quality
            width, height = processed_img.size
            image_quality = 'high' if width * height > 1000000 else 'low'
            
            # Create output filename
            output_filename = os.path.splitext(input_path)[0] + '_converted.png'
            
            if image_quality == 'high':
                # Save as PNG directly
                processed_img.save(output_filename, 'PNG')
            else:
                # Adjust quality by enhancing contrast and sharpness
                adjusted_img = processed_img.enhance(1.2)  # Enhance contrast
                adjusted_img = adjusted_img.filter(ImageFilter.SHARPEN)
                adjusted_img.save(output_filename, 'PNG')
                
            print(f"Conversion completed. Saved as: {output_filename}")
            return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

def main():
    while True:
        input_path = input("Enter the path to your JPEG image (or 'q' to quit): ")
        
        if input_path.lower() == 'q':
            break
        
        if not os.path.exists(input_path):
            print("File does not exist. Please try again.")
            continue
            
        if not input_path.lower().endswith(('.jpg', '.jpeg')):
            print("File is not a JPEG image. Please try again.")
            continue
        
        success = convert_jpeg_to_png(input_path)
        if success:
            print("Conversion completed successfully!")
        else:
            print("Conversion failed. Please try again with a different image.")

if __name__ == "__main__":
    main()
