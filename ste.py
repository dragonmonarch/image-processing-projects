# mean filter



import cv2
img = cv2.imread("train.jpg")
img1 = img.copy()
m,n,p = img.shape

for k in range(0,p):
    for i in range(1,m-1):
        for j in range(1,n-1):
           z =  img1[i-1,j-1,k]+img1[i-1,j,k]+img1[i-1,j+1,k]+img1[i,j-1,k]+img1[i,j,k]+img1[i,j+1,k]+img1[i+1,j-1,k]+img1[i+1,j,k]+img1[i+1,j+1,k]
           me = z//9
           img1[i,j,k] = me

cv2.imshow("original",img)
cv2.imshow("new",img1)
cv2.waitKey()
cv2.destroyAllWindows()





#median filter 

# import cv2
# img = cv2.imread("train.jpg")
# img1 = img.copy()
# m,n,p = img.shape

# for k in range(0,p):
#     for i in range(1,m-1):
#         for j in range(1,n-1):
#            list1 =  [img1[i-1,j-1,k],img1[i-1,j,k],img1[i-1,j+1,k],img1[i,j-1,k],img1[i,j,k],img1[i,j+1,k],img1[i+1,j-1,k],img1[i+1,j,k],img1[i+1,j+1,k]]
#            z = sorted(list1)
#            me = z[4]
#            img1[i,j,k] = me

# cv2.imshow("original",img)
# cv2.imshow("new",img1)
# cv2.waitKey()
# cv2.destroyAllWindows()


# #mode filter 

# import cv2
# img = cv2.imread("itachi.png")
# img1 = img.copy()
# m,n,p = img.shape
# count = 0

# for k in range(0,p):
#     for i in range(0,m-1):
#         for j in range(0,n-1):
#             z =  [img1[i-1,j-1,k],img1[i-1,j,k],img1[i-1,j+1,k],img1[i,j-1,k],img1[i,j,k],img1[i,j+1,k],img1[i+1,j-1,k],img1[i+1,j,k],img1[i+1,j+1,k]]
#             v = z[0]
#             for ab in z:
#                 mode = z.count(ab)
#                 if mode > count :
#                     count=mode
#                     v = ab
#                     img1[i,j,k] = v 
# cv2.waitKey(0)
# cv2.destroyAllWindows()





# dot detection
# import cv2
# img = cv2.imread("C:\\Users\\drago\\Downloads\\dot.png")
# img1 = img.copy()
# m,n,p = img.shape
# count = 0
# for k in range(0,p):
#      for i in range(1,m-1):
#          for j in range(1,n-1):
#               if int(img1[i,j,k]-img1[i-1,j,k]+img1[i,j,k]-img1[i,j-1,k]+img1[i,j,k]-img1[i,j+1,k]+img1[i,j,k]-img1[i+1,j,k])/4 >6 :
#                   count += 1
# if count > 0:
#      print('dot is present')
# else:
#      print('not present')


#water mark


# import cv2 
# img = cv2.imread("itachi.png")
# img2 = cv2.imread("itachi.png")

# m,n,p = img.shape
# img3 = img.copy()
# for k in range(0,p):
#     for i in range(1,m-1):
#         for j in range(1,n-1):
#             if img2[i][j][k] >50:
#                 img3[i][j][k] = img2[i][j][k]

# cv2.imshow("vyt", img3)
# cv2.waitKey(0)
# cv2.destroyAllWindows()










