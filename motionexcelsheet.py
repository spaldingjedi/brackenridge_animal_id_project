import PIL.Image
import pandas as pd
import glob
import PIL
import re
#this script is garbage do not use it
#Make excel sheet
dataforMotion = pd.DataFrame(columns=['ID', 'filepath', 'sitename', 'date', 'time'])
id=1
for filename in glob.iglob('C:\\Users\\spald\\Downloads\\FebruaryPhotos_Sorted\\FebruaryPhotos_Sorted\\[a-zA-Z][0-9][0-9]\\*', recursive=True):
    try:
        img = PIL.Image.open(filename)
    except:
        print(filename + " is corrupted")
        continue
        # If one wants the regex piece could be replaced by string based counting methods. This would be faster but would require more work
        # This finds the place where you would want to move the photos based on the pattern of anything a slash a letter a number a second number and two slashs and exports it to the form of string
    filename2 = re.search(r'.*\\[a-zA-Z][0-9][0-9]\\', filename).group()
    # This does the samething as the last 1 with 1 key differnce being that it doesn't extract anything from before the first slash the result should be something like \\C01\\
    sitewithslash = re.search(r'\\[a-zA-Z][0-9][0-9]\\', filename).group()
    # This removes the slashes from around the site name using string indexing.
    site = sitewithslash[1:4]
    NotTimelapseFolderPath = filename2
    exif_data = img._getexif()
    pimagename = exif_data[306].replace(" ", "")
    imagename = pimagename.replace(":", "")
    imagename = imagename + site
    NotTimelapsePhotoPath = NotTimelapseFolderPath + '\\' + imagename + '.jpg'
    img.close()
    datetime = exif_data[306].split(" ")
    date = datetime[0].replace(":", "//")
    time = datetime[1]
    dataforMotion.loc[len(dataforMotion.index)]=[id, NotTimelapsePhotoPath, site, date, time]
    id += 1
writerM = pd.ExcelWriter('C:\\Users\\spald\\Downloads\\FebruaryPhotos_Sorted\\Motion.xlsx')
dataforMotion.to_excel(writerM)
writerM.close()
