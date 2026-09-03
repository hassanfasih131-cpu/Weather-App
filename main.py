import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label=QLabel("Enter the city name: ",self)
        self.city_input=QLineEdit(self)
        self.get_weather_button=QPushButton("Get Weather",self)
        self.temperature_label=QLabel("70 degrees F ",self)
        self.emoji_label=QLabel("*",self)
        self.description_label=QLabel("It is sunny: ",self)
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle("Weather App")
        #brings all the info to its proper positions
        vbox=QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)
        #brings all the info to the middle
        self.city_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.city_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #setting the object name
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        #sets style
        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: 'Calibri'; 
            }
            QLabel#city_label { 
                font-size: 40px;
                font-style: italic;
                
            }
        """)


if __name__=="__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp() #weather app object
    weather_app.show() #showing weather app
    sys.exit(app.exec()) #lets the app stay until its closed