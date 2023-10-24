from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QPushButton, QFrame
from PyQt6.QtGui import QImage, QPixmap, QIcon
from PyQt6.QtCore import Qt
import requests
import random
import sys
from hinata import Hinata



def main(window_title, project_name, team_members):

    def get_image_urls(query):
        image_urls = Hinata(query).images()
        return image_urls

    def update_image(query, image_label_widget):
        image_urls = get_image_urls(query)
        url = random.choice(image_urls)
        image = QImage()
        image.loadFromData(requests.get(url).content)
        pixmap = QPixmap(image)
        pixmap = pixmap.scaled(512, 512, Qt.AspectRatioMode.KeepAspectRatio)
        image_label_widget.setPixmap(pixmap)


    app = QApplication([])

    window = QWidget()
    window.setWindowTitle(window_title)
    window.setWindowIcon(QIcon('hinata.png'))

    parent_widget = QVBoxLayout()
    parent_widget.setAlignment(Qt.AlignmentFlag.AlignTop)

    project_name_widget = QLabel(project_name)
    project_name_widget.setStyleSheet("font-weight: bold")

    team_members_widget = QHBoxLayout()
    for i in range(len(team_members[0])):
        row = QVBoxLayout()
        for j in range(len(team_members)):
            row.addWidget(QLabel(team_members[j][i]))
        team_members_widget.addLayout(row)

    query_input_widget = QLineEdit()

    search_button_widget = QPushButton("Generate")

    search_button_widget.clicked.connect(lambda: update_image(query_input_widget.text(), image_label_widget))

    image_label_widget = QLabel()

    parent_widget.addWidget(project_name_widget)
    parent_widget.addWidget(QFrame())
    parent_widget.addLayout(team_members_widget)
    parent_widget.addWidget(QFrame())
    parent_widget.addWidget(query_input_widget)
    parent_widget.addWidget(search_button_widget)
    parent_widget.addWidget(QFrame())
    parent_widget.addWidget(image_label_widget)

    window.setLayout(parent_widget)
    window.show()

    sys.exit(app.exec())



if __name__ == '__main__':
    window_title = "HINATA"
    project_name = "HINATA: Prompt To Image Generator"
    team_members = [
        ["S.No.", "Name", "UID"],
        ["1", "Aditya Raj", "22BCS80016"],
        ["2", "Arpit Suman Aind", "22BCS80021"],
        ["3", "Shreshtha Pal", "22BCS80010"],
        ["4", "Akash Kumar", "22BCS80022"],
        ["5", "Himani", "22BCS80040"]
    ]

    main(window_title, project_name, team_members)
