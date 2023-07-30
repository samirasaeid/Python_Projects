# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
from lxml import etree as ET


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(917, 828)
        Form.setStyleSheet(u".QWidget {\n"
"   background-color: beige;\n"
"}\n"
"\n"
"/* Nice Windows-XP-style password character. */\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character: 9679;\n"
"}\n"
"\n"
"/* We provide a min-width and min-height for push buttons\n"
"   so that they look elegant regardless of the width of the text. */\n"
"QPushButton {\n"
"    background-color: palegoldenrod;\n"
"    border-width: 2px;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 5;\n"
"    padding: 3px;\n"
"    min-width: 9ex;\n"
"    min-height: 2.5ex;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: khaki;\n"
"}\n"
"\n"
"/* Increase the padding, so the text is shifted when the button is\n"
"   pressed. */\n"
"QPushButton:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: #d0d67c;\n"
"}\n"
"\n"
"QLabel, QAbstractButton {\n"
"    font: bold;\n"
"}\n"
"\n"
"/* Mark mandatory fields with a brownish color. */\n"
".mandatory {\n"
"    color: brown;\n"
""
                        "}\n"
"\n"
"/* Bold text on status bar looks awful. */\n"
"QStatusBar QLabel {\n"
"   font: normal;\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border-width: 1;\n"
"    border-color: darkkhaki;\n"
"    border-style: solid;\n"
"    border-radius: 2;\n"
"}\n"
"\n"
"QComboBox, QLineEdit, QSpinBox, QTextEdit, QListView {\n"
"    background-color: cornsilk;\n"
"    selection-color: #0a214c; \n"
"    selection-background-color: #C19A6B;\n"
"}\n"
"\n"
"QListView {\n"
"    show-decoration-selected: 1;\n"
"}\n"
"\n"
"QListView::item:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* We reserve 1 pixel space in padding. When we get the focus,\n"
"   we kill the padding and enlarge the border. This makes the items\n"
"   glow. */\n"
"QLineEdit, QFrame {\n"
"    border-width: 2px;\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border-color: darkkhaki;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* As mentioned above, eliminate the padding and increase the border. */\n"
"QLineEdit:focus, QFrame:focus {\n"
""
                        "    border-width: 3px;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"/* A QLabel is a QFrame ... */\n"
"QLabel {\n"
"    border: none;\n"
"    padding: 0;\n"
"    background: none;\n"
"}\n"
"\n"
"/* A QToolTip is a QLabel ... */\n"
"QToolTip {\n"
"    border: 2px solid darkkhaki;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"    opacity: 200;\n"
"}\n"
"\n"
"/* Nice to have the background color change when hovered. */\n"
"QRadioButton:hover, QCheckBox:hover {\n"
"    background-color: wheat;\n"
"}\n"
"\n"
"/* Force the dialog's buttons to follow the Windows guidelines. */\n"
"QDialogButtonBox {\n"
"    button-layout: 0;\n"
"}\n"
"")
        self.Output_Group = QGroupBox(Form)
        self.Output_Group.setObjectName(u"Output_Group")
        self.Output_Group.setGeometry(QRect(480, 330, 391, 101))
        font = QFont()
        font.setFamily(u"MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Output_Group.setFont(font)
        self.Output_Group.setAutoFillBackground(False)
        self.High = QRadioButton(self.Output_Group)
        self.High.setObjectName(u"High")
        self.High.setGeometry(QRect(50, 30, 95, 20))
        font1 = QFont()
        font1.setFamily(u"MS Serif")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.High.setFont(font1)
        self.Low = QRadioButton(self.Output_Group)
        self.Low.setObjectName(u"Low")
        self.Low.setGeometry(QRect(50, 60, 141, 20))
        self.Low.setFont(font1)
        self.Mode_Group = QGroupBox(Form)
        self.Mode_Group.setObjectName(u"Mode_Group")
        self.Mode_Group.setGeometry(QRect(60, 200, 401, 231))
        self.Mode_Group.setFont(font)
        self.Mode_Group.setAutoFillBackground(False)
        self.Input = QRadioButton(self.Mode_Group)
        self.Input.setObjectName(u"Input")
        self.Input.setGeometry(QRect(70, 40, 181, 51))
        self.Input.setFont(font1)
        self.Output = QRadioButton(self.Mode_Group)
        self.Output.setObjectName(u"Output")
        self.Output.setGeometry(QRect(70, 150, 131, 41))
        self.Output.setFont(font1)
        self.Select_Group = QGroupBox(Form)
        self.Select_Group.setObjectName(u"Select_Group")
        self.Select_Group.setGeometry(QRect(60, 40, 811, 151))
        font2 = QFont()
        font2.setFamily(u"MS Sans Serif")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.Select_Group.setFont(font2)
        self.Select_Group.setAutoFillBackground(False)
        self.Port_Comb = QComboBox(self.Select_Group)
        self.Port_Comb.addItem("")
        self.Port_Comb.addItem("")
        self.Port_Comb.addItem("")
        self.Port_Comb.addItem("")
        self.Port_Comb.setObjectName(u"Port_Comb")
        self.Port_Comb.setGeometry(QRect(40, 90, 231, 31))
        font3 = QFont()
        font3.setFamily(u"Cambria Math")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setWeight(50)
        self.Port_Comb.setFont(font3)
        self.Port_label = QLabel(self.Select_Group)
        self.Port_label.setObjectName(u"Port_label")
        self.Port_label.setGeometry(QRect(40, 50, 71, 31))
        self.Port_label.setFont(font1)
        self.PinComb = QComboBox(self.Select_Group)
        self.PinComb.addItem("")
        self.PinComb.addItem("")
        self.PinComb.addItem("")
        self.PinComb.addItem("")
        self.PinComb.addItem("")
        self.PinComb.addItem("")
        self.PinComb.addItem("")
        self.PinComb.addItem("")
        self.PinComb.setObjectName(u"PinComb")
        self.PinComb.setGeometry(QRect(460, 90, 231, 31))
        self.PinComb.setFont(font3)
        self.PinComb.setInputMethodHints(Qt.ImhNone)
        self.PinComb.setEditable(False)
        self.Pin_Label = QLabel(self.Select_Group)
        self.Pin_Label.setObjectName(u"Pin_Label")
        self.Pin_Label.setGeometry(QRect(460, 50, 51, 31))
        self.Pin_Label.setFont(font1)
        self.Save_Group = QGroupBox(Form)
        self.Save_Group.setObjectName(u"Save_Group")
        self.Save_Group.setGeometry(QRect(60, 590, 811, 181))
        self.Save_Group.setFont(font2)
        self.Save_Group.setAutoFillBackground(False)
        self.New_button = QPushButton(self.Save_Group)
        self.New_button.setObjectName(u"New_button")
        self.New_button.setGeometry(QRect(670, 30, 111, 41))
        font4 = QFont()
        font4.setFamily(u"MS Shell Dlg 2")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setWeight(75)
        self.New_button.setFont(font4)
        self.Save_button = QPushButton(self.Save_Group)
        self.Save_button.setObjectName(u"Save_button")
        self.Save_button.setGeometry(QRect(670, 80, 111, 41))
        self.Save_button.setFont(font4)
        self.Load_button = QPushButton(self.Save_Group)
        self.Load_button.setObjectName(u"Load_button")
        self.Load_button.setGeometry(QRect(670, 130, 111, 41))
        self.Load_button.setFont(font4)
        self.Save_path = QTextEdit(self.Save_Group)
        self.Save_path.setObjectName(u"Save_path")
        self.Save_path.setGeometry(QRect(20, 100, 621, 41))
        self.Configuration_label = QLabel(self.Save_Group)
        self.Configuration_label.setObjectName(u"Configuration_label")
        self.Configuration_label.setGeometry(QRect(30, 60, 231, 21))
        self.Configuration_label.setFont(font1)
        self.Code_Gen_Group = QGroupBox(Form)
        self.Code_Gen_Group.setObjectName(u"Code_Gen_Group")
        self.Code_Gen_Group.setGeometry(QRect(60, 450, 811, 131))
        self.Code_Gen_Group.setFont(font2)
        self.Code_Gen_Group.setAutoFillBackground(False)
        self.Generate_button = QPushButton(self.Code_Gen_Group)
        self.Generate_button.setObjectName(u"Generate_button")
        self.Generate_button.setGeometry(QRect(670, 70, 111, 41))
        self.Generate_button.setFont(font4)
        self.Path_Label = QLabel(self.Code_Gen_Group)
        self.Path_Label.setObjectName(u"Path_Label")
        self.Path_Label.setGeometry(QRect(30, 40, 51, 31))
        self.Path_Label.setFont(font1)
        self.output_path = QTextEdit(self.Code_Gen_Group)
        self.output_path.setObjectName(u"output_path")
        self.output_path.setGeometry(QRect(20, 70, 621, 41))
        self.Input_Group = QGroupBox(Form)
        self.Input_Group.setObjectName(u"Input_Group")
        self.Input_Group.setGeometry(QRect(480, 200, 391, 121))
        self.Input_Group.setFont(font)
        self.Input_Group.setAutoFillBackground(False)
        self.Pull_Up = QRadioButton(self.Input_Group)
        self.Pull_Up.setObjectName(u"Pull_Up")
        self.Pull_Up.setGeometry(QRect(50, 40, 95, 20))
        self.Pull_Up.setFont(font1)
        self.Pull_Down = QRadioButton(self.Input_Group)
        self.Pull_Down.setObjectName(u"Pull_Down")
        self.Pull_Down.setGeometry(QRect(50, 90, 141, 20))
        self.Pull_Down.setFont(font1)

        self.retranslateUi(Form)
        QObject.connect(self.Output,SIGNAL("clicked(bool)"),self.Input_Group.setDisabled)
        QObject.connect(self.Output,SIGNAL("clicked(bool)"),self.Output_Group.setEnabled)
        QObject.connect(self.Input,SIGNAL("clicked(bool)"),self.Input_Group.setEnabled)
        QObject.connect(self.Input,SIGNAL("clicked(bool)"),self.Output_Group.setDisabled)
        self.Generate_button.clicked.connect(self.GenerateFunction)
        self.New_button.clicked.connect(self.NewButtonFunc)
        self.Save_button.clicked.connect(self.saveButtonFunc)
        self.Load_button.clicked.connect(self.loadButtonFunc)
        self.Port_Comb.highlighted.connect(self.updateports)
        self.PinComb.highlighted.connect(self.updateports)
        self.Port_Comb.currentIndexChanged.connect(self.updateFunction)
        self.PinComb.currentIndexChanged.connect(self.updateFunction)
        QMetaObject.connectSlotsByName(Form)
    # setupUi
    
    
    def GenerateFunction(self):
      self.updateFunction()
      if self.output_path.toPlainText() != '':
        DIO_H_Handler = open(self.output_path.toPlainText() + '\DIO.h', 'w')
        DIO_Handler = open(self.output_path.toPlainText() + '\DIO_confg.h', 'w')
      else:
        DIO_Handler = open('DIO_confg.h', 'w')
        DIO_H_Handler = open('DIO.h', 'w')
      
      DIO_H_Handler.write("#ifndef DIO_H\n")
      DIO_H_Handler.write("#define DIO_H\n\n\n")
      DIO_H_Handler.write("#define DIO_INPUT                   0\n")
      DIO_H_Handler.write("#define DIO_OUTPUT                  1\n\n")
      DIO_H_Handler.write("#define DIO_PULL_UP              1\n")
      DIO_H_Handler.write("#define DIO_PULL_Down            0\n\n")
      DIO_H_Handler.write("#define DIO_HIGH                 1\n")
      DIO_H_Handler.write("#define DIO_LOW                  0\n\n")
      DIO_H_Handler.write("#endif\n")
      DIO_H_Handler.close()
      
      DIO_Handler.write("#ifndef DIO_CFG_H\n")
      DIO_Handler.write("#define DIO_CFG_H\n\n\n")
      for port in AllPorts:
        for pin in AllPorts[port][1]:
          if AllPorts[port][1][pin].strip() == "DIO_High" or AllPorts[port][1][pin].strip() == "DIO_LOW":
            DIO_Handler.write('#define DIO_'+AllPorts[port][0]+'_'+pin+'      '+"DIO_OUTPUT\n")
          else:
            DIO_Handler.write('#define DIO_'+AllPorts[port][0]+'_'+pin+'      '+"DIO_INPUT\n")
      
      DIO_Handler.write('\n\n\n')
      
      for port in AllPorts:
        for pin in AllPorts[port][1]:
            DIO_Handler.write('#define DIO_'+port+'_'+pin+'     '+AllPorts[port][1][pin])
      
      DIO_Handler.write("\n\n#endif\n")
      DIO_Handler.close()
      return
      
    def NewButtonFunc(self):
      self.Save_path.setText('')
      for port in AllPorts:
        for pin in AllPorts[port][1]:
          AllPorts[port][1][pin] = "DIO_PULL_UP\n"
      self.updateFunction()
      return
      
    def saveButtonFunc(self):
      self.updateFunction() 
      root=ET.Element("DIO")
      tree=ET.ElementTree(root)
      for port in AllPorts:
        portTag=ET.Element(port)
        root.append(portTag)
        for pin in AllPorts[port][1]:
          pinTag=ET.Element(pin)
          portTag.append(pinTag)
          pinTag.text=AllPorts[port][1][pin]                
      if self.Save_path.toPlainText() != '':
        SavedFile = self.Save_path.toPlainText()+r'\ConfigFile.xml' 
      else:
        SavedFile = 'ConfigFile.xml'
      SavedFile2=open(SavedFile,'w')
      SavedFile2.write(ET.tostring(root, pretty_print=True).decode())
      SavedFile2.close()
      return
      
    def loadButtonFunc(self):
      if self.Save_path.toPlainText() != '':
        LoadFile = self.Save_path.toPlainText()+r'\ConfigFile.xml'
      else:
        return
      tree=ET.parse(LoadFile)
      root = tree.getroot()
      for child in root:
        port=child.tag
        for x in child.iter():
          pin=x.tag
          pin_text=x.text
          #print(port,pin,pin_text)
          AllPorts[port][1][pin] = pin_text
      self.updateFunction()
      return
      
      
    def updateFunction(self):
      if (AllPorts[self.Port_Comb.currentText()][1][self.PinComb.currentText()].strip() == "DIO_HIGH"):
        self.Output.setChecked(True)
        self.Input_Group.setDisabled(True)
        self.Output_Group.setEnabled(True)
        self.High.setChecked(True)
      
      elif (AllPorts[self.Port_Comb.currentText()][1][self.PinComb.currentText()].strip() == "DIO_LOW"):
        self.Output.setChecked(True)
        self.Input_Group.setDisabled(True)
        self.Output_Group.setEnabled(True)
        self.Low.setChecked(True)
        
      elif (AllPorts[self.Port_Comb.currentText()][1][self.PinComb.currentText()].strip() == "DIO_PULL_Down"):
        self.Input.setChecked(True)
        self.Input_Group.setEnabled(True)
        self.Output_Group.setDisabled(True)
        self.Pull_Down.setChecked(True)
      
      else:
        self.Input.setChecked(True)
        self.Input_Group.setEnabled(True)
        self.Output_Group.setDisabled(True)
        self.Pull_Up.setChecked(True)
      return
    
    def updateports(self): 
        if self.Output.isChecked():
          if self.High.isChecked():
            AllPorts[self.Port_Comb.currentText()][1][self.PinComb.currentText()] = "DIO_HIGH\n"
          else:
            AllPorts[self.Port_Comb.currentText()][1][self.PinComb.currentText()] = "DIO_LOW\n"

        else:
          if self.Pull_Up.isChecked():
            AllPorts[self.Port_Comb.currentText()][1][self.PinComb.currentText()] = "DIO_PULL_UP\n"
          else:
            AllPorts[self.Port_Comb.currentText()][1][self.PinComb.currentText()] = "DIO_PULL_Down\n"
        return

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"AVR Pin Configration", None))
        self.Output_Group.setTitle(QCoreApplication.translate("Form", u"Output Level", None))
        self.High.setText(QCoreApplication.translate("Form", u"High", None))
        self.Low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.Mode_Group.setTitle(QCoreApplication.translate("Form", u"Mode", None))
        self.Input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.Output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Select_Group.setTitle(QCoreApplication.translate("Form", u"Selection", None))
        self.Port_Comb.setItemText(0, QCoreApplication.translate("Form", u"PORTA", None))
        self.Port_Comb.setItemText(1, QCoreApplication.translate("Form", u"PORTB", None))
        self.Port_Comb.setItemText(2, QCoreApplication.translate("Form", u"PORTC", None))
        self.Port_Comb.setItemText(3, QCoreApplication.translate("Form", u"PORTD", None))

        self.Port_label.setText(QCoreApplication.translate("Form", u"PORT", None))
        self.PinComb.setItemText(0, QCoreApplication.translate("Form", u"PIN0", None))
        self.PinComb.setItemText(1, QCoreApplication.translate("Form", u"PIN1", None))
        self.PinComb.setItemText(2, QCoreApplication.translate("Form", u"PIN2", None))
        self.PinComb.setItemText(3, QCoreApplication.translate("Form", u"PIN3", None))
        self.PinComb.setItemText(4, QCoreApplication.translate("Form", u"PIN4", None))
        self.PinComb.setItemText(5, QCoreApplication.translate("Form", u"PIN5", None))
        self.PinComb.setItemText(6, QCoreApplication.translate("Form", u"PIN6", None))
        self.PinComb.setItemText(7, QCoreApplication.translate("Form", u"PIN7", None))

        self.Pin_Label.setText(QCoreApplication.translate("Form", u"PIN", None))
        self.Save_Group.setTitle(QCoreApplication.translate("Form", u"Configuration Save Utility", None))
        self.New_button.setText(QCoreApplication.translate("Form", u"New", None))
        self.Save_button.setText(QCoreApplication.translate("Form", u"Save", None))
        self.Load_button.setText(QCoreApplication.translate("Form", u"Load", None))
        self.Configuration_label.setText(QCoreApplication.translate("Form", u"Configuration File Path", None))
        self.Code_Gen_Group.setTitle(QCoreApplication.translate("Form", u"Code Generation File", None))
        self.Generate_button.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.Path_Label.setText(QCoreApplication.translate("Form", u"Path", None))
        self.Input_Group.setTitle(QCoreApplication.translate("Form", u"Input Configuration", None))
        self.Pull_Up.setText(QCoreApplication.translate("Form", u"Pull Up", None))
        self.Pull_Down.setText(QCoreApplication.translate("Form", u"Pull Down", None))
    # retranslateUi
    
PORTA={"PIN0":"DIO_PULL_UP\n","PIN1":"DIO_PULL_UP\n","PIN2":"DIO_PULL_UP\n","PIN3":"DIO_PULL_UP\n","PIN4":"DIO_PULL_UP\n","PIN5":"DIO_PULL_UP\n","PIN6":"DIO_PULL_UP\n","PIN7":"DIO_PULL_UP\n"}
PORTB={"PIN0":"DIO_PULL_UP\n","PIN1":"DIO_PULL_UP\n","PIN2":"DIO_PULL_UP\n","PIN3":"DIO_PULL_UP\n","PIN4":"DIO_PULL_UP\n","PIN5":"DIO_PULL_UP\n","PIN6":"DIO_PULL_UP\n","PIN7":"DIO_PULL_UP\n"}
PORTC={"PIN0":"DIO_PULL_UP\n","PIN1":"DIO_PULL_UP\n","PIN2":"DIO_PULL_UP\n","PIN3":"DIO_PULL_UP\n","PIN4":"DIO_PULL_UP\n","PIN5":"DIO_PULL_UP\n","PIN6":"DIO_PULL_UP\n","PIN7":"DIO_PULL_UP\n"}
PORTD={"PIN0":"DIO_PULL_UP\n","PIN1":"DIO_PULL_UP\n","PIN2":"DIO_PULL_UP\n","PIN3":"DIO_PULL_UP\n","PIN4":"DIO_PULL_UP\n","PIN5":"DIO_PULL_UP\n","PIN6":"DIO_PULL_UP\n","PIN7":"DIO_PULL_UP\n"}
AllPorts={"PORTA": ["DDRA", PORTA], "PORTB": ["DDRB", PORTB], "PORTC": ["DDRC", PORTC], "PORTD": ["DDRD", PORTD]}

app = QApplication(sys.argv)
Widget = QWidget()
Form = Ui_Form()
Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())

