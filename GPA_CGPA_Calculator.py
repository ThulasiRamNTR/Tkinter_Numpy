import tkinter as tk
from tkinter.ttk import Notebook #For creating tabs
import numpy as np
import tkinter.messagebox as msg #For creting messageboxes




class Calculator(tk.Tk):

    def __init__(self):
        super().__init__()

        #Setting up the window
        self.title("Calculator")
        self.geometry("600x600")
        self.colour_schemes = [{"bg":"lightgrey", "fg":"black"}, {"bg":"grey", "fg":"white"}]
        self.semesters = [(1, "Semester 1"), (2, "Semester 2"), (3, "Semester 3"), (4, "Semester 4"), (5, "Semester 5"), (6, "Semester 6"), (7, "Semester 7"), (8, "Semester 8")]
        self.grade_credit_value = {"S" : 10, "A": 9, "B" : 8, "C": 7, "D": 6, "E": 5, "U": 0, "s" : 10, "a": 9, "b" : 8, "c": 7, "d": 6, "e": 5, "u": 0}
        self.regulation_departments_semester = {2008:{},

         2013:{"CSE":{1:[["Technical English - 1", 4], ["Mathematics -1", 4], ["Engineering Physics", 3], ["Engineering Chemistry", 3], ["Computer Programming", 3], ["Engineering Graphics", 4], ["Computer Practices Laboratory", 2], ["Engineering Practices Laboratory", 2], ["Physics and Chemistry Laboratory", 1]],
         2:[["Technical English - 2", 4], ["Mathematics - 2", 4], ["Engineering Physics - 2", 3], ["Enginnering Chemistry - 2", 3], ["Digital Principles and System Design", 3], ["Programming and Data Structures - 1", 3], ["Physics and Chemistry Laboratory - 2", 1], ["Digital Laboratory", 2], ["Programming and Data Structures Laboratory - 1", 2]],
         3:[["Transforms and Partial Differential Equations", 4], ["Programming and Data Structures - 2",3],["Database Management Systems", 3], ["Computer Architecture", 3], ["Analog and Digital Communication", 3],["Environmental Science and Engineering", 3], ["Programming and Data Structures Laboratory - 2", 2], ["Database Management Systems Laboratory", 2]],
         4:[["Probablity and Queuing Theory", 4], ["Computer Networks", 3], ["Operating Systems", 3], ["Design and Analysis of Algorithms", 3], ["Microprocessor and Microcontroller", 3], ["Software Engineering", 3], ["Networks Laboratory", 2], ["Microprocessor and Microcontroller Laboratory", 2], ["Operating Systems Laboratory", 2]],
         5:[["Discrete Mathematics", 4], ["Internet Programming", 4], ["Object Oriented Analysis and Design", 3], ["Theory of Computation", 3], ["Computer Graphics", 3], ["Case Tools Laboratory", 2], ["Internet Programming Laboratory", 2], ["Computer Graphics Laboratory", 2]],
         6:[["Distributed Systems", 3], ["Mobile COmputing", 3], ["Compiler Design", 3], ["Digital Signal Processing", 4], ["Artificial Intelligence", 3], ["Elective - 1", 3], ["Mobile Application Development Laboratory", 2], ["Compiler Laboratory", 2], ["Communication and Soft Skills - Laboratory Based", 2]],
         7:[["Cryptography and Network Security", 3], ["Graph Theory and Applications", 3], ["Grid and Cloud Computing", 3], ["Resource Management Techniques", 3], ["Elective - 2", 3], ["Elective - 3", 3], ["Security Laboratory", 2], ["Grid and Cloud Computing Laboratory", 2]],
         8:[["Multi - Core Architectures and Programming", 3], ["Elective - 4", 3], ["Elective - 5", 3], ["Project Work", 6]],
                    },
                "IT":{},
                "EEE":{},
                "ECE":{},
                "EIE":{}
         },

         2018:{}}


        #Creating the widgets of the window
        self.calculator_notebook = Notebook(self) #Notebook holding the tabs

        self.gpa_calculator_tab = tk.Frame(self.calculator_notebook) #Tab for calculating gpa
        self.cgpa_calculator_tab = tk.Frame(self.calculator_notebook) #Tab for calculating cgpa


        self.regulation = tk.IntVar()
        self.regulation.set(2013)
        self.department = tk.StringVar()
        self.department.set("CSE")
        self.semester = tk.IntVar()
        self.semester.set(1)



        #packing the widgets
        self.calculator_notebook.add(self.gpa_calculator_tab, text = "GPA") #Adding the gpa tab to the notebook
        self.calculator_notebook.add(self.cgpa_calculator_tab, text = "CGPA") #Adding the cgpa tab to the notebook

        self.calculator_notebook.pack(fill = tk.BOTH, expand = 1)


        self.initialize_gpa_calculator_tab() #Initializing the gpa_calculator_tab
        self.initialize_cgpa_calculator_tab() #Initializing the cgpa_calculator_tab






    def initialize_gpa_calculator_tab(self):
        #Initializing the gpa_calculator_tab

        self.gpa_regulation_frame = tk.Frame(self.gpa_calculator_tab) #Frame for gpa regulation
        self.gpa_department_frame = tk.Frame(self.gpa_calculator_tab) #Frame for gpa department
        self.gpa_semester_frame = tk.Frame(self.gpa_calculator_tab) #Frame for gpa semester
        self.gpa_subjects_frame = tk.Frame(self.gpa_calculator_tab) #Frame for gpa subjects
        self.display_frame = tk.Frame(self.gpa_subjects_frame) #Frame for displaying the subjects and grade input bar

        """Regulation Widgets """
        self.gpa_regulation_label = tk.Label(self.gpa_regulation_frame, text = "Select your Syllabus Regulation", bg = "grey", fg ="white")
        self.gpa_regulation_2008 = tk.Radiobutton(self.gpa_regulation_frame, text = "Regulation 2008", variable = self.regulation, value = 2008, indicatoron = 0)
        self.gpa_regulation_2013 = tk.Radiobutton(self.gpa_regulation_frame, text = "Regulation 2013", variable = self.regulation, value = 2013, indicatoron = 0)
        self.gpa_regulation_2018 = tk.Radiobutton(self.gpa_regulation_frame, text = "Regulation 2018", variable = self.regulation, value = 2018, indicatoron = 0)

        """Department Widgets """
        self.gpa_department_label = tk.Label(self.gpa_department_frame, text = "Select your Department", bg="grey", fg = "white")
        self.gpa_department_CSE = tk.Radiobutton(self.gpa_department_frame, text = "CSE", variable = self.department, value = "CSE", indicatoron = 0)
        self.gpa_department_IT = tk.Radiobutton(self.gpa_department_frame, text = "IT", variable = self.department, value = "IT", indicatoron = 0)
        self.gpa_department_EEE = tk.Radiobutton(self.gpa_department_frame, text = "EEE", variable = self.department, value = "EEE", indicatoron = 0)
        self.gpa_department_ECE = tk.Radiobutton(self.gpa_department_frame, text = "ECE", variable = self.department, value = "ECE", indicatoron = 0)
        self.gpa_department_EIE = tk.Radiobutton(self.gpa_department_frame, text = "EIE", variable = self.department, value = "EIE", indicatoron = 0)

        """Semester Widgets """
        self.gpa_semester_label = tk.Label(self.gpa_semester_frame, text = "Select your Semester", bg = "grey", fg ="white")

        """Creating buttons to display subjects_grade_frame"""
        self.gpa_display_frame_button = tk.Button(self.gpa_calculator_tab, text = "Display Subjects", command = self.display_subjects)
        self.gpa_calculator_tab.bind('<Return>', self.display_subjects)

        """Subjects Widgets"""
        self.gpa_subjects_label = tk.Label(self.gpa_subjects_frame, text = "Enter your Subjects Grade", bg = "grey", fg = "white")


        #Styling the frames
        self.gpa_calculator_tab['borderwidth'] = 5
        self.cgpa_calculator_tab['borderwidth'] = 5

        self.gpa_regulation_frame['borderwidth'] = 5
        self.gpa_department_frame['borderwidth'] = 5
        self.gpa_semester_frame['borderwidth'] = 5
        self.gpa_subjects_frame['borderwidth'] = 5
        self.gpa_display_frame_button['borderwidth'] = 5


        #packing the widgets
        self.calculator_notebook.add(self.gpa_calculator_tab, text = "GPA") #Adding the gpa tab to the notebook
        self.calculator_notebook.add(self.cgpa_calculator_tab, text = "CGPA") #Adding the cgpa tab to the notebook

        self.calculator_notebook.pack(fill = tk.BOTH, expand = 1)

        self.gpa_regulation_frame.pack()
        self.gpa_department_frame.pack()
        self.gpa_semester_frame.pack()
        self.gpa_display_frame_button.pack()
        self.gpa_subjects_frame.pack()

        self.gpa_regulation_label.pack(side = tk.TOP, fill = tk.X)
        self.gpa_regulation_2008.pack(side = tk.LEFT)
        self.gpa_regulation_2013.pack(side = tk.LEFT)
        self.gpa_regulation_2018.pack(side = tk.LEFT)

        self.gpa_department_label.pack(side = tk.TOP, fill = tk.X)
        self.gpa_department_CSE.pack(side = tk.LEFT)
        self.gpa_department_IT.pack(side = tk.LEFT)
        self.gpa_department_EEE.pack(side = tk.LEFT)
        self.gpa_department_ECE.pack(side = tk.LEFT)
        self.gpa_department_EIE.pack(side = tk.LEFT)

        self.gpa_semester_label.pack(side = tk.TOP, fill = tk.X)
        for sem, text in self.semesters:
            self.semester_radiobutton = tk.Radiobutton(self.gpa_semester_frame, text = text, variable = self.semester, value = sem, indicatoron = 0)
            self.semester_radiobutton.pack(side = tk.LEFT)

        self.gpa_subjects_label.pack(side = tk.TOP, fill = tk.X)




    def initialize_cgpa_calculator_tab(self):
        #Initializing the gpa_calculator_tab

        self.cgpa_regulation_frame = tk.Frame(self.cgpa_calculator_tab) #Frame for cgpa regulation
        self.cgpa_department_frame = tk.Frame(self.cgpa_calculator_tab) #Frame for cgpa department
        self.cgpa_semester_frame = tk.Frame(self.cgpa_calculator_tab) #Frame for cgpa semester
        self.cgpa_subjects_frame = tk.Frame(self.cgpa_calculator_tab) #Frame for cgpa subjects
        self.display_sem_frame = tk.Frame(self.cgpa_subjects_frame) #Frame for semesters and gpa input bar

        """Regulation Widgets """
        self.cgpa_regulation_label = tk.Label(self.cgpa_regulation_frame, text = "Select your Syllabus Regulation", bg = "grey", fg ="white")
        self.cgpa_regulation_2008 = tk.Radiobutton(self.cgpa_regulation_frame, text = "Regulation 2008", variable = self.regulation, value = 2008, indicatoron = 0)
        self.cgpa_regulation_2013 = tk.Radiobutton(self.cgpa_regulation_frame, text = "Regulation 2013", variable = self.regulation, value = 2013, indicatoron = 0)
        self.cgpa_regulation_2018 = tk.Radiobutton(self.cgpa_regulation_frame, text = "Regulation 2018", variable = self.regulation, value = 2018, indicatoron = 0)

        """Department Widgets """
        self.cgpa_department_label = tk.Label(self.cgpa_department_frame, text = "Select your Department", bg="grey", fg = "white")
        self.cgpa_department_CSE = tk.Radiobutton(self.cgpa_department_frame, text = "CSE", variable = self.department, value = "CSE", indicatoron = 0)
        self.cgpa_department_IT = tk.Radiobutton(self.cgpa_department_frame, text = "IT", variable = self.department, value = "IT", indicatoron = 0)
        self.cgpa_department_EEE = tk.Radiobutton(self.cgpa_department_frame, text = "EEE", variable = self.department, value = "EEE", indicatoron = 0)
        self.cgpa_department_ECE = tk.Radiobutton(self.cgpa_department_frame, text = "ECE", variable = self.department, value = "ECE", indicatoron = 0)
        self.cgpa_department_EIE = tk.Radiobutton(self.cgpa_department_frame, text = "EIE", variable = self.department, value = "EIE", indicatoron = 0)

        """Semester Widgets """
        self.cgpa_semester_label = tk.Label(self.cgpa_semester_frame, text = "Select your Semester", bg = "grey", fg ="white")

        """Creating buttons to display semester_cgpa_frame"""
        self.cgpa_display_frame_button = tk.Button(self.cgpa_calculator_tab, text = "Display Semesters", command = self.display_semester)

        """Subjects Widgets"""
        self.cgpa_subjects_label = tk.Label(self.cgpa_subjects_frame, text = "Enter your Subjects Grade", bg = "grey", fg = "white")


        #Styling the frames
        self.gpa_calculator_tab['borderwidth'] = 5
        self.cgpa_calculator_tab['borderwidth'] = 5

        self.cgpa_regulation_frame['borderwidth'] = 5
        self.cgpa_department_frame['borderwidth'] = 5
        self.cgpa_semester_frame['borderwidth'] = 5
        self.cgpa_subjects_frame['borderwidth'] = 5
        self.cgpa_display_frame_button['borderwidth'] = 5

        #Packing the widgets
        self.cgpa_regulation_frame.pack()
        self.cgpa_department_frame.pack()
        self.cgpa_semester_frame.pack()
        self.cgpa_display_frame_button.pack()
        self.cgpa_subjects_frame.pack()

        self.cgpa_regulation_label.pack(side = tk.TOP, fill = tk.X)
        self.cgpa_regulation_2008.pack(side = tk.LEFT)
        self.cgpa_regulation_2013.pack(side = tk.LEFT)
        self.cgpa_regulation_2018.pack(side = tk.LEFT)

        self.cgpa_department_label.pack(side = tk.TOP, fill = tk.X)
        self.cgpa_department_CSE.pack(side = tk.LEFT)
        self.cgpa_department_IT.pack(side = tk.LEFT)
        self.cgpa_department_EEE.pack(side = tk.LEFT)
        self.cgpa_department_ECE.pack(side = tk.LEFT)
        self.cgpa_department_EIE.pack(side = tk.LEFT)

        self.cgpa_semester_label.pack(side = tk.TOP, fill = tk.X)
        for sem, text in self.semesters:
            self.semester_radiobutton = tk.Radiobutton(self.cgpa_semester_frame, text = text, variable = self.semester, value = sem, indicatoron = 0)
            self.semester_radiobutton.pack(side = tk.LEFT)

        self.cgpa_subjects_label.pack(side = tk.TOP, fill = tk.X)




    def display_subjects(self, event = None):

        self.subjects_credits = np.array(self.regulation_departments_semester[self.regulation.get()][self.department.get()][self.semester.get()])

        self.subjects_name = np.array(self.subjects_credits[...,0])
        self.subject_credit = np.array(self.subjects_credits[...,1], dtype = int)


        """Subject Display Widget"""
        for widget in self.display_frame.winfo_children():
            widget.destroy()
        self.display_frame.pack()

        self.subject_entry = []
        self.subject_entry_grade = []

        index = 0
        for subject,credit in self.subjects_credits:
            self.grade_var = tk.StringVar()
            self.subject_entry_grade.append(self.grade_var)

            self.subject_label = tk.Label(self.display_frame, text = subject)
            self.grade_entry = tk.Entry(self.display_frame, textvariable = self.subject_entry_grade[index])

            self.current_subject_entry = [self.subject_label, self.grade_entry]
            self.subject_entry.append(self.current_subject_entry)

            index += 1

        index = 0
        for label, entry in self.subject_entry:
            label.grid(row = index)
            entry.grid(row = index, column = 1)
            index += 1


        self.display_frame['borderwidth'] = 10

        self.calculate_gpa = tk.Button(self.display_frame, text = "Calculate GPA", command = self.gpa_calculation)
        self.calculate_gpa['borderwidth'] = 5
        self.calculate_gpa.grid(row = index, columnspan = 2)


    def gpa_calculation(self):

        self.grade_credits = np.array([self.grade_credit_value[self.subject_entry_grade[index].get()] for index in range(len(self.subject_entry_grade))])
        
        self.cgp_product_sum = sum(self.grade_credits * self.subject_credit)
        self.credit_sum = round(sum(self.subject_credit), 3)

        self.gpa = self.cgp_product_sum / self.credit_sum

        msg.showinfo("GPA", self.gpa)


    def display_semester(self):

        self.subjects_credits = np.array(self.regulation_departments_semester[self.regulation.get()][self.department.get()][self.semester.get()])

        self.credit_value = np.array(self.subjects_credits[...,1], dtype = int)

        """Subject Display Widget"""
        for widget in self.display_sem_frame.winfo_children():
            widget.destroy()
        self.display_sem_frame.pack()

        self.semester_entry = []
        self.semester_gpa_entry = []
        index = 0

        for sem,name in self.semesters:
            self.gpa_var = tk.DoubleVar()
            self.semester_gpa_entry.append(self.gpa_var)
            if sem > self.semester.get():
                break

            self.semester_label = tk.Label(self.display_sem_frame, text = name)
            self.gpa_entry = tk.Entry(self.display_sem_frame, textvariable = self.semester_gpa_entry[index])

            self.current_semester_entry = [self.semester_label, self.gpa_entry]
            self.semester_entry.append(self.current_semester_entry)

            index += 1

        index = 0
        for sem, gpa_entry in self.semester_entry:
            sem.grid(row = index)
            gpa_entry.grid(row = index, column = 1)
            index += 1


        self.display_sem_frame['borderwidth'] = 10

        self.calculate_cgpa = tk.Button(self.display_sem_frame, text = "Calculate CGPA", command = self.cgpa_calculation)
        self.calculate_cgpa['borderwidth'] = 5
        self.calculate_cgpa.grid(row = index, columnspan = 2)



    def cgpa_calculation(self): #Doubt persists

        self.gpa_total = 0
        self.credit_total = 0
        for current_sem in range(self.semester.get()):
            self.credit_total += sum([credit for subject,credit in self.regulation_departments_semester[self.regulation.get()][self.department.get()][current_sem+1]])

        for index in range(len(self.semester_gpa_entry)):
            self.gpa_total += self.semester_gpa_entry[index].get()

        self.cgpa = round(self.gpa_total / self.credit_total, 3)

        msg.showinfo("CGPA", self.cgpa)



calc = Calculator()
calc.mainloop()
