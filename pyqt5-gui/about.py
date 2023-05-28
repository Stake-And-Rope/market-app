#!/usr/bin/python3


from PyQt5.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QWidget,
    QApplication,
)
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys
sys.path.append(r'..')
import webbrowser

class About(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        self.setGeometry(650, 300, 550, 400)
        self.setWindowIcon(QIcon(r'../img/market.png'))
        
        
        """ADD CUSTOM FONT TO ARRAY READY TO BE LOADED TO ANY TEXT OBJECT"""
        font = QFontDatabase.addApplicationFont(r'../fonts/jetbrains-mono.regular.ttf')
        font_two = QFontDatabase.addApplicationFont(r'../fonts/JetBrainsMonoNerdFont-Bold.ttf')
        if font >= 0:
            fonts = QFontDatabase.applicationFontFamilies(font)
            fonts = QFontDatabase.applicationFontFamilies(font_two)
        else:
            print("Error loading fonts!")

        main_layout = QVBoxLayout()

        """INIT THE OUR STORY LAYOUT"""
        our_story_layout = QVBoxLayout()
        
        our_story_header = QLabel()
        our_story_header.setText("About MarketApp")
        our_story_header.setFont(QFont(fonts[0], 14, QFont.Bold))
        
        description_text = "MarketApp is a hobby-project created by students and professionals,<br>" \
                            "aiming to create an environment for training and gaining new skills:<br>" \
                            "* Python coding skills<br>" \
                            "* Using Python libraries (pyqt5, sshtunnel, python-decouple, etc.)<br>" \
                            "* Linux-based Operating Systems<br>" \
                            "* PostreSQL - Install, Configure and work with database<br>" \
                            "* Qt Framework<br>" \
                            "* Git/GitHub<br>" \
                            "* Project Management and Team-work<br>"
                            
        our_story = QLabel()
        our_story.setText(description_text)
        our_story.setFont(QFont(fonts[0], 10))

        our_story_layout.addWidget(our_story_header)
        our_story_layout.addWidget(our_story)
        # our_story_layout.addStretch()
        our_story_layout.addSpacing(0)

        """CONTRIBUTORS LAYOUT"""
        contributors_layout = QVBoxLayout()

        contributors_header = QLabel()
        contributors_header.setText("Contributors")
        contributors_header.setFont(QFont(fonts[0], 14, QFont.Bold))

        contributors_names = QLabel()
        contributors_names.setText("Raya Petkova<br>"
                                 "Aleksandar Karastoyanov<br>"
                                 "Bobby Blagov")
        contributors_names.setFont(QFont(fonts[0], 10))

        contributors = QLabel()
        contributors.setText("Check our GitHub page <a href=\"https://github.com/Stake-And-Rope\">link</a>.")
        contributors.setFont(QFont(fonts[0], 10))
        contributors.setOpenExternalLinks(True)

        contributors_layout.addWidget(contributors_header)
        contributors_layout.addWidget(contributors_names)
        contributors_layout.addStretch()
        
        
        """GITHUB REPO BUTTON LAYOUT"""
        github_repo_layout = QVBoxLayout()
        github_repo_layout.addStretch(0)
        github_repo_layout.addSpacing(0)
        
        github_button = QPushButton()
        github_button.setText("GitHub Repository")
        github_button.setFont(QFont(fonts[0], 10))
        github_button.setStyleSheet("background-color: transparent; \
                                    border: 0px")
        github_button.setIcon(QIcon("../img/github.png"))
        github_button.clicked.connect(lambda: open_github())
        github_button.setFixedWidth(200)
        github_button.setFixedHeight(30)
        
        current_version = QLabel()
        current_version.setText("Current Version: 1.0.0")
        current_version.setFont(QFont(fonts[0], 10))
        
        release_date = QLabel()
        release_date.setText("Release Date: DD-MM-YYYY")
        release_date.setFont(QFont(fonts[0], 10))
        
        github_repo_layout.addWidget(github_button)
        github_repo_layout.addWidget(current_version)
        github_repo_layout.addWidget(release_date)


        """ADDING ALL LAYERS TO MAIN LAYOUT"""
        main_layout.addLayout(our_story_layout)
        main_layout.addLayout(contributors_layout)
        main_layout.addLayout(github_repo_layout)

        self.setLayout(main_layout)
        
        def open_github():
            url=str(r'https://github.com/Stake-And-Rope/market-app')
            webbrowser.open(url)

app = QApplication(sys.argv)
about_window = About()
about_window.show()
app.exec_()