import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

result= 0
result_list=[]

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hesap Makinesi")
        self.setGeometry(850,200,380,550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        #####################Entry Field################

        self.entry_box=QLineEdit(self)
        self.entry_box.resize(335,30)
        self.entry_box.setAlignment(Qt.AlignRight)
        self.entry_box.setStyleSheet("font:14pt Arial Bold;border:3px solid gray;border-radius:5px;background-color:#e6e6fa;")
        self.entry_box.setText("O")
        self.entry_box.move(20,30)
        ##################Number Buttons#########################
        btn_number=[]
        for i in range(1,10):
            i =QPushButton(str(i),self)
            i.setFont(QFont("Arial",15))
            i.resize(70,40)
            i.setStyleSheet("background-color:white")
            i.clicked.connect(self.enterNumbers)
            btn_number.append(i)

        btn_index=0
        for i in range(0,3):
            for j in range(0,3):
                btn_number[btn_index].move(25+j*90,70+i*70)
                btn_index +=1
                print(i,j)
     ##############################Operator button#########################33

        btn_operator=[]
        for i in range(4):
            i=QPushButton(self)
            i.resize(70,40)
            i.setStyleSheet("background-color:white")
            i.setFont(QFont("Arial",15))
            i.clicked.connect(self.enterOperator)
            btn_operator.append(i)

        btn_operator[0].setText("+")
        btn_operator[1].setText("-")
        btn_operator[2].setText("*")
        btn_operator[3].setText("/")


        for i in range(4):
            btn_operator[i].move(290,70+i*70)


        ################Other buttons#############3
        btn_zero=QPushButton("0",self)
        btn_zero.setStyleSheet("background-color:white")
        btn_zero.setFont((QFont("Arial",20)))
        btn_zero.resize(250,40)
        btn_zero.clicked.connect(self.enterNumbers)
        btn_zero.move(25,280)
        ##################################################
        btn_clear=QPushButton("C",self)
        btn_clear.setStyleSheet("background-color:white")
        btn_clear.setFont(QFont("Arial",20))
        btn_clear.resize(70,40)
        btn_clear.clicked.connect(self.funcClear)
        btn_clear.move(25,340)
        ##################################################
        btn_dot=QPushButton(".",self)
        btn_dot.setStyleSheet("background-color:white")
        btn_dot.setFont(QFont("Arial", 15) )
        btn_dot.resize(70, 40)
        btn_dot.clicked.connect(self.enterNumbers)
        btn_dot.move(110,340)
        ##################################################
        btn_equal=QPushButton("=",self)
        btn_equal.setStyleSheet("background-color:white")
        btn_equal.setFont(QFont("Arial", 15))
        btn_equal.resize(70, 40)
        btn_equal.clicked.connect(self.funcOperator)
        btn_equal.move(200, 340)
        ##################################################
        btn_delete=QPushButton(self)
        btn_delete.setIcon(QIcon('icons/arrow.png'))
        btn_delete.setStyleSheet("background-color:white")
        btn_delete.setFont(QFont("Arial", 15))
        btn_delete.resize(70, 40)
        btn_delete.clicked.connect(self.funcDelete)
        btn_delete.move(290, 340)
        ##############status bar######################
        self.status_bar=QStatusBar()
        self.setStatusBar(self.status_bar)


    def enterNumbers(self):
        btn_text=self.sender().text()
        print(btn_text)
        if self.entry_box.text()=="O":
            self.entry_box.setText("")
            self.entry_box.setText(btn_text)
        else:
            self.entry_box.setText(self.entry_box.text()+btn_text)

    def enterOperator(self):
        btn_text=self.sender().text()
        if self.entry_box.text() !="O":
            self.entry_box.setText(self.entry_box.text()+btn_text)

    def funcClear(self):
        self.entry_box.setText("O")
    def funcDelete(self):
        x=self.entry_box.text()
        print(x)
        x=x[:-1]
        self.entry_box.setText(x)
        if len(x)==0:
            self.entry_box.setText("O")
    def funcOperator(self):
        content=self.entry_box.text()
        result=eval(content)
        print(result)
        self.entry_box.setText(str(result))
        result_list.append(content)
        result_list.reverse()
        self.status_bar.showMessage('History'+ '|'.join(result_list[:5]))
        self.status_bar.setFont(QFont("Verdana",15))





def main():
    App=QApplication(sys.argv)
    window =Calculator()
    sys.exit(App.exec_())
if __name__=='__main__':
     main()



