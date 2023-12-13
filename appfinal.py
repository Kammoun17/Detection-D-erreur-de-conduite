from tkinter import *
import os
import numpy as np 
import pandas as pd 
from sklearn.impute import SimpleImputer 
imputer = SimpleImputer(missing_values=np.nan, strategy='mean') 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer 
from sklearn.cluster import KMeans

dataset=pd.read_excel('datasetfinal.xlsx')
x=dataset.iloc[:,12]
labelEncoder_X=LabelEncoder()
dataset.iloc[:,12]=labelEncoder_X.fit_transform(x)

one=OneHotEncoder()
one=pd.get_dummies(dataset['zone'])
#dataset.iloc[:,i]=onehotencoder.fit_transform(x).toarray()

dataset=dataset.drop('zone',axis=1)
dataset=one.join(dataset)
dataset
x=dataset.iloc[1:3,:12]
dataset=dataset.iloc[:,1:]

dataset=dataset.drop('time',axis=1)
dataset=dataset.drop('CIN',axis=1)


df=dataset
#from sklearn.decomposition import PCA
#pca =PCA(n_components=2)
#df = pca.fit_transform(df)
model = KMeans(n_clusters=4)

model.fit(df)
y1_kmeans=model.predict(df)














#ar = np.array([[1.1, 2, 3.3, 'urbaine']])
#dk = pd.DataFrame(ar, index = ['a1'], columns = ['A', 'B', 'C', 'D'])



def data_test():
    global y_kmeans
    if Zone.get()=='urbaine' :    
     A=np.array([[0,1,float(latitude.get()),float(longitude.get()),float(speed.get()),float(RPM.get()),float(Engine_load.get()),float(AmbientAirTemp.get()),float(ThrottlePos.get()),float(insFuel.get()),float(X.get()),float(Y.get()),float(Z.get())]])
     print(A)
    if Zone.get()=='nationale' :    
     A=np.array([[1,0,float(latitude.get()),float(longitude.get()),float(speed.get()),float(RPM.get()),float(Engine_load.get()),float(AmbientAirTemp.get()),float(ThrottlePos.get()),float(insFuel.get()),float(X.get()),float(Y.get()),float(Z.get())]])
     print(A)
    if Zone.get()=='autouroute' :    
     A=np.array([[0,0,float(latitude.get()),float(longitude.get()),float(speed.get()),float(RPM.get()),float(Engine_load.get()),float(AmbientAirTemp.get()),float(ThrottlePos.get()),float(insFuel.get()),float(X.get()),float(Y.get()),float(Z.get())]])
     
   
    
    dtest = pd.DataFrame(A, index=[0],columns = ['0','1', 'latitude', 'longitude', 'Speed','RPM','ENGINE_LOAD','AmbientAirTemp','ThrottlePos', 'insFuel','X','Y','Z'])
    
    y_kmeans=model.predict(dtest)
    #if y_kmeans[0]==0 : 
        #resultat_positive()
    #if y_kmeans[0]==1:
        #resultat_negatif()
    resultat_positive()

    
   
def resultat_positive(): 
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("resultat")
    screen6.geometry("150x100")   
    Label(screen6, text="c'est un bon conducteur {y_kmeans}".format(y_kmeans=y_kmeans)).pack()
    Button(screen6, text="ok", command=delete6).pack()

def resultat_negatif(): 
    global screen7
    screen7 = Toplevel(screen)
    screen7.title("resultat")
    screen7.geometry("150x100")   
    Label(screen7, text="c'est un mauvais conducteur").pack()
    Button(screen7, text="ok", command=delete7).pack()

def Test():
    global screen5
    global latitude 
    global longitude 
    global speed 
    global RPM 
    global Engine_load 
    global AmbientAirTemp 
    global ThrottlePos 
    global insFuel 
    global X 
    global Y 
    global Z 
    global Zone 
    
    screen5 = Toplevel(screen)
    screen5.title("Test")
  
    screen5.config(background="#000000")
    screen5.geometry("1920x1080")

    # creation d'un image
    width = 30
    height = 30
    #image = PhotoImage(file="logo.png").zoom(17).subsample(64)
    # canvas=Canvas(screen5,width=width,height=height,background="#000000")
    # canvas.create_image(width/2,height/2,anchor=NW,image=image)
    # canvas.pack()
    
    latitude = StringVar()
    longitude = StringVar()
    speed = StringVar()
    RPM = StringVar()
    Engine_load = StringVar()
    AmbientAirTemp = StringVar()
    ThrottlePos = StringVar()
    insFuel = StringVar()
    X = StringVar()
    Y = StringVar()
    Z = StringVar()
    Zone = StringVar()
    Label(screen5, text="Please enter details of car", font=(
        "arial", 15), background="#000000", fg='white').pack()
    Label(screen5, text="", background="#000000", fg='white').pack()

    Label(screen5, text="latitude ", background="#000000", fg='white').pack()
    latitude_entry = Entry(screen5, textvariable=latitude)
    latitude_entry.pack()
    Label(screen5, text="", background="#000000", fg='white').pack()

    Label(screen5, text="longitude  ", background="#000000", fg='white').pack()
    longitude_entry = Entry(screen5, textvariable=longitude)
    longitude_entry.pack()
    Label(screen5, text="", background="#000000", fg='white').pack()

    Label(screen5, text="Speed ", background="#000000", fg='white').pack()
    Speed_entry = Entry(screen5, textvariable=speed)
    Speed_entry.pack()
    Label(screen5, text="", background="#000000", fg='white').pack()

    Label(screen5, text="RPM ", background="#000000", fg='white').pack()
    RPM_entry = Entry(screen5, textvariable=RPM)
    RPM_entry.pack()
    Label(screen5, text="", background="#000000", fg='white').pack()

    Label(screen5, text="ENGINE LOAD ", background="#000000", fg='white').pack()
    Engine_load_entry = Entry(screen5, textvariable=Engine_load)
    Engine_load_entry.pack()
    Label(screen5, text="", background="#000000", fg='white').pack()

    Label(screen5, text="AmbientAirTemp ",
          background="#000000", fg='white').pack()
    AmbientAirTemp_entry = Entry(screen5, textvariable=AmbientAirTemp)
    AmbientAirTemp_entry.pack()
    Label(screen5, text="", background="#000000", fg='white').pack()

    Label(screen5, text="ThrottlePos ", background="#000000", fg='white').pack()
    ThrottlePos_entry = Entry(screen5, textvariable=ThrottlePos)
    ThrottlePos_entry.pack()
    Label(screen5, text="", background="#000000", fg='white').pack()

    Label(screen5, text="insFuel ", background="#000000", fg='white').pack()
    insFuel_entry = Entry(screen5, textvariable=insFuel)
    insFuel_entry.pack()
    Label(screen5, text="", background="#000000", fg='white').pack()

    Label(screen5, text="X ", background="#000000", fg='white').pack()
    X_entry = Entry(screen5, textvariable=X)
    X_entry.pack()
    Label(screen5, text="", background="#000000", fg='white').pack()

    Label(screen5, text="Y ", background="#000000", fg='white').pack()
    Y_entry = Entry(screen5, textvariable=Y)
    Y_entry.pack()
    Label(screen5, text="", background="#000000", fg='white').pack()

    Label(screen5, text="Z ", background="#000000", fg='white').pack()
    Z_entry = Entry(screen5, textvariable=Z)
    Z_entry.pack()
    Label(screen5, text="", background="#000000", fg='white').pack()

    Label(screen5, text="Zone ", background="#000000", fg='white').pack()
    Zone_entry = Entry(screen5, textvariable=Zone)
    Zone_entry.pack()
    Label(screen5, text="", background="#000000", fg='white').pack()

    Button(screen5, text="Register", width=10,
           height=1, command=data_test).pack()


def delete7():
    screen7.destroy()

def delete6():
    screen6.destroy()

def delete2():
    screen3.destroy()


def delete3():
    screen4.destroy()


def delete4():
    screen5.destroy()


def login_sucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text="Login Sucess").pack()
    Button(screen3, text="teste", command=Test).pack()


def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error").pack()
    Button(screen4, text="OK", command=delete3).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()


def register_user():
    print("working")

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Sucess",
          fg="green", font=("calibri", 11)).pack()


def login_verify():

    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            Test()
        else:
            password_not_recognised()

    else:
        user_not_found()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()

    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10,
           height=1, command=register_user).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10,
           height=1, command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("720x480")
    screen.title("Notes 1.0")
    screen.config(background="white")
    frame=Frame(screen,background="white")
    Label(screen,text = "Bienvenue", bg = "white", font = ("Calibri", 20),).pack(expand=YES)

    width = 300
    height = 300
    image = PhotoImage(file="lo.png").zoom(12).subsample(32)
    canvas = Canvas(frame, width=width, height=height, background="white",bd=0,highlightthickness=0)
    canvas.create_image(150, 150, image=image)
    canvas.grid(row=0,column=0,sticky=W)
    frame1=Frame(frame,background="white")

    Label(frame1,text = "",bg="white").pack()
    Button(frame1,text = "Login" , command = login,foreground = 'red',width=10).pack()
    Label(frame1,text = "",bg="white").pack()
    Button(frame1,text = "Register", command = register,foreground = 'red',width=10).pack()
    frame1.grid(row=0,column=1,sticky=W)
    frame.pack(expand=YES)

    screen.mainloop()


main_screen()
