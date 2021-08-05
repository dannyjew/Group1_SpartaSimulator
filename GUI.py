from tkinter import *
from SimulationClass import *
from main_func import main


def click():
    sim = Simulation()
    simulation = sim_length.get()  # this collects the text from the text entry box
    total = open_centres.get()
    output.delete(0.0, END)
    try:
        sim.total_centres = int(total)
        sim.simulation_length = int(simulation)
        if sim.total_centres < 0 or sim.simulation_length < 0:
            raise ValueError

        result = main(sim)

    except ValueError:
        result = "Invalid input, please enter a positive integer"
    output.insert(END, result)


# exit function
def close_window():
    window.destroy()
    exit()


window = Tk()
window.title("Sparta Simulator")
window.configure(background="#2D2A2B")

# # photo
# photo1 = PhotoImage(file="sparta.gif")
# Label(window, image=photo1, bg="black") .grid(row=0, column=0, sticky=E)

# create label
Label(window, text="                *** Welcome to this Sparta Simulation ***\n", bg="#2D2A2B", fg="#E33661", font="none 12 bold") .grid(row=1, column=0, sticky=W)
Label(window, text='How long do you want the simulation to last (in months)?: ', bg='#2D2A2B', fg="#E33661", font="none 12 bold") .grid(row=2, column=0, sticky=W)

# create text entry box
sim_length = Entry(window, width=20, bg="#AEAEAE")
sim_length.grid(row=3, column=0, sticky=W)

Label(window, text="\nHow many open centres do you want to start with?: ", bg="#2D2A2B", fg="#E33661", font="none 12 bold") .grid(row=4, column=0, sticky=W)

open_centres = Entry(window, width=20, bg="#AEAEAE")
open_centres.grid(row=5, column=0, sticky=W)

Label(window, text="", bg="#2D2A2B", fg="#E33661", font="none 12 bold") .grid(row=6, column=0, sticky=W)

# add submit button
Button(window, text="SUBMIT", width=6, command=click) .grid(row=7, column=0, sticky=W)

# create another label
Label(window, text="\n\nSimulation Result: ", bg="#2D2A2B", fg="#E33661", font="none 12 bold") .grid(row=8, column=0, sticky=W)

# create a text box
output = Text(window, width=75, height=20, wrap=WORD, background="#AEAEAE")
output.grid(row=9, column=0, columnspan=2, sticky=W)


# exit label
Label(window, text="\nClick to exit:", bg="#2D2A2B", fg="#E33661", font="none 12 bold") .grid(row=10, column=0, sticky=W)

# exit button
Button(window, text="Exit", width=12, command=close_window) .grid(row=11, column=0, sticky=W)

window.mainloop()
