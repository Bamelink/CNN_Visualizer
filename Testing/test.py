import json
import numpy # pip install numpy
from sklearn import metrics # pip install scikit-learn
import matplotlib.pyplot as plt # pip install matplotlib
from PIL import Image

def getGenderAndAge(filepath):
    f = open(filepath)
    
    # returns JSON object as a dictionary
    data = json.load(f)
    
    # Iterating through the json list
    for i in data['FaceDetails']:
        agerange = i['AgeRange']
        gender = i['Gender']
        print(f"Detectet person with an age of {agerange['Low']} to {agerange['High']} of gender {gender['Value']}")
        return (agerange, gender['Value'])
        
    # Closing file
    f.close()


def createConfusionMatrix(actual, predicted):
    confusion_matrix = metrics.confusion_matrix(actual, predicted)
    cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])
    cm_display.plot()
    plt.show()


def main():
    getGenderAndAge(r'./response.json')

    
    
    
if __name__ == "__main__":
    main()