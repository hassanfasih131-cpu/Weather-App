import sys
import requests
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
if __name__=="__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp() #weather app object
    weather_app.show() #showing weather app
    sys.exit(app.exec()) #lets the app stay until its closed