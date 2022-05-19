# transformations.py
# Worked on by: Pedro
# Description: Holds image transformation code for the info page
#
# Transformations:
#       Grayscale
#       Negative
#       Sepia

import base64
from io import BytesIO

# Apply a given image transformation to a given image
def transform_image(img, transformation):
    # Will perform transformation based on input
    # If input is 'normal', do nothing
    if transformation == 'grayscale':
        img = grayscale_list(img)
    elif transformation == 'sepia':
        img = sepia_list(img)
    elif transformation == 'negative':
        img = negative_list(img)

    return get_img(img)

# Convert image so that it can be used in HTML
def get_img(img):
    img_data = BytesIO()
    img.save(img_data, "PNG")
    img_str = base64.b64encode(img_data.getvalue()).decode('ascii')
    return f'data:image/png;base64,{ img_str }'

# Perform sepia image transformation for current pixel
def sepia(i):
    # tint shadows
    if i[0] < 63:
        r,g,b = int(i[0] * 1.1), i[1], int(i[2] * 0.9)

    # tint midtones
    elif i[0] > 62 and i[0] < 192:
        r,g,b = int(i[0] * 1.15), i[1], int(i[2] * 0.85)
    
    # tint highlights
    else:
        r = int(i[0] * 1.08) 
        g,b = i[1], int(i[2] * 0.5)
    
    return r, g, b

# Get list of sepia transformed pixels
def sepia_list(img):
    sep_list = [sepia(i) for i in img.getdata()]
    img.putdata(sep_list)
    return img

# Perform negative image transformation for current pixel
def negative(i):
    # taking negative of rgb values
    r,g,b = 255 - i[0], 255 - i[1], 255 - i[2]

    return r, g, b

# Get list of negative transformed pixels
def negative_list(img):
    neg_list = [negative(i) for i in img.getdata()]
    img.putdata(neg_list)
    return img

# Perform grayscale image transformation for current pixel
def grayscale(i):
    # performing grayscale conversion
    r,g,b = ((i[0]*299 + i[1]*587 + i[2]*114) // 1000,) * 3

    return r, g, b

# Get list of grayscale transformed pixels
def grayscale_list(img):
    gray_list = [grayscale(i) for i in img.getdata()]
    img.putdata(gray_list)
    return img