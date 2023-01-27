import cv2
import pytesseract
from pytesseract import Output

def isNumeric(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def main():
    
    image = cv2.imread("card5.png")
    image = cv2.resize(image, (700,500))
    image = cv2.GaussianBlur(image, (5, 5),0)
    Mrot = cv2.getRotationMatrix2D((350, 250), 6, 1) # desde -7 hasta 6 grados de rotación
    image = cv2.warpAffine(image, Mrot, (700, 500))
    image1 = image.copy()
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
    
    box = pytesseract.image_to_data(image_gray, output_type=Output.DICT)
    
    n_boxes = len(box['text'])
    for i in range(n_boxes):
        if int(box['conf'][i]) > 50:
            text = box['text'][i]
            if isNumeric(text):
                (x, y, w, h) = (box['left'][i], box['top'][i], box['width'][i], box['height'][i])
                image1 = cv2.rectangle(image1, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(image1, text, (x-10,y-20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                
    cv2.imshow("Imagen",image1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
    

    

