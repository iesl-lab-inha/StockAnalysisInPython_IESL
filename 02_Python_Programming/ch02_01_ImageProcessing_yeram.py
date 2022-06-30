import requests
from PIL import Image
import hashlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 2.8.1 리퀘스트로 인터넷에서 이미지 파일 가져오기
url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA2MTBfMTgy%2FMDAxNjIzMjkwMzI4OTkx.1rNNli3spg-ic5WOm2acv61t0NJYcyC3nx6--u94qz0g.oMX3-MXdyDhOjX6lHkCeoaaNtnSbWdhdzVa3ddujphsg.JPEG.kimjin8946%2F36.jpg&type=sc960_832'
r = requests.get(url, stream=True).raw # image file download

# 2.8.2 필로우로 이미지 보여주기
img = Image.open(r) # Open the response object received with requests as an image
img.show() # show image
img.save('src.png') # save image

# 2.8.3 'with ~ as 파일 객체:'로 이미지 파일 복사
BUF_SIZE = 1024
with open('src.png', 'rb') as sf, open('dst.png', 'wb')as df: #Create a sf file object by opening the source image file in rb mode, and create a df file object by opening the destination image file in wb mode
    while True:
        data = sf.read(BUF_SIZE) # Read 1024 bytes from the sf file object
        if not data:
            break # If there's no data to read, break
        df.write(data) # Write the read data to the df file object

# 2.8.4 SHA-256으로 파일 복사 검증하기
sha_src = hashlib.sha256()
sha_dst = hashlib.sha256() # Create hash objects for source and copy image files

with open('src.png', 'rb') as sf, open('dst.png','rb') as df:
    sha_src.update(sf.read())
    sha_dst.update(df.read()) # Update hash object

print("src.png's hash : {}".format(sha_src.hexdigest()))
print("dst.png's hash : {}".format(sha_dst.hexdigest())) # Outputs the hash values of the source and copy image files in hexadecimal

# 2.8.5 맷플롯립으로 이미지 가공하기
plt.suptitle('Image Processing', fontsize=18)
plt.subplot(1, 2, 1) # 1행 2열의 영역에서 첫 번째 영역으로 지정
plt.title('Original Image')
plt.imshow(mpimg.imread('src.png')) # 원본 파일을 읽어서 이미지로 표시

plt.subplot(122) # 1행 2열의 영역에서 두 번째 영역으로 지정 
plt.title('Pseudocolor Image')
dst_img = mpimg.imread('dst.png')
pseudo_img = dst_img [:, :, 0]  # 의사 색상 적용
plt.imshow(pseudo_img) # 의사 색상을 적용한 사본 이미지 표시
plt.show()

        
    


