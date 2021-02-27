
########################################################################################################################
# McGill Rocket Team Avionics Ground Simulator                                                                         #
#                                                                                                                      #
# Loading Circular Progress Program to show the users the percentage of simulations loaded in the .csv file            #
#                                                                                                                      #
# IMPORTANT NOTICE: The code has been written by following a modern UI tutorials, credits to Wanderson on YouTube      #
#                                                                                                                      #
#                                                                                                                      #
#                                                                                                                      #
########################################################################################################################





import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# Import the ui_ProgressCircle.ui file
from ui_ProgressCircle import Ui_LoadingScreen


class ProgressCircle(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_LoadingScreen()
        self.ui.setupUi(self)

        # Test the progress bar function --> works all fine
        # self.progressBarValue(20)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Set the background transparent

        # Show main window
        self.show()
        # End main window

    # Progress bar Value
    def progressBarValue(self, value):
        # PROGRESSBAR STYLESHEET BASE

        stylesheet = """
        QFrame{
            border-radius: 150px; background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_VALUE_1} 
            rgba(0, 0, 0, 0), stop:{STOP_VALUE_2} rgba(140, 0, 20, 255));
        }
        """

        # Getters
        # Get progress bar value, convert to float and invert values
        # The stop values range from 1.000 to 0.000
        progress = (100 - value) / 100.0

        stop_value_1 = str(progress - 0.001)
        stop_value_2 = str(progress)

        # Setters
        # Sets values to the stylesheet
        newstylesheet = stylesheet.replace("{STOP_VALUE_1}", stop_value_1).replace("{STOP_VALUE_2}", stop_value_2)

        # Update the old style sheet with the new style sheet
        self.ui.circularProgressBar.setStyleSheet(newstylesheet)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProgressCircle()
    sys.exit(app.exec_())