import os
import zipfile

os.chdir('/Users/Eremes/Desktop')
testZip = zipfile.ZipFile('test.zip')

indexInfo = testZip.getinfo('testJS/index.html')
print("Compressed file is %sx smaller!" % (round(indexInfo.file_size / indexInfo.compress_size, 2)))

testZip.close()
