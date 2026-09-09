import sys, os, json, random
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader

from mainWindow import Ui_MainWindow
from importSets import Ui_importSets
from home import Ui_home
from flashcards import Ui_flashcards

app = QApplication(sys.argv)

currSet = None
quizType = 0
questions = []
currQuestion = 0
reverseQuestion = False

def getSets():
    setList = [[], [], []]
    sets = []

    dirs = os.scandir("sets/")
    for i in dirs:
        if i.is_dir():
            sets.append(i.name)

    for dir in sets:
        with open(f'sets/{dir}/info.json', 'r') as info:
            data = json.load(info)["info"]
            setList[0].append(data["title"])
            setList[1].append(data["desc"])
            setList[2].append(f'{dir}')

    return setList

class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sw.addWidget(home)
        self.ui.sw.addWidget(importSets)
        self.ui.sw.addWidget(flashcards)
        self.ui.sw.setCurrentIndex(0)
        self.setFixedSize(640, 480)
        self.setWindowTitle("PhlashCards")

class flashcardsWindow(QDialog):
    def __init__(self):
        super(flashcardsWindow, self).__init__()
        self.ui = Ui_flashcards()
        self.ui.setupUi(self)
        self.ui.button_flip.clicked.connect(self.revealAnswer)
        self.ui.button_know3.setHidden(True)
        self.ui.button_know0.setHidden(True)
        self.ui.button_know3.clicked.connect(self.correct)
        self.ui.button_know0.clicked.connect(self.again)
        self.setWindowTitle("PhlashCards - Studying")

    def loadQuestion(self):
        global questions, currQuestion, reverseQuestion, questions
        self.ui.button_know3.setHidden(True)
        self.ui.button_know0.setHidden(True)
        if currQuestion+1 > len(questions):
            currQuestion = 0
        if len(questions) > 0:

            questionNumber = 0
            if reverseQuestion:
                questionNumber = 1

            self.ui.label_question.setText(f'{questions[currQuestion][questionNumber]}')
            self.ui.label_answer.setText("")
        else:
            window.ui.sw.setCurrentIndex(0)

    def revealAnswer(self):
        global reverseQuestion, questions, currQuestion

        questionNumber = 1
        if reverseQuestion:
            questionNumber = 0

        self.ui.label_answer.setText(f'Answer:\n{questions[currQuestion][questionNumber]}')
        self.ui.button_know3.setHidden(False)
        self.ui.button_know0.setHidden(False)

    def again(self):
        global currQuestion, shuffle, questions, reverseQuestion
        if not shuffle:
            currQuestion += 1
        else:
            currQuestion = random.randint(0, len(questions)-1)
        self.loadQuestion()

    def correct(self):
        global currQuestion, reverseQuestion
        if shuffle:
            currQuestion = random.randint(0, len(questions)-1)
        questions.remove(questions[currQuestion])
        self.loadQuestion()

class homeWindow(QDialog):
    def __init__(self):
        super(homeWindow, self).__init__()
        self.ui = Ui_home()
        self.ui.setupUi(self)
        self.setWindowTitle("PhlashCards")
        self.ui.button_start.setEnabled(False)
        self.ui.button_start.clicked.connect(self.start)
        self.ui.button_import.clicked.connect(self.goto_importSets)
        self.ui.dropdown_type.currentIndexChanged.connect(self.selectQuizType)
        self.ui.dropdown_shuffle.currentIndexChanged.connect(self.shuffle)
        self.ui.dropdown_reverse.currentIndexChanged.connect(self.reverse)
        self.ui.label_selectset.setHidden(False)
        self.setWindowTitle("PhlashCards - Home")

    def start(self):
        global currSet, quizType, questions, currQuestion
        quizType = self.ui.dropdown_type.currentIndex()
        if quizType == 0:
            if shuffle:
                currQuestion = random.randint(0, len(questions)-1)
            window.ui.sw.setCurrentIndex(2)
        questions.clear()
        with open(f'sets/{currSet}/info.json', 'r') as currentSet:
            tempQuestions = json.load(currentSet)["questions"]
            for question in tempQuestions:
                questions.append(tempQuestions[question])

        flashcards.loadQuestion()

    def goto_importSets(self):
        window.ui.sw.setCurrentIndex(1)

    def selectQuizType(self):
        global currSet
        self.ui.button_start.setEnabled(False)
        home.ui.label_selectset.setHidden(False)
        home.ui.label_selectset.setHidden(True)
        if currSet != None:
            self.ui.button_start.setEnabled(True)
        else:
            home.ui.label_selectset.setHidden(False)
            home.ui.label_selectset.setText("Please select a set.")

        self.ui.dropdown_reverse.setEnabled(True)
        if self.ui.dropdown_type.currentIndex() != 0:
            self.ui.dropdown_reverse.setEnabled(False)

    def shuffle(self):
        global shuffle
        shuffle = bool(self.ui.dropdown_shuffle.currentIndex())

    def reverse(self):
        global reverseQuestion
        reverseQuestion = bool(self.ui.dropdown_reverse.currentIndex())


class importWindow(QDialog):
    def __init__(self):
        super(importWindow, self).__init__()
        self.ui = Ui_importSets()
        self.ui.setupUi(self)
        self.setWindowTitle("PhlashCards - Import Sets")

        self.ui.button_refresh.clicked.connect(self.refresh)
        self.ui.button_home.clicked.connect(self.goto_home)
        self.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        for i in range(1):
            self.ui.table.setColumnWidth(i, self.ui.table.width()/2)
        self.ui.table.itemClicked.connect(self.selectListItem)

        self.ui.label_currset.setText(f'Current Set: {currSet}')
        self.refresh()

    def refresh(self):
        setList = getSets()
        self.ui.table.setRowCount(len(setList[0]))
        self.ui.table.setColumnCount(len(setList)-1)
        self.ui.table.setHorizontalHeaderLabels(["Name", "Description"])

        for i in range(len(setList[0])):
            set_name = QTableWidgetItem(setList[0][i])
            set_desc = QTableWidgetItem(setList[1][i])
            set_dir = QTableWidgetItem(setList[2][i])
            self.ui.table.setItem(i, 0, set_name)
            self.ui.table.setItem(i, 1, set_desc)

    def selectListItem(self):
        global currSet
        setList = getSets()
        selectedSet = self.ui.table.selectionModel()
        if selectedSet.hasSelection():
            current_index = selectedSet.currentIndex()
            row = current_index.row()
            currSet = setList[2][row]
        self.ui.label_currset.setText(f'Current Set: {setList[0][row]}')

    def goto_home(self):
        global currSet
        window.ui.sw.setCurrentIndex(0)
        home.selectQuizType()
        """
        if home.ui.dropdown_type.currentIndex() != 0 and currSet != None:
            home.ui.label_selectset.setHidden(True)
        if currSet == None:
            home.ui.label_selectset.setHidden(False)
            home.ui.label_selectset.setText("Please select a set.")
        if home.ui.dropdown_type.currentIndex() != 1:
            home.ui.label_selectset.setHidden(False)
            home.ui.label_selectset.setText("unsupported quiz type")
        if home.ui.dropdown_type.currentIndex() == 0:
            home.ui.label_selectset.setHidden(False)
            home.ui.label_selectset.setText("Please select a quiz type.")
        """

home = homeWindow()
importSets = importWindow()
flashcards = flashcardsWindow()
window = mainWindow()

window.show()

sys.exit(app.exec())
