import glob
import PIL.Image
import os
import re
#Simple version of script for speed renaming
for filename in glob.iglob('C:\\Users\\spald\\Downloads\\FebruaryPhotos_Sorted\\FebruaryPhotos_Sorted\\[a-zA-Z][0-9][0-9]\\*', recursive=True):
    try:
        img = PIL.Image.open(filename)
    except:
        print(filename + " is corrupted")
        continue
#If one wants the regex piece could be replaced by string based counting methods. This would be faster but would require more work
 #This finds the place where you would want to move the photos based on the pattern of anything a slash a letter a number a second number and two slashs and exports it to the form of string
    filename2 = re.search(r'.*\\[a-zA-Z][0-9][0-9]\\',filename).group()
    #This does the same thing as the last 1 with 1 key differnce being that it doesn't extract anything from before the first slash the result should be something like \\C01\\
    sitewithslash = re.search(r'\\[a-zA-Z][0-9][0-9]\\', filename).group()
    #This removes the slashes from around the site name using string indexing.
    site=sitewithslash[1:4]
    Timelapse10AMFolderPath=filename2[:-4]+"Timelapse\\"+site+'Timelapse'
    NotTimelapseFolderPath=filename2
    #This part checks if the folders to add the timelapse and non timelapse photos to exists and if not it makes it
    if not os.path.exists(Timelapse10AMFolderPath):
        os.makedirs(Timelapse10AMFolderPath)
    if not os.path.exists(NotTimelapseFolderPath):
        os.makedirs(NotTimelapseFolderPath)
    exif_data = img._getexif()
    pimagename=exif_data[306].replace(" ", "")
    imagename=pimagename.replace(":", "")
    imagename=imagename+site
    Timelapse10AMPhotoPath = Timelapse10AMFolderPath + '\\' + imagename + '.jpg'
    Timelapse10AMPhotoPath2 = Timelapse10AMFolderPath + '\\' + imagename + 'Duplicate.jpg'
    NotTimelapsePhotoPath = NotTimelapseFolderPath + '\\' + imagename + '.jpg'
    img.close()
    datetime = exif_data[306].split(" ")
    date = datetime[0].replace(":", "//")
    time = datetime[1]
    if time=='10:00:00':
        try:
            os.rename(filename,Timelapse10AMPhotoPath)
        except:
           print(filename + " has a motion and timelapse both at 10 am")
           os.rename(filename, Timelapse10AMPhotoPath2)
           continue
    else:
        os.rename(filename,NotTimelapsePhotoPath)