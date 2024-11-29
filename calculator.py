from tkinter import *

                                                                                                           # globally declare the expression variable 
expression = ""

                                                                                                    # Function to update expression in the text entry box
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

                                                                                                              # Function to evaluate the final expression
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""

                                                                                                  # Function to clear the contents of the text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

                                                                                                                                   # Driver code
if __name__ == "__main__":
                                                                                                                                  # Create a GUI window
    gui = Tk()
    gui.configure(background="light blue")
    gui.title("Calculator")
    gui.geometry("350x450")
    
                                                                                                              # Set up a StringVar to hold the equation
    equation = StringVar()
    
                                                                                                              # Create the text entry box for the display
    expression_field = Entry(gui, textvariable=equation, font=("Arial", 20), bg="white", fg="black", borderwidth=5, relief="groove")
    expression_field.grid(columnspan=4, ipadx=8, ipady=10, pady=10)

                                                                                                                               # Common button style
    button_style = {
        "fg": "white",
        "bg": "dark blue",
        "font": ("Arial", 14),
        "height": 2,
        "width": 5,
        "relief": "raised",
        "borderwidth": 3,
    }

                                                                                                            # Create buttons for digits and operations
    buttons = [
        ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
        ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
        ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3),
        ('C', 5, 0), ('0', 5, 1), ('.', 5, 2), ('/', 5, 3),
        ('=', 6, 0, 4)
    ]
    
    for text, row, col, *span in buttons:
        Button(gui, text=text, command=(clear if text == 'C' else equalpress if text == '=' else lambda t=text: press(t)), **button_style)\
            .grid(row=row, column=col, columnspan=(span[0] if span else 1), sticky="nsew", padx=5, pady=5)

                                                                                                # Adjust the weight of rows and columns for proper spacing
    for i in range(7):
        gui.rowconfigure(i, weight=1)
    for i in range(4):
        gui.columnconfigure(i, weight=1)

                                                                                                                                           # Start the GUI
    gui.mainloop()
