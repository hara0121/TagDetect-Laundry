import cv2#画像や動画を処理するオープンライブラリ

# 画像を読み込みます
img = cv2.imread("D:/wash-material/40_resize/wash40.jpg")

# 画像を表示するウィンドウの名前は"sample"
# 読み込んだ画像は"img"です
cv2.imshow("sample", img)
cv2.waitKey(0)