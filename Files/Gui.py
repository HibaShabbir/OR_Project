import tkinter
from tkinter import *
import tkinter.messagebox
import customtkinter
from customtkinter import StringVar
import pulp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

class PrintLogger(): # create file like object
    def __init__(self, textbox): # pass reference to text widget
        self.textbox = textbox # keep ref

    def write(self, text):
        self.textbox.insert(tkinter.END, text) # write text to textbox
            # could also scroll to end of textbox here to make sure always visible

    def flush(self): # needed for file like object
        pass


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
text_var = []
entries = []

text_var_ObjEntries = []
text_InequalityEntries = []
ObjEntries = []
text_varB = []
entriesB = []

matrixA = []
matrixB = []

r=0
c=0
class App(customtkinter.CTk):
	def __init__(self):
		super().__init__()
		# configure window
		self.title("Linear Programming 20L-1271")
		self.geometry(f"{1100}x{580}")
		self.textR = StringVar()
		self.textC = StringVar()
		self.textObj = StringVar()
		self.check_var = StringVar()

		# create tabview
		self.tabview = customtkinter.CTkTabview(self, width=1200 , height =900)
		self.tabview.pack(padx=20 ,pady=20)
		self.tabview.add("Program")
		self.tabview.add("Results")
		# self.tabview.add("Tab 3")

		self.textbox_Result = customtkinter.CTkTextbox(self.tabview.tab("Results"), width = 900 , height = 900)
		self.textbox_Result.pack()

		# create instance of file like object
		pl = PrintLogger(self.textbox_Result)
		# replace sys.stdout with our object
		sys.stdout = pl

		self.label_EnterRows = customtkinter.CTkLabel(self.tabview.tab("Program"), text="No.of constraints :",font=('arial', 16, 'bold'))
		self.label_EnterRows.grid(row=0, column=0, padx=20, pady=20)

		self.entry_Rows = customtkinter.CTkEntry(self.tabview.tab("Program"),textvariable= self.textR,font=('arial', 16, 'bold'), width =20)
		self.entry_Rows.grid(row=0, column=1, padx=5, pady=20 , ipadx=20)

		self.label_EnterCols = customtkinter.CTkLabel(self.tabview.tab("Program"),text="No. of variables :" ,font=('arial', 16, 'bold'))
		self.label_EnterCols.grid(row=1, column=0, padx=20, pady=20)

		self.entry_Cols = customtkinter.CTkEntry(self.tabview.tab("Program"), textvariable=self.textC, font=('arial', 16, 'bold'), width =20)
		self.entry_Cols.grid(row=1, column=1, padx=5, pady=20 , ipadx=20 )

		self.combobox = customtkinter.CTkOptionMenu(self.tabview.tab("Program"),values=["Maximize", "Minimize"],
													command=lambda selected : self.optionmenu_callback)
		self.combobox.grid(row=2, column=0, padx=20, pady=20)
		self.combobox.set("Maximize")  # set initial value

		self.buttonEnter = customtkinter.CTkButton(self.tabview.tab("Program"), text="Enter", width=15,command=self.get_mat)
		self.buttonEnter.grid(row=11, column=0)


	def get_mat(self):
		rows = int(self.textR.get())
		cols = int(self.textC.get())
		self.buttonEnter.grid_remove()
		self.label_ObjFunc = customtkinter.CTkLabel(self.tabview.tab("Program"), text="Enter objective function :",font=('arial', 16, 'bold'))
		self.label_ObjFunc.grid(row=3, column=0, padx=20, pady=20)
		count = 2
		for i in range(cols):
			text_var_ObjEntries.append(customtkinter.CTkEntry(self.tabview.tab("Program"), width=8) ) # Create and append to list
			text_var_ObjEntries[-1].grid(row=3, column=count , ipadx=20)  # Place the just created widget
			count += 1  # Increase the count by


		self.label_EnterMatrix = customtkinter.CTkLabel(self.tabview.tab("Program"), text="Enter matrix :",font=('arial', 16, 'bold'))
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
					customtkinter.CTkEntry(self.tabview.tab("Program"), textvariable=text_var[i][j], width=8))
				entries[i][j].grid(row=x2, column=y2 , ipadx=20)
				y2 += 1

			x2 += 1
			y2 = 4

		cols2 = 1
		x2 = 4
		y2 = 4+cols
		for i in range(rows):
			# append an empty list to your two arrays
			# so you can append to those later
			text_varB.append([])
			entriesB.append([])
			for j in range(cols2):
				text_InequalityEntries.append(customtkinter.CTkOptionMenu(self.tabview.tab("Program"),values=["<=", ">=", "="] , width = 8))  # Create and append to list
				text_InequalityEntries[-1].grid(row=x2, column=y2,padx=20)  # Place the just created widget
				text_InequalityEntries[-1].set("<=")  # set initial value
				# append your StringVar and Entry
				y2 += 1
				text_varB[i].append(StringVar())
				entriesB[i].append(
					customtkinter.CTkEntry(self.tabview.tab("Program"), textvariable=text_varB[i][j], width=8))
				entriesB[i][j].grid(row=x2, column=y2, padx=20 , ipadx=20)
			x2 += 1
			y2 = 4+cols
		self.buttonSubmit = customtkinter.CTkButton(self.tabview.tab("Program"), text="Submit", width=15, command=self.submit)
		self.buttonSubmit.grid(row=rows+6, column=1)


	def submit(self):
		self.buttonSubmit.grid_remove()
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
		# print(matrixA)
		# print(matrixB)
		# print(self.textObj.get())
		# print(ObjEntries)
		# print(rows)
		# print(cols)
		# print(self.combobox.get())

		# Create an object of a model
		inequalitySign = []
		colNames=[]
		colN="y"
		colNameCount =1
		for i in range(rows):
			colN = colN + str(colNameCount)
			colNames.append(colN)
			colNameCount += 1
			colN = "y"

			if(text_InequalityEntries[i].get() == "="):
				inequalitySign.append(0)
			elif(text_InequalityEntries[i].get()== ">="):
					inequalitySign.append(1)
			else:
				inequalitySign.append(-1)

		colNames.append("rev")

		varNames = []
		var = "x"
		varCount = 1


		for i in range(cols):
			var = var + str(varCount)
			varNames.append(var)
			varCount += 1
			var = "x"


		numpy_array = np.array(matrixA)
		transpose = numpy_array.T

		transpose_matrixA = transpose.tolist()

		for i in range(cols):
			transpose_matrixA[i].append(ObjEntries[i])

		# Create DataFrame object from list of tuples
		data_frame = pd.DataFrame(transpose_matrixA,
								  columns=colNames,
								  index=varNames)

		if(self.combobox.get()=="Maximize"):
			prob = pulp.LpProblem("ProbSimplex", pulp.LpMaximize)

			listVar = [pulp.LpVariable(varName, 0) for varName in varNames]

			# Objective Function
			prob += pulp.lpSum([data_frame.rev[i] * listVar[i] for i in range(len(data_frame))])

			# Constraints:
			for i in range(len(matrixB)):

				if(inequalitySign[i] == -1):
					prob += pulp.lpSum([data_frame.iloc[j, i] * listVar[j]
										   for j in range(len(listVar))]) <= int(matrixB[i])
				elif(inequalitySign[i] == 1):
					prob += pulp.lpSum([data_frame.iloc[j, i] * listVar[j]
										for j in range(len(listVar))]) >= int(matrixB[i])
				else:
					prob += pulp.lpSum([data_frame.iloc[j, i] * listVar[j]
										for j in range(len(listVar))]) == int(matrixB[i])

			prob.solve()
			print("Status: ",  pulp.LpStatus[prob.status])

			for v in prob.variables():
				print(v.name + "=" + str(v.varValue) + "\tReduced cost = " + str(v.dj))
			print("objective function = " + str(pulp.value(prob.objective)))
			print("Senstivity Analysis\n Constraints\t\t      ShadowPrice \t    Slack")
			for name, c in prob.constraints.items():
				print(name, c, "\t  ", c.pi, "\t\t", c.slack)
		else:
			prob = pulp.LpProblem("ProbSimplex", pulp.LpMinimize)

			listVar = [pulp.LpVariable(varName, 0) for varName in varNames]

			# Objective Function
			prob += pulp.lpSum([data_frame.rev[i] * listVar[i] for i in range(len(data_frame))])

			# Constraints:
			for i in range(len(matrixB)):
				prob += pulp.lpSum([data_frame.iloc[j, i] * listVar[j]
									for j in range(len(listVar))]) <= int(matrixB[i])

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