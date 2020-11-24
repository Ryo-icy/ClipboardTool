# 標準ライブラリ
import configparser
import tkinter as tk

# サードパーティ製ライブラリ
import pyperclip

# アプリケーションクラス
class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        master.geometry('388x310')
        master.title('Password Tools')
        self.Username, self.Password, self.Color = Config().Get_Data()
        self.create_button(master)
    
    def create_button(self, master):
        for i in range(0, 6):
            button = tk.Button(text=self.Username[i], width=50, height=2, bg=self.Color[i])
            button.bind('<Button-1>', self.click_button)
            button.place(x=13, y=5+i*50)
    
    def click_button(self, event):
        index = self.Username.index(event.widget['text'])
        pyperclip.copy(self.Password[index])

class Config():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(r'.\UserSetting\config.ini', encoding='UTF-8')
    
    def Get_Data(self):
        Username = []
        Password = []
        Color = []
        for i in range(1, 7):
            Username.append(self.config.get('P-{}'.format(i), 'Username'))
            Password.append(self.config.get('P-{}'.format(i), 'Password'))
            Color.append(self.config.get('P-{}'.format(i), 'Color'))
        return Username, Password, Color

def main():
    App = Application(master=tk.Tk())
    App.mainloop()

if __name__ == '__main__':
    main()