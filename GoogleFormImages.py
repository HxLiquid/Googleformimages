from PIL import Image
from time import sleep
import pyautogui

# Replace with with the image source folder. REMEMBER TO DOUBLE BACKSLASH
image_location = ""
# Replace with the image output folder. REMEMBER TO DOUBLE BACKSLASH
save_image_location = ""

left_off = pyautogui.prompt('Enter the number of the last image you did. 1 if you are just starting.')

# Repeat the process as many times as needed
for img_count in range(99999):

    # This accounts for how the files are named and allows for continuing where you left off
    img_number = img_count + int(left_off)
    img_number = str(img_number)

    print("Rendering image " + img_number)

    # Resize image to 9x7
    filename = image_location + "\\image (" + img_number + ").png"
    img = Image.open(filename)
    new_size = (9, 7)
    img = img.resize(new_size)

    # Image size
    wid, hgt = img.size

    # Convert image to RGB
    img_rgb = img.convert('RGB')

    # Loop though values and check boxes
    for pixel_root_wid in range(wid):
        pyautogui.moveTo(710, 360)
        pyautogui.move(70 * pixel_root_wid, 0)
        for pixel_root_hgt in range(hgt):
            rgb_pixel_value = img_rgb.getpixel((pixel_root_wid, pixel_root_hgt))
            r, g, b = rgb_pixel_value
            if r < 100:
                pyautogui.click()
            pyautogui.move(0, 70)
    pyautogui.click()

    # Save screenshot
    sleep(0.20)
    dst = "image-" + str(img_number).zfill(4) + ".png"
    screenshot = pyautogui.screenshot()
    screenshot.save(save_image_location + "\\" + dst)
    save_location = str(save_image_location + "\\" + dst)
    sleep(0.20)
    print("Image saved to " + save_location)

    # Loop though values and check boxes again to clear canvas
    for pixel_root_wid in range(wid):
        pyautogui.moveTo(710, 360)
        pyautogui.move(71 * pixel_root_wid, 0)
        for pixel_root_hgt in range(hgt):
            rgb_pixel_value = img_rgb.getpixel((pixel_root_wid, pixel_root_hgt))
            r, g, b = rgb_pixel_value
            if r < 100:
                pyautogui.click()
            pyautogui.move(0, 70)
    pyautogui.click()

    print("Cleared canvas")
    
    


