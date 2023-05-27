#!/usr/bin/python3

import sys

from PyQt5.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QWidget,
    QApplication
)
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class About(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        self.setGeometry(650, 300, 600, 400)
        
        
        """ADD CUSTOM FONT TO ARRAY READY TO BE LOADED TO ANY TEXT OBJECT"""
        font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
        if font >= 0:
            fonts = QFontDatabase.applicationFontFamilies(font)
        else:
            print("Error loading fonts!")

        main_layout = QVBoxLayout()

        """INIT THE OUR STORY LAYOUT"""
        our_story_layout = QVBoxLayout()
        our_story_header = QLabel()
        our_story_header.setText("About MarketApp")
        our_story_header.setFont(QFont(fonts[0], 9).setBold(True))
        
        
        description_text = "<font size='4'>MarketApp is a hobby-project created by students and professionals,<br>" \
                            "aiming to create an environment for training and gaining new skills:<br>" \
                            "* Python coding skills<br>" \
                            "* Using Python libraries (pyqt5, sshtunnel, python-decouple, etc.)<br>" \
                            "* Linux-based Operating Systems<br>" \
                            "* PostreSQL - Install, Configure and work with database<br>" \
                            "* Qt Framework<br>" \
                            "* Git/GitHub<>br" \
                            "* Project Management and Team-work<br>" \
                            "</font>"
        our_story = QLabel()
        our_story.setText(description_text)
        our_story.setFont(QFont(fonts[0], 9))

        our_story_layout.addWidget(our_story_header)
        our_story_layout.addWidget(our_story)
        our_story_layout.addStretch()

        """CONTACT US LAYOUT"""
        contact_us_layout = QVBoxLayout()
        contact_us = QLabel()
        contact_us.setText("<b><font size='4'>Contact Us</font></b><br>"
                           "123-456-7890<br>"
                           "stake_robe@example.com")

        contact_us_layout.addWidget(contact_us)
        contact_us_layout.addStretch()

        """CONTRIBUTORS LAYOUT"""
        contributors_layout = QVBoxLayout()

        contributors_header = QLabel()
        contributors_header.setText("<b><font size='4'>Contributors</font></b>")

        contributors_names = QLabel()
        contributors_names.setText("<font size='3'>Raya Petkova<br>"
                                 "Aleksandar Karastoyanov<br>"
                                 "Bobby Blagov</font>")

        contributors = QLabel()
        contributors.setText("Check our GitHub page <a href=\"https://github.com/Stake-And-Rope\">link</a>.")
        contributors.setOpenExternalLinks(True)

        contributors_layout.addWidget(contributors_header)
        contributors_layout.addWidget(contributors_names)
        contributors_layout.addWidget(contributors)
        contributors_layout.addStretch()


        """ADDING ALL LAYERS TO MAIN LAYOUT"""
        main_layout.addLayout(our_story_layout)
        main_layout.addLayout(contact_us_layout)
        main_layout.addLayout(contributors_layout)

        self.setLayout(main_layout)


app = QApplication(sys.argv)
about_window = About()
about_window.show()
app.exec_()