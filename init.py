import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('CalculatorGPT')
        self.geometry('300x300')

        self.result = tk.Label(self, text='', font=('Arial', 32))
        self.result.pack()

        button_frame = tk.Frame(self)
        button_frame.pack()

        buttons = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '0', '.', '=',
            "+", "-", "*",
            "/", 'C', "x²",
            "x³", "MD", "D"
        ]

        for button_text in buttons:
            button = tk.Button(
                button_frame,
                text=button_text,
                font=('Arial', 24),
                width=2,
                height=1,
                command=lambda text=button_text: self.append(text)
            )
            button.pack(side='left')

    def append(self, value):
        if value == 'C':
            self.clearResult()
        elif value == '=':
            self.calculate()    
        elif value == "D":
            print("Its D!")
        else:
            self.result.config(text=self.result.cget('text') + value)

    def clearResult(self):
        self.result.config(text='')      

    def calculate(self):
        try:
            result = eval(self.result.cget('text'))
            self.result.config(text=result)
        except (SyntaxError, ZeroDivisionError):
            self.result.config(text='Error')

if __name__ == '__main__':
    Calculator().mainloop()
