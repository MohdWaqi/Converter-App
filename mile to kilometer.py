import tkinter
window = tkinter.Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)
label1 = tkinter.Label(text="is equal to")
label1.grid(column=0, row=1)

input_text = tkinter.Entry(width=10)
input_text.grid(column=1, row=0)

label2 = tkinter.Label(text=0)
label2.grid(column=1, row=1)


def click():
    result =round(float(input_text.get()) * 1.60934)
    label2.config(text=result)


button = tkinter.Button(text="Calculate", command=click)
button.grid(column=1, row=2)

label3 = tkinter.Label(text="Miles")
label3.grid(column=2, row=0)

label4 = tkinter.Label(text="Km")
label4.grid(column=2, row=1)
window.mainloop()