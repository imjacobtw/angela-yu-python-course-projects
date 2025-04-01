import tkinter

def convert_miles_to_kilometers():
    try:
        miles = float(miles_entry.get())
        kilometers = miles * 1.61
        conversion_result_label.config(text=f"{kilometers:.2f}")
    except ValueError:
        conversion_result_label.config(text="?")

window = tkinter.Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)

miles_entry = tkinter.Entry(width=10)
miles_entry.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_to_label = tkinter.Label(text="is equal to")
is_equal_to_label.grid(row=1, column=0)

conversion_result_label = tkinter.Label(text="0")
conversion_result_label.grid(row=1, column=1)

kilometers_label = tkinter.Label(text="Kilometers")
kilometers_label.grid(row=1, column=2)

calculate_button = tkinter.Button(text="Calculate", command=convert_miles_to_kilometers)
calculate_button.grid(row=2, column=1)

window.mainloop()