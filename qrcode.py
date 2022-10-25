# Python İle PC Üzerinden QR Kod Okutma İşlemi. 
# The QR code reading program with Python works only on the computer.

import cv2
import webbrowser


cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:
    _, img = cap.read()
    data, one, _ = detector.detectAndDecode(img)
    if data:
        link = data
        break
    cv2.imshow('QR Code Reader', img)
    if cv2.waitKey(1) == ord('q'):
        break
b = webbrowser.open(str(link))
cap.relase(link)
cv2.destroyAllWindows
