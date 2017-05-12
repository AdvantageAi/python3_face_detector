import cv2
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("harr_file", type=str, 
                    help="location of Harr Cascade to do detection")
parser.add_argument('img_locations', metavar='N', type=str, nargs='+',
                    help='will create a list of images to process')
parser.add_argument("--crop", action="store_true")


def main(detectorPath, imagePathes, crop=False):
    detector = load_detector(detectorPath)
    for img in imagePathes:
        image = cv2.imread(img)
        faces = find_faces(image, detector)
        print("Found {} in {}".format(len(faces), img))
        if crop:
            results = crop_faces(image, faces)
        else:
            results = draw_bbox(image, faces)
            # Save results
            savePath = img.split(".")
            savePath = savePath[0] + "_boxed." + savePath[1]
            print(savePath)
            cv2.imwrite(savePath, results)


def load_detector(cascadePath):
    # load detector
    return cv2.CascadeClassifier(cascadePath)


def find_faces(img, detector,
               scaleFactor=1.1, minNeighbors=10, minSize=(20, 20)):
    """ Returns list of face bounding boxes.
    """
    # gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # find the faces
    face_bboxes = detector.detectMultiScale(
        gray,
        scaleFactor=scaleFactor,
        minNeighbors=minNeighbors,
        minSize=minSize
    )
    return face_bboxes


def draw_bbox(img, bboxes, color=(255, 20, 147), lineWidth=2):
    for (x, y, w, h) in bboxes:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, lineWidth)
    return img


def crop_faces():
    # TODO
    pass


if __name__ == "__main__":
    args = parser.parse_args()
    main(detectorPath=args.harr_file, imagePathes=args.img_locations)