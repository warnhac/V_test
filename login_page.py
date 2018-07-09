import Tkinter
import tkMessageBox

login_window = Tkinter.Tk()
login_window.minsize(width=666, height=400)

###########################################################################################################

def add_initial_code():
	string1 = e1.get()
	tkMessageBox.showinfo( "error", "Test Case Name Added" )
	test_case_window.destroy()


############################################################################################################

def add_initial_code01():
	string1 = e1.get()
	tkMessageBox.showinfo( "error","Break Point Added")
	BP_window.destroy()

############################################################################################################
def quit():
    pass


############################################################################################################


def Add_Testcase():
	#print getting
    global test_case_window
    test_case_window = Tkinter.Tk()
    
    test_case_window.minsize(width = 600 , height = 400) 

    #label.config(width=200)

    w =Tkinter.Label(test_case_window, text="Enter Test Case Name",font=("Helvetica", 25))
    w.place(x = 100 , y = 100)

    test_case_name = Tkinter.Entry(test_case_window)
    test_case_name.place(x = 100 , y = 150)

    B9 = Tkinter.Button(test_case_window, text ="ADD TEST CASE NAME", command = add_initial_code)
    B9.place(x=100, y=200)

   

   # B8 = Tkinter.Button(test_case_window, text ="Close", command = quit)
   # B8.place(x=100, y =150)

    test_case_window.mainloop()


#############################################################################################################

def Add_BreakPoint():

	global BP_window
	BP_window= Tkinter.Tk()
 	BP_window.minsize(width = 600 , height = 400)  

 	w1 = Tkinter.Label(BP_window,text = "ENTER BREAK POINT LINE ",font=("Helvetica", 25))
 	w1.place(x=100,y=100)

 	test_caseline = Tkinter.Entry(BP_window)
 	test_caseline.place(x=100 , y=150)

 	B10 = Tkinter.Button(BP_window,text = "Add_BP", command=add_initial_code01)
 	B10.place (x=100 , y =200)
	BP_window.mainloop()

#############################################################################################################



def add_variable_WW():
	pass


#############################################################################################################

def Comapre_variable_WW():
	shoaub=50
	
	

#############################################################################################################
def Check_BP():
	global check_bp_window
	check_bp_window = Tkinter.Tk()
	check_bp_window.minsize(width = 600 , height = 400) 

	w1 = Tkinter.Label(check_bp_window,text = "ENTER BREAK POINT NUMBER TO CHECK ",font=("Helvetica", 25))
	w1.place(x=100,y=100)

 	break_point_number = Tkinter.Entry(check_bp_window)
 	break_point_number.place(x=100 , y=150)

 	B12 = Tkinter.Button(check_bp_window,text = "Check_BP", command=add_initial_code01)
 	B12.place (x=100 , y =200)

	chek_bp_window.mainloop()

#############################################################################################################
def Generate_Script():
	pass


#############################################################################################################

def check_BP():
	pass
	



e1 = Tkinter.Entry(login_window)
e1.place(x = 300 , y = 60)

#dict = {'first': Add_Testcase("shoaib")}
B2 = Tkinter.Button(login_window, text ="Add_TestCase_name", command=Add_Testcase )
B2.place(x=100, y=60)

B3 = Tkinter.Button(login_window, text ="Add_Break-Point    ", command = Add_BreakPoint)
B3.place(x=100, y=90)

B4 = Tkinter.Button(login_window, text ="Check Break-Point Reach    ", command = Check_BP)
B4.place(x=100, y=120)

B5 = Tkinter.Button(login_window, text ="Generate automate test case  Script    ", command = Generate_Script)
B5.place(x=100, y=150)






#button_01= Tkinter.Button(text = "ENter", command = add_initial_code("shoaib"))
#button_01.Grid = (row =1 , column = 0 )
# 000210001001919-----------------utib0sjcb01
#B2.pack()
login_window.mainloop()
