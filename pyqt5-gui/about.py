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
        self.setWindowTitle("About Us")
        self.setGeometry(650, 300, 600, 400)

        main_layout = QVBoxLayout()

        """Init the our story layout"""
        our_story_layout = QVBoxLayout()
        our_story_header = QLabel()
        our_story_header.setText("<b><font size='4'>Our Story</font></b>")

        description_text = "<font size='4'>Since 2013, we've been committed to providing high-quality organic food.<br>" \
                            "We link local farmers and consumers, offering the best from the field to your table.<br>" \
                            "We stand for a healthier lifestyle, environmental respect, and support for the local economy.<br>" \
                            "With us, you'll enjoy the freshest, organically grown food for a healthier you.</font>"
        our_story = QLabel()
        our_story.setText(description_text)

        our_story_layout.addWidget(our_story_header)
        our_story_layout.addWidget(our_story)

        our_story_layout.addStretch()

        """Contact Us Layout"""

        contact_us_layout = QVBoxLayout()
        contact_us = QLabel()
        contact_us.setText("<b><font size='4'>Contact Us</font></b><br>"
                           "123-456-7890<br>"
                           "stake_robe@example.com")

        contact_us_layout.addWidget(contact_us)
        contact_us_layout.addStretch()

        """Contributors Layout"""

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


        """Adding all layers together"""
        main_layout.addLayout(our_story_layout)
        main_layout.addLayout(contact_us_layout)
        main_layout.addLayout(contributors_layout)

        self.setLayout(main_layout)


app = QApplication(sys.argv)
about_window = About()
about_window.show()
app.exec_()