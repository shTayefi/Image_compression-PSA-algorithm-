# PCA-Based Image Compression

This repository contains a Python implementation of image compression using Principal Component Analysis (PCA). PCA is a dimensionality reduction technique used to compress images while retaining as much essential information as possible.

---

## Features
- Image Compression:
  - Reduces the size of an image by retaining only the most important components (principal components).
  - Allows the user to control the level of compression by selecting the number of principal components.
- Image Quality Metrics:
  - Calculates PSNR (Peak Signal-to-Noise Ratio) to evaluate the quality of the compressed image.
  - Calculates MSE (Mean Squared Error) to quantify the difference between the original and compressed images.
- Visualization:
  - Displays the original and compressed images side-by-side for comparison.

---

##  Installation 

###  Prerequisites 
Ensure you have Python installed (version 3.7 or later) and the following libraries installed in your environment:
- `scikit-learn`
- `numpy`
- `pillow`
- `matplotlib`
- `scikit-image`

###  Install Dependencies 
You can install the required packages using `pip`:
```bash
pip install numpy pillow matplotlib scikit-learn scikit-image
```

Alternatively, if you're using  conda :
```bash
conda install numpy pillow matplotlib scikit-learn scikit-image
```

---

##  Usage 

###  Running the Code 
1.  Input Image : Save your input image to a desired directory (e.g., `image_1.jpg`).
2. Update the `image_path` variable in the code to point to your input image file.

```python
image_path = r"C:\path\to\your\image.jpg"  # Update this with the path to your image
```

3. Set the desired number of principal components using the `n_components` variable.

```python
n_components = 3  # Adjust this value to control the compression level
```

4. Run the Python script:
```bash
python script_name.py
```

---

##  Output 
-  Visual Comparison : The program displays the original and compressed images side-by-side for comparison.
-  Compressed Image File : The compressed image is saved as `compressed_output.jpg` in the same directory.
-  Quality Metrics : The program prints the following metrics in the console:
  -  PSNR (Peak Signal-to-Noise Ratio):  Indicates the quality of the compressed image. Higher values indicate better quality.
  -  MSE (Mean Squared Error):  Indicates the error between the original and compressed image. Lower values indicate better quality.

---

##  Code Explanation 

###  Core Function: `pca_compression` 
This function handles the PCA-based compression and reconstruction process:
-  Input:  Path to the image and the number of principal components.
-  Output:  Original image and the compressed image.

###  Steps: 
1.  Load Image:  Reads the image and converts it into a NumPy array.
2.  Reshape for PCA:  Flattens the image into a 2D array where each row represents a pixel, and columns represent color channels (R, G, B).
3.  Apply PCA:  Reduces the dimensions of the image using the specified number of principal components.
4.  Reconstruct Image:  Converts the compressed data back to the original image dimensions.
5.  Return Results:  Returns both the original and compressed images for further analysis.

---

##  Example Results 

-  Original vs. Compressed Image :  
  The compressed image retains most of the visual quality while reducing the amount of data stored.
  
  ![Example Output](example_image_comparison.jpg)

-  Quality Metrics :
  ```
  PSNR: 30.45 dB
  MSE: 125.67
  ```

---

##  How to Modify 
-  Change Compression Level:  Adjust the `n_components` variable to increase or decrease the level of compression. Lower values mean higher compression but reduced quality.
-  Grayscale Compression:  If desired, modify the code to compress grayscale images instead of RGB.

