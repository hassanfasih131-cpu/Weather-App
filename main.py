import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
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
        pass
if __name__=="__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp() #weather app object
    weather_app.show() #showing weather app
    sys.exit(app.exec()) #lets the app stay until its closed