from sklearn.decomposition import PCA  # For Principal Component Analysis (PCA)
import numpy as np  # For numerical computations
from PIL import Image  # For loading and saving images
import matplotlib.pyplot as plt  # For visualizing images
from skimage.metrics import peak_signal_noise_ratio as psnr  # For calculating PSNR
from skimage.metrics import mean_squared_error as mse  # For calculating MSE

def pca_compression(image_path, n_components):
    """
    Compress an image using Principal Component Analysis (PCA).
    
    Args:
        image_path (str): Path to the input image.
        n_components (int): Number of principal components to retain.
    
    Returns:
        tuple: Original image as a NumPy array and the compressed image as a NumPy array.
    """
    # Load the image and convert it to RGB format
    image = Image.open(image_path).convert('RGB')
    image_np = np.array(image)  # Convert image to a NumPy array

    # Reshape the image to 2D (flatten spatial dimensions) for PCA
    h, w, c = image_np.shape  # Get the height, width, and channels of the image
    image_reshaped = image_np.reshape(-1, 3)  # Reshape into (pixels, channels)

    # Apply PCA to reduce dimensionality
    pca = PCA(n_components=n_components)  # Initialize PCA with specified components
    compressed = pca.fit_transform(image_reshaped)  # Perform PCA transformation

    # Reconstruct the image from compressed data
    reconstructed = pca.inverse_transform(compressed)  # Inverse transform to reconstruct
    reconstructed_image = reconstructed.reshape(h, w, 3).astype(np.uint8)  # Reshape back to original dimensions

    return image_np, reconstructed_image  # Return original and compressed images


image_path = r"C:\Users\test\image.jpg"  # Path to the input image
n_components = 1  # Number of principal components to retain

# Perform PCA compression
original_image, compressed_image = pca_compression(image_path, n_components)

# Compare the original and compressed images side-by-side
plt.figure(figsize=(10, 5))  # Set the figure size

# Display the original image
plt.subplot(1, 2, 1)  # Create the first subplot
plt.imshow(original_image)  # Show the original image
plt.title("Original Image")  # Set the title
plt.axis("off")  # Turn off axis display

# Display the compressed image
plt.subplot(1, 2, 2)  # Create the second subplot
plt.imshow(compressed_image)  # Show the compressed image
plt.title(f"Compressed Image (n_components={n_components})")  # Set the title
plt.axis("off")  # Turn off axis display

plt.tight_layout()  # Adjust layout to avoid overlap
plt.show()  # Display the plot

# Save the compressed image to a file
compressed_image_pil = Image.fromarray(compressed_image)  # Convert NumPy array to PIL Image
compressed_image_pil.save("compressed_output.jpg")  # Save the compressed image

# Calculate and print quality metrics
psnr_value = psnr(original_image, compressed_image)  # Calculate PSNR (Peak Signal-to-Noise Ratio)
mse_value = mse(original_image, compressed_image)  # Calculate MSE (Mean Squared Error)

# Print the results
print(f"PSNR: {psnr_value:.2f} dB")  # Print PSNR in decibels
print(f"MSE: {mse_value:.2f}")  # Print MSE
