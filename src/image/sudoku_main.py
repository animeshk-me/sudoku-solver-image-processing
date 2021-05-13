

from inspect import ismemberdescriptor
from .utils import *
from .utils_tk import *
from .sudoku_solver import *


def sudoku_main(img):
    heightImg = 450
    widthImg = 450

    # Pre processing the image
    # img = cv2.imread("sudoku.jpg")
    img = cv2.resize(img, (widthImg, heightImg))
    imgBlank = np.zeros((heightImg, widthImg, 3), np.uint8)
    imgThreshold = preProcess(img)
    # cv2.imshow("PreProcessed Image", imgThreshold)
    model = intializePredectionModel()
    #Finding all contours
    imgContours = img.copy()
    imgBigContour = img.copy()
    contours, hierarchy = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 3) 
    # cv2.imshow("Draw all contours", imgContours)

    #Finding the largest contour and use it as sudoku
    biggest, maxArea = biggestContour(contours)
    # print(biggest)
    if biggest.size != 0:
        biggest = reorder(biggest)
        cv2.drawContours(imgBigContour, biggest, -1, (0,0,255), 25) #draw the biggest contour
        # cv2.imshow("Biggest contour", imgBigContour)
        pts1 = np.float32(biggest)
        pts2 = np.float32([[0,0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
        imgDetectedDigits = imgBlank.copy()
        imgWarpColored = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("warp colored image", imgWarpColored)
        imgSolvedDigits = imgBlank.copy()
        boxes = splitBoxes(imgWarpColored)
        print(len(boxes))
        # cv2.imshow("Sample",boxes[65])
        numbers = getPredection(boxes, model)
        # print(numbers)
        imgDetectedDigits = displayNumbers(imgDetectedDigits, numbers)
        numbers = np.asarray(numbers)
        posArray = np.where(numbers > 0, 0, 1)

        board = np.array_split(numbers,9)
        # print(board)
        try:
            board = solveSuduko(board, 0, 0) 
            # sudukoSolver.solve(board)
        except:
            pass
        # print(board)
        flatList = []
        for sublist in board:
            for item in sublist:
                flatList.append(item)
        solvedNumbers =flatList*posArray
        imgSolvedDigits= displayNumbers(imgSolvedDigits,solvedNumbers)
        # print(posArray)
        # for i in range(imgSolvedDigits.shape[0]):
        #     for j in range(imgSolvedDigits.shape[1]):
        #         imgSolvedDigits[i][j] += (imgSolvedDigits[i][j] + imgDetectedDigits[i][j]) / 2
        imgSolvedDigits = imgSolvedDigits/2 + imgDetectedDigits/2
        return imgSolvedDigits
    
    #split the image and find each digit available
    # imgSolvedDigits = imgBlank.copy()
    # boxes = splitBoxes(imgWarpColored)
    # print(boxes)
    # print(len(boxes))
    # cv2.imshow("sample small box", boxes[76])

    # print(numbers)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()