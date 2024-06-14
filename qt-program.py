import sys
import time
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

questions1 = [' נהנה לשרבט תמיד, במחברות שלי יש הרבה תמונות, חיצים עיגולים קווים',
              "זוכר דברים טוב יותר אם אני כותב אותם, גם אם אך אני לא חוזר לעיין בהם.",
              "מנסה לזכור מספר טלפון , על ידי כך שאני מדמיין אותו בראשי.",
              "במהלך בחינה כאשר אני נזכר במידע, אני יכול לראות בדמיון את המחברת עם המידע כתוב בתוכה.",
              "אם אני לא כותב הוראות הגעה למקום מסוים, אני טועה בדרך או מגיע באיחור."]

questions2 = [" לא אוהב להקשיב להוראות או לקרא אותן , אני מעדיף פשוט להתחיל",
              "לומד באופן הטוב ביותר כאשר מראים לי איך לעשות משהו.",
              "זוכר בעיקר דברים שהתנסיתי בהם באופן מעשי.",
              " מעדיף ללמוד מתוך התנסות.",
              "נהנה ללמוד על ידי יצירה ובנייה של דברים"]

questions3 = [" מעדיף לקורא בקול,", " כשאני צריך לזכור מידע, אני משנן זאת שוב ושוב בקול רם וזה עוזר לי לזכור",
              "מבין טוב יותר, אם אני מסביר את החומר לאדם אחר.", " זוכר טוב יותר מה אנשים אומרים ופחות איך הם נראים או מה הם לובשים.",
              "מעדיף לשמוע חדשות ברדיו מאשר לקרא אותם בעיתון."]

answers1 = []
answers2 = []
answers3 = []

import sounddevice as sd
import numpy as np
import wave
import os

def speak(text):
    # Set parameters
    duration = 5  # Recording duration in seconds
    sample_rate = 44100  # Sample rate (samples per second)

    # Record audio
    print("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
    sd.wait()  # Wait for recording to finish
    print("Finished recording.")

    # Save the recorded audio to a WAV file
    wavefile = wave.open("output.wav", "wb")
    wavefile.setnchannels(1)
    wavefile.setsampwidth(2)  # 16-bit PCM
    wavefile.setframerate(sample_rate)
    wavefile.writeframes(audio_data.tobytes())
    wavefile.close()

    from openai import OpenAI
    client = OpenAI(api_key='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')

    audio_file = open("output.wav", "rb")
    transcript = client.audio.transcriptions.create(
      model="whisper-1",
      file=audio_file,
      response_format="text"
    )
    os.remove("output.wav")
    print(transcript)
    print(transcript + f" explain this for {text} learing")
    chat = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": transcript + f" explain this for {text}",
                        }
                    ],
                    model="gpt-3.5-turbo",
                )
    teach = chat.choices[0].message.content.strip()
    print(teach)
    ex = App()
    ex.answer.setVisible(True)
    ex.answer.setText(teach)
    return teach


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Smart Class'
        self.left = 10
        self.top = 10
        self.width = 1000
        self.height = 200
        self.initUI()

    def initUI(self):
        self.place = 0
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        self.label = QLabel("נהנה לשרבט תמיד, במחברות שלי יש הרבה תמונות, חיצים עיגולים קווים", self)
        self.label.resize(self.width, 20)
        self.label.move(0, 20)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 100)
        self.textbox.resize(280, 40)



        # Create a button in the window
        self.button = QPushButton('Next', self)
        self.button.move(20, 160)

        self.button_run = QPushButton('RUN')
        self.button_run.setVisible(False)


        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

        self.answer = QLabel("")
        self.answer.resize(200, 200)
        self.answer.setVisible(False)

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        print(int(textboxValue))

        # QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok,
        #                      QMessageBox.Ok)

        self.textbox.setText("")

        if self.place < 5:
            self.label.setText(questions1[self.place])

            answers1.append(int(textboxValue))

        elif self.place < 10:
            self.label.setText(questions2[self.place - 5])
            answers2.append(int(textboxValue))


        elif self.place < 15:
            self.label.setText(questions3[self.place - 10])
            answers3.append(int(textboxValue))

        else:
            self.textbox.setVisible(False)
            self.button.setVisible(False)

            sums = [sum(answers1), sum(answers2), sum(answers3)]
            # print(sorted(sums)[-1])
            top = sorted(sums)[-1]
            print(sums)
            ltype = ""
            if top == sum(answers1):
                ltype = "חזותי"
            elif top == sum(answers2):
                ltype = "תנועתי"
            else:
                ltype = 'שמיעתי'

            print(ltype)

            self.label.setText(ltype)
            self.button_run.setVisible(True)
            self.button_run.clicked.connect(lambda: speak(ltype))
        self.place += 1

    # def run(ltype):
    #     text = speak(ltype)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = App()
    sys.exit(app.exec_())