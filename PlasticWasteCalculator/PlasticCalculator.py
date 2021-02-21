import tkinter as tk

x = 0
label = 'According to the US National Ocean Service, it is estimated that 8 million metric tons of plastic entered the ' \
        'ocean in 2010 (507.4 pounds per second).  \n Unfortunately, this problem is only continuing to grow. \n ' \
        'Unlike other kinds of waste, plastic does not decompose, which means that plastic sticks around ' \
        'indefinitely, wreaking marine ecosystems. \n As the plastic is tossed around, much of it breaks into tiny ' \
        'pieces, called microplastics. \n These microplastics are not only harmful to marine life, but they can cause ' \
        'harmful pollutants like pesticides, dyes, and flame retardants to be released into the ocean. \n Not only ' \
        'can microplastics transport chemical pollutants into the ocean, but they can also serve as a vector for ' \
        'transportation of pollutants to soil. \n This reminded me of the daphnia ' \
        'toxicology experiment where we saw that the presence of toxins visibly stressed out the organism.'
title = 'How much plastic has entered the ocean since this app has been opened?'


def add():
    global x
    x += 51
    round(x, 2)
    clock_label['text'] = str(round(x, 2)) + ' pounds'
    window.after(100, add)


window = tk.Tk()
window.title('Plastic Waste Calculator')
window.geometry("5000x5000")

titles = tk.Label(window, font='areil 40', bg='white', fg='blue', text=title)
titles.grid(row=0, column=0)
titles.pack()

clock_label = tk.Label(window, font='areil 80', bg='white', fg='blue', text=x)
clock_label.pack()
add()

clock = tk.Label(window, font='areil 18', bg='white', fg='blue', text=label)
clock.pack()
window.mainloop()
