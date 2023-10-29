import tkinter
from tkinter import *
import tkinter.messagebox
import customtkinter
from customtkinter import StringVar
import pulp
import numpy as np
import pandas as pd
import sys


class PrintLogger():  # create file like object
    def __init__(self, textbox):  # pass reference to text widget
        self.textbox = textbox  # keep ref

    def write(self, text):
        self.textbox.insert(tkinter.END, text)  # write text to textbox
        # could also scroll to end of textbox here to make sure always visible

    def flush(self):  # needed for file like object
        pass


customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("green")
text_var = []
entries = []

text_var_ObjEntries = []
text_InequalityEntries = []
ObjEntries = []
text_varB = []
entriesB = []

matrixA = []
matrixB = []

r = 0
c = 0


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # configure window
        self.title("20L-1319_OR_Project")
        self.geometry(f"{1100}x{580}")
        self.textR = StringVar()
        self.textC = StringVar()
        self.textObj = StringVar()
        self.check_var = StringVar()

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=1200, height=900)
        self.tabview.pack(padx=20, pady=20)
        self.tabview.add("Question")
        self.tabview.add("Report")
        # self.tabview.add("Tab 3")

        self.textbox_Result = customtkinter.CTkTextbox(self.tabview.tab("Report"), width=900, height=900)
        self.textbox_Result.pack()

        # create instance of file like object
        pl = PrintLogger(self.textbox_Result)
        # replace sys.stdout with our object
        sys.stdout = pl

        self.label_EnterRows = customtkinter.CTkLabel(self.tabview.tab("Question"), text="Number of constraints :",
                                                      font=('helvetica', 16, 'bold'))
        self.label_EnterRows.grid(row=0, column=0, padx=20, pady=20)

        self.entry_Rows = customtkinter.CTkEntry(self.tabview.tab("Question"), textvariable=self.textR,
                                                 font=('helvetica', 16, 'bold'), width=20)
        self.entry_Rows.grid(row=0, column=1, padx=5, pady=20, ipadx=20)

        self.label_EnterCols = customtkinter.CTkLabel(self.tabview.tab("Question"), text="Number of variables :",
                                                      font=('helvetica', 16, 'bold'))
        self.label_EnterCols.grid(row=1, column=0, padx=20, pady=20)

        self.entry_Cols = customtkinter.CTkEntry(self.tabview.tab("Question"), textvariable=self.textC,
                                                 font=('helvetica', 16, 'bold'), width=20)
        self.entry_Cols.grid(row=1, column=1, padx=5, pady=20, ipadx=20)

        self.combobox = customtkinter.CTkOptionMenu(self.tabview.tab("Question"), values=["Maximize", "Minimize"],
                                                    command=lambda selected: self.optionmenu_callback)
        self.combobox.grid(row=2, column=0, padx=20, pady=20)
        self.combobox.set("Maximize")  # set initial value

        self.enter_btn = customtkinter.CTkButton(self.tabview.tab("Question"), text="Enter", width=15,
                                                   command=self.get_mat)
        self.enter_btn.grid(row=11, column=0)

    def get_mat(self):
        rows = int(self.textR.get())
        cols = int(self.textC.get())
        self.enter_btn.grid_remove()
        self.label_ObjFunc = customtkinter.CTkLabel(self.tabview.tab("Question"), text="Enter objective function :",
                                                    font=('helvetica', 16, 'bold'))
        self.label_ObjFunc.grid(row=3, column=0, padx=20, pady=20)
        count = 2
        for i in range(cols):
            text_var_ObjEntries.append(
                customtkinter.CTkEntry(self.tabview.tab("Question"), width=8))  # Create and append to list
            text_var_ObjEntries[-1].grid(row=3, column=count, ipadx=20)  # Place the just created widget
            count += 1  # Increase the count by

        self.label_EnterMatrix = customtkinter.CTkLabel(self.tabview.tab("Question"), text="Enter constraints :",
                                                        font=('helvetica', 16, 'bold'))
        self.label_EnterMatrix.grid(row=4, column=0, padx=20)
        x2 = 4
        y2 = 4
        for i in range(rows):
            # append an empty list to your two arrays
            # so you can append to those later
            text_var.append([])
            entries.append([])
            for j in range(cols):
                # append your StringVar and Entry
                text_var[i].append(StringVar())
                entries[i].append(
                    customtkinter.CTkEntry(self.tabview.tab("Question"), textvariable=text_var[i][j], width=8))
                entries[i][j].grid(row=x2, column=y2, ipadx=20)
                y2 += 1

            x2 += 1
            y2 = 4

        cols2 = 1
        x2 = 4
        y2 = 4 + cols
        for i in range(rows):
            text_varB.append([])
            entriesB.append([])
            for j in range(cols2):
                text_InequalityEntries.append(
                    customtkinter.CTkOptionMenu(self.tabview.tab("Question"), values=["<=", ">=", "="],
                                                width=8))  # Create and append to list
                text_InequalityEntries[-1].grid(row=x2, column=y2, padx=20)  # Place the just created widget
                text_InequalityEntries[-1].set("<=")
                y2 += 1
                text_varB[i].append(StringVar())
                entriesB[i].append(
                    customtkinter.CTkEntry(self.tabview.tab("Question"), textvariable=text_varB[i][j], width=8))
                entriesB[i][j].grid(row=x2, column=y2, padx=20, ipadx=20)
            x2 += 1
            y2 = 4 + cols
        self.submit_btn = customtkinter.CTkButton(self.tabview.tab("Question"), text="Submit", width=15,
                                                    command=self.submit)
        self.submit_btn.grid(row=rows + 6, column=1)

    def submit(self):
        self.submit_btn.grid_remove()
        rows = int(self.textR.get())
        cols = int(self.textC.get())

        for i in range(cols):
            ObjEntries.append(float(text_var_ObjEntries[i].get()))

        for i in range(rows):
            matrixA.append([])
            for j in range(cols):
                matrixA[i].append(float(text_var[i][j].get()))

        cols2 = 1
        for i in range(rows):
            matrixB.append(float(text_varB[i][0].get()))
        sign = []
        column_names = []
        colN = "y"
        column_names_count = 1
        for i in range(rows):
            colN = colN + str(column_names_count)
            column_names.append(colN)
            column_names_count += 1
            colN = "y"

            if text_InequalityEntries[i].get() == "=":
                sign.append(0)
            elif text_InequalityEntries[i].get() == ">=":
                sign.append(1)
            else:
                sign.append(-1)

        column_names.append("rev")

        var_names = []
        var = "x"
        var_count = 1

        for i in range(cols):
            var = var + str(var_count)
            var_names.append(var)
            var_count += 1
            var = "x"

        numpy_array = np.array(matrixA)
        transpose = numpy_array.T

        transpose_matrix_a = transpose.tolist()

        for i in range(cols):
            transpose_matrix_a[i].append(ObjEntries[i])

        # Create DataFrame object from list of tuples
        data_frame = pd.DataFrame(transpose_matrix_a,
                                  columns=column_names,
                                  index=var_names)

        if self.combobox.get() == "Maximize":
            prob = pulp.LpProblem("ProbSimplex", pulp.LpMaximize)

            var_list = [pulp.LpVariable(var_name, 0) for var_name in var_names]

            # Objective Function
            prob += pulp.lpSum([data_frame.rev[i] * var_list[i] for i in range(len(data_frame))])

            # Constraints:
            for i in range(len(matrixB)):

                if sign[i] == -1:
                    prob += pulp.lpSum([data_frame.iloc[j, i] * var_list[j]
                                        for j in range(len(var_list))]) <= int(matrixB[i])
                elif sign[i] == 1:
                    prob += pulp.lpSum([data_frame.iloc[j, i] * var_list[j]
                                        for j in range(len(var_list))]) >= int(matrixB[i])
                else:
                    prob += pulp.lpSum([data_frame.iloc[j, i] * var_list[j]
                                        for j in range(len(var_list))]) == int(matrixB[i])

            prob.solve()
            print("Status: ", pulp.LpStatus[prob.status])

            for v in prob.variables():
                print(v.name + "=" + str(v.varValue) + "\tReduced cost = " + str(v.dj))
            print("objective function = " + str(pulp.value(prob.objective)))
            print("Senstivity Analysis\n Constraints\t\t      ShadowPrice \t    Slack")
            for name, c in prob.constraints.items():
                print(name, c, "\t  ", c.pi, "\t\t", c.slack)
        else:
            prob = pulp.LpProblem("ProbSimplex", pulp.LpMinimize)

            var_list = [pulp.LpVariable(varName, 0) for varName in var_names]

            # Objective Function
            prob += pulp.lpSum([data_frame.rev[i] * var_list[i] for i in range(len(data_frame))])

            # Constraints:
            for i in range(len(matrixB)):
                prob += pulp.lpSum([data_frame.iloc[j, i] * var_list[j]
                                    for j in range(len(var_list))]) <= int(matrixB[i])

            prob.solve()
            print("Status: ", pulp.LpStatus[prob.status])

            for v in prob.variables():
                print(v.name + "=" + str(v.varValue) + "\tReduced cost = " + str(v.dj))
            print("objective function = " + str(pulp.value(prob.objective)))
            print("Senstivity Analysis\n Constraints\t\t      ShadowPrice \t    Slack")
            for name, c in prob.constraints.items():
                print(name, "1", c, "\t  ", c.pi, "\t\t", c.slack)


def optionmenu_callback(self, choice):
    print("optionmenu dropdown clicked:", choice)


if __name__ == "__main__":
    app = App()
    app.mainloop()
