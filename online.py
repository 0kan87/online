import sys
import time
import random
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, 
                           QVBoxLayout, QWidget, QSpinBox, QHBoxLayout)
from PyQt5.QtCore import QTimer, Qt, QThread, pyqtSignal
import pyautogui

# Güvenlik ayarı
pyautogui.FAILSAFE = True

class ActivityWorker(QThread):
    status_update = pyqtSignal(str)
    countdown_update = pyqtSignal(str)
    
    def __init__(self, min_interval, max_interval):
        super().__init__()
        self.is_running = True
        self.min_interval = min_interval
        self.max_interval = max_interval
        self.activity_count = 0

    def simulate_activity(self):
        try:
            # Mevcut fare konumunu kaydet
            current_x, current_y = pyautogui.position()
            
            # Mini fare hareketi
            pyautogui.moveRel(10, 0, duration=0.2)
            pyautogui.moveRel(-10, 0, duration=0.2)
            
            # Scroll hareketi
            pyautogui.scroll(10)
            time.sleep(0.1)
            pyautogui.scroll(-10)
            
            # Shift tuşuna basma
            pyautogui.press('shift')
            
            # Fareyi orijinal konumuna getir
            pyautogui.moveTo(current_x, current_y, duration=0.2)
            
            return True
        except pyautogui.FailSafeException:
            self.status_update.emit("Program durduruldu - fare köşeye çekildi")
            return False

    def run(self):
        while self.is_running:
            self.activity_count += 1
            current_time = datetime.now().strftime("%H:%M:%S")
            self.status_update.emit(f"Aktivite #{self.activity_count} - Saat: {current_time}")
            
            if not self.simulate_activity():
                break
                
            wait_time = random.randint(self.min_interval, self.max_interval)
            total_seconds = wait_time
            
            while total_seconds > 0 and self.is_running:
                mins, secs = divmod(total_seconds, 60)
                self.countdown_update.emit(f"{mins:02d}:{secs:02d}")
                time.sleep(1)
                total_seconds -= 1

    def stop(self):
        self.is_running = False

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Çevrimiçi Durumu Koruyucu")
        self.setFixedSize(400, 300)
        
        # Ana widget ve layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()
        main_widget.setLayout(layout)
        
        # Durum etiketi
        self.status_label = QLabel("Program hazır...")
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)
        
        # Geri sayım etiketi
        self.countdown_label = QLabel("--:--")
        self.countdown_label.setAlignment(Qt.AlignCenter)
        self.countdown_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(self.countdown_label)
        
        # Aralık ayarları
        interval_layout = QHBoxLayout()
        interval_layout.addWidget(QLabel("Minimum süre (saniye):"))
        self.min_spin = QSpinBox()
        self.min_spin.setRange(30, 300)
        self.min_spin.setValue(60)
        interval_layout.addWidget(self.min_spin)
        
        interval_layout.addWidget(QLabel("Maximum süre (saniye):"))
        self.max_spin = QSpinBox()
        self.max_spin.setRange(30, 300)
        self.max_spin.setValue(120)
        interval_layout.addWidget(self.max_spin)
        layout.addLayout(interval_layout)
        
        # Başlat/Durdur düğmesi
        self.toggle_button = QPushButton("Başlat")
        self.toggle_button.clicked.connect(self.toggle_activity)
        layout.addWidget(self.toggle_button)
        
        # Desteklenen uygulamalar listesi
        supported_apps = """Desteklenen Uygulamalar:
- Skype
- Microsoft Teams
- Slack
- WhatsApp Web
- Telegram Web
- Discord
- Google Meet
- Zoom (web)"""
        info_label = QLabel(supported_apps)
        info_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(info_label)
        
        self.worker = None

    def toggle_activity(self):
        if self.worker is None or not self.worker.is_running:
            # Programı başlat
            self.toggle_button.setText("Durdur")
            self.min_spin.setEnabled(False)
            self.max_spin.setEnabled(False)
            
            self.worker = ActivityWorker(self.min_spin.value(), self.max_spin.value())
            self.worker.status_update.connect(self.update_status)
            self.worker.countdown_update.connect(self.update_countdown)
            self.worker.start()
        else:
            # Programı durdur
            self.stop_activity()

    def stop_activity(self):
        if self.worker:
            self.worker.stop()
            self.worker = None
        self.toggle_button.setText("Başlat")
        self.min_spin.setEnabled(True)
        self.max_spin.setEnabled(True)
        self.status_label.setText("Program durduruldu")
        self.countdown_label.setText("--:--")

    def update_status(self, message):
        self.status_label.setText(message)

    def update_countdown(self, time_str):
        self.countdown_label.setText(time_str)

    def closeEvent(self, event):
        self.stop_activity()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
