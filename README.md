# Micropython-traffic-light

<img width="1920" height="1030" alt="Wokwi - Online ESP32, STM32, Arduino Simulator - Google Chrome 06-12-2025 14_47_11" src="https://github.com/user-attachments/assets/8df91500-7ed4-443a-81d6-8c70252854a8" />


# 🚦 MicroPython Traffic Light System with OLED Display

A simple yet realistic **traffic light simulation** built using **MicroPython** on **ESP32/ESP8266** with a **128×64 SSD1306 OLED display**.

Perfect for beginners learning MicroPython, IoT, GPIO control, and I2C communication!

## ✨ Features
- Full traffic light sequence: **Red → Green → Yellow → Red**
- Real-time status displayed on **SSD1306 OLED**
- Clean console output for debugging
- Proper delay timing (5s Red/Green, 2s Yellow)
- Well-commented and beginner-friendly code

## 🖼️ Demo (Real Hardware)
![Traffic Light in Action](demo.jpg)  
*(Add your own photo here after uploading to the repo)*

## ⚙️ Hardware Required
- ESP32 or ESP8266 (any variant)
- 3 LEDs (Red, Yellow, Green) with 220–330Ω resistors
- SSD1306 OLED Display (128×64, I2C)
- Jumper wires & breadboard

## 📍 Default Pin Configuration (ESP32)
| Component       | GPIO Pin |
|-----------------|----------|
| Red LED         | GPIO 5   |
| Yellow LED      | GPIO 18  |
| Green LED       | GPIO 19  |
| OLED SDA        | GPIO 21  |
| OLED SCL        | GPIO 22  |

> You can easily change pins in `main.py`

## 🚀 How to Run
1. Flash MicroPython firmware on your ESP32/ESP8266
2. Copy these files to the board:
   - `boot.py`
   - `main.py`
   - `ssd1306.py`
3. Reset the device → Traffic light starts automatically!


# Connections

<img width="1920" height="1030" alt="Wokwi - Online ESP32, STM32, Arduino Simulator - Google Chrome 06-12-2025 14_48_08" src="https://github.com/user-attachments/assets/e752438c-baf0-4b52-afcf-675c8066fc4e" />


## 📂 Project Files
- `main.py` → Main logic and display control
- `ssd1306.py` → OLED driver (official MicroPython)
- `boot.py` → Startup script

## 🔧 Future Improvements (Contributions Welcome!)
- [ ] Add pedestrian crossing button
- [ ] Countdown timer on OLED
- [ ] Web dashboard control via Wi-Fi
- [ ] Sound buzzer for accessibility

## 👨‍💻 Author
**Ayush Rajak**
- Working on IoT, Embedded Systems & MicroPython

## 📄 License
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

⭐ **Star this repo if you found it helpful!**  
Feel free to fork and improve it! 🚀

#IoT #MicroPython #ESP32 #EmbeddedSystems #Electronics #DIY
