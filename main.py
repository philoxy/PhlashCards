import sys, os, json, random
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader

from mainWindow import Ui_MainWindow
from importSets import Ui_importSets
from home import Ui_home
from flashcards import Ui_flashcards
from dictionary import Ui_dictionary

app = QApplication(sys.argv)

currSet = None
quizType = 0
questions = []
currQuestion = 0
currWord = ""
reverseQuestion = False
questionsCorrect = 0
questionsWrong = 0
shuffle = False
practicing = False

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

def goto_home():
    global currSet, practicing
    window.ui.sw.setCurrentIndex(0)
    home.selectQuizType()
    home.ui.button_start.setText("Start")
    if practicing:
        home.ui.button_start.setText("Continue")

def goto_importSets():
    window.ui.sw.setCurrentIndex(1)

def goto_dict():
    window.ui.sw.setCurrentIndex(3)
    dictWin.refresh()

class mainWindow(QMainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sw.addWidget(home)
        self.ui.sw.addWidget(importSets)
        self.ui.sw.addWidget(flashcards)
        self.ui.sw.addWidget(dictWin)
        self.ui.sw.setCurrentIndex(0)
        self.setFixedSize(640, 480)
        self.setWindowTitle("PhlashCards")

class flashcardsWindow(QDialog):
    def __init__(self):
        super(flashcardsWindow, self).__init__()
        self.ui = Ui_flashcards()
        self.ui.setupUi(self)
        self.ui.button_flip.clicked.connect(self.revealAnswer)
        self.ui.button_home.clicked.connect(goto_home)
        self.ui.button_know3.setHidden(True)
        self.ui.button_know0.setHidden(True)
        self.ui.button_know3.clicked.connect(self.correct)
        self.ui.button_know0.clicked.connect(self.again)
        self.setWindowTitle("PhlashCards - Studying")

    def loadQuestion(self):
        global questions, currQuestion, reverseQuestion, questions, questionsWrong, questionsCorrect
        self.ui.label_stats.setText(f'{questionsWrong} Not guessed, {questionsCorrect} Guessed, {len(questions)} Remaining')
        try:
            self.ui.label_acc.setText(f'Accuracy: {round(questionsCorrect/(questionsCorrect+questionsWrong)*100, 1)}%')
        except ZeroDivisionError:
            self.ui.label_acc.setText(f'Accuracy: 0%')
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
        global currQuestion, shuffle, questions, reverseQuestion, questionsWrong
        if not shuffle:
            currQuestion += 1
        else:
            currQuestion = random.randint(0, len(questions)-1)
        questionsWrong += 1
        self.loadQuestion()

    def correct(self):
        global currQuestion, reverseQuestion, questionsCorrect
        if shuffle:
            currQuestion = random.randint(0, len(questions)-1)
        questions.remove(questions[currQuestion])
        questionsCorrect += 1
        self.loadQuestion()

class homeWindow(QDialog):
    def __init__(self):
        super(homeWindow, self).__init__()
        self.ui = Ui_home()
        self.ui.setupUi(self)
        self.setWindowTitle("PhlashCards")
        self.ui.button_start.setEnabled(False)
        self.ui.button_start.clicked.connect(self.start)
        self.ui.button_import.clicked.connect(goto_importSets)
        self.ui.dropdown_type.currentIndexChanged.connect(self.selectQuizType)
        self.ui.dropdown_shuffle.currentIndexChanged.connect(self.shuffle)
        self.ui.dropdown_reverse.currentIndexChanged.connect(self.reverse)
        self.ui.label_selectset.setHidden(False)
        self.setWindowTitle("PhlashCards - Home")

    def start(self):
        global currSet, quizType, questions, shuffle, practicing
        quizType = self.ui.dropdown_type.currentIndex()
        if quizType == 0:
            if shuffle and not practicing:
                currQuestion = random.randint(0, len(questions))
            practicing = True
            window.ui.sw.setCurrentIndex(2)

        flashcards.loadQuestion()

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
        self.ui.button_home.clicked.connect(goto_home)
        self.ui.button_dict.clicked.connect(goto_dict)

        self.ui.table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        for i in range(1):
            self.ui.table.setColumnWidth(i, self.ui.table.width()/2)
        self.ui.table.itemClicked.connect(self.selectListItem)

        self.ui.label_currset.setText(f'Current Set: {currSet}')
        self.ui.button_dict.setEnabled(False)
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
        global currSet, questions, practicing
        setList = getSets()
        selectedSet = self.ui.table.selectionModel()
        if selectedSet.hasSelection():
            current_index = selectedSet.currentIndex()
            row = current_index.row()
            currSet = setList[2][row]
        self.ui.label_currset.setText(f'Current Set: {setList[0][row]}')
        self.ui.button_dict.setEnabled(False)
        if currSet != None:
            self.ui.button_dict.setEnabled(True)

        questions.clear()
        with open(f'sets/{currSet}/info.json', 'r') as currentSet:
            tempQuestions = json.load(currentSet)["questions"]
            for question in tempQuestions:
                questions.append(tempQuestions[question])
        practicing = False

class dictWindow(QDialog):
    def __init__(self, parent=None):
        super(dictWindow, self).__init__(parent)
        self.ui = Ui_dictionary()
        self.ui.setupUi(self)

        self.qhide = False
        self.ahide = False

        self.ui.button_home.clicked.connect(goto_home)
        self.ui.button_home.clicked.connect(goto_importSets)
        self.ui.button_hideq.clicked.connect(self.toggleQ)
        self.ui.button_hidea.clicked.connect(self.toggleA)
        self.ui.button_edit.setEnabled(False)

        for i in range(1):
            self.ui.table.setColumnWidth(i, self.ui.table.width()/2)
        self.ui.table.itemClicked.connect(self.selectListItem)

    def toggleA(self):
        if self.ahide:
            self.ahide = False
            self.ui.button_hidea.setText("Hide answers")
        else:
            self.ahide = True
            self.ui.button_hidea.setText("Show answers")
        self.refresh()

    def toggleQ(self):
        if self.qhide:
            self.qhide = False
            self.ui.button_hideq.setText("Hide questions")
        else:
            self.qhide = True
            self.ui.button_hideq.setText("Show questions")
        self.refresh()

    def refresh(self):
        global currSet

        self.questionList = []
        with open(f'sets/{currSet}/info.json', 'r') as currentSet:
            tempQuestions = json.load(currentSet)
            for question in tempQuestions["questions"]:
                self.questionList.append(tempQuestions["questions"][question])
            currName = tempQuestions["info"]["title"]

        self.ui.table.setRowCount(len(self.questionList))
        self.ui.table.setColumnCount(2)
        self.ui.table.setHorizontalHeaderLabels(["Question", "Answer"])

        self.ui.label_currset.setText(f'Current Set: {currName} - {len(self.questionList)} Questions')

        for i in range(len(self.questionList)):
            if not self.qhide:
                set_name = QTableWidgetItem(self.questionList[i][0])
            else:
                set_name = QTableWidgetItem("")
            if not self.ahide:
                set_desc = QTableWidgetItem(self.questionList[i][1])
            else:
                set_desc = QTableWidgetItem("")
            self.ui.table.setItem(i, 0, set_name)
            self.ui.table.setItem(i, 1, set_desc)

    def selectListItem(self):
        global currWord
        selectedSet = self.ui.table.selectionModel()
        if selectedSet.hasSelection():
            current_index = selectedSet.currentIndex()
            row = current_index.row()
            currWord = row
            self.ui.button_edit.setEnabled(True)

home = homeWindow()
importSets = importWindow()
flashcards = flashcardsWindow()
dictWin = dictWindow()
window = mainWindow()

window.show()

sys.exit(app.exec())
