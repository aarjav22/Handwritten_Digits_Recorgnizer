from tkinter import *
import PIL
from PIL import Image,ImageTk,ImageDraw
from tkinter.font import Font
from tkinter import messagebox
from tkinter import ttk
import time
import pickle
from skimage.io import imread
from skimage.exposure import rescale_intensity
from skimage.transform import resize

class main_class:
    def __init__(self,menu):
        main_menu=menu
        main_menu.geometry("720x480+120+120")
        main_menu.title("Digit Recognizer")
        main_menu.resizable(0,0)
        main_menu.configure(background='#F7F9F9')

        self.background=PhotoImage(file='./background/back.png')
        background=Label(main_menu,image=self.background,
                         background='#F7F9F9').pack()
        self.posx=122
        self.posy=84
        self.sizex=210
        self.sizey=210
        self.b1='up'
        self.xold=None
        self.yold=None

        self.drawing_area=Canvas(main_menu,width=210,height=210,
                            background='White')
        self.drawing_area.place(x=122,y=84)
        self.drawing_area.bind("<Motion>",self.motion)
        self.drawing_area.bind("<ButtonPress-1>",self.b1down)
        self.drawing_area.bind("<ButtonRelease-1>",self.b1up)

        self.icon1=PhotoImage(file='./icon/icon1.png')
        button=Button(main_menu,image=self.icon1,
                      background="#F7F9F9",border='0',
                      activebackground='#F7F9F9',
                      command=lambda:self.save(main_menu)
                      ).place(x=30,y=390)

        self.icon2=PhotoImage(file='./icon/icon2.png')
        button=Button(main_menu,image=self.icon2,
                      background="#F7F9F9",border='0',
                      activebackground='#F7F9F9',
                      command=self.clear).place(x=120,y=390)

        self.icon3=PhotoImage(file='./icon/icon3.png')
        button=Button(main_menu,image=self.icon3,
                      background="#F7F9F9",border='0',
                      activebackground='#F7F9F9',
                      command=self.information).place(x=210,y=390)

        self.icon4=PhotoImage(file='./icon/icon4.png')
        button=Button(main_menu,image=self.icon4,
                      background="#F7F9F9",border='0',
                      activebackground='#F7F9F9',
                      command=main_menu.destroy).place(x=300,y=390)

        self.image=Image.new("RGB",(210,210),(0,0,0))
        self.draw=ImageDraw.Draw(self.image)

        Maker=Label(main_menu,text=" ~ Aarjav Kumar Jain",
                    background='#F7F9F9',font=Font(family='Segoe Print',size=8)).place(x=580,y=450)

    def save(self,main_menu):
        self.image.save('./data/image.jpg')
        self.result_window(main_menu)

    def clear(self):
        self.drawing_area.delete("all")
        self.image=Image.new("RGB",(210,210),(0,0,0))
        self.draw=ImageDraw.Draw(self.image)

    def b1down(self,event):
        self.b1="down"

    def b1up(self,event):
        self.b1='up'
        self.xold=None
        self.yold=None

    def motion(self,event):
        if self.b1=="down":
            if self.xold is not None and self.yold is not None:
                event.widget.create_line(self.xold,self.yold,
                                         event.x,event.y,smooth='true',
                                         width=5,fill="Black")

                self.draw.line(((self.xold,self.yold),
                                (event.x,event.y)),
                               (255,255,255),width=5)

        self.xold=event.x
        self.yold=event.y

    def result_window(self,main_menu):
        result_window=Toplevel(main_menu)
        result_window.geometry("720x480+120+120")
        result_window.title("Result")
        result_window.resizable(0,0)
        result_window.configure(background='#F7F9F9')
        font=Font(family='Segoe Print',size=10)
        self.wall=PhotoImage(file="./background/wall.png")
        wallpaper=Label(result_window,image=self.wall,background="#F7F9F9").pack()

        button=Button(result_window,image=self.icon4,background="#F7F9F9",border='0',
                      activebackground='#F7F9F9',
                      command=result_window.destroy).place(x=643,y=404)

        s = ttk.Style()
        s.theme_use('default')
        s.configure("TProgressbar",background='#454545',
                    troughcolor='#F7F9F9',thickness=30)

        zero_label=Label(result_window,text="Zero",font=font,
                         background="#F7F9F9").place(x=47,y=310)
        zero=ttk.Progressbar(result_window,orient='vertical',
                             length=250,style="TProgressbar")
        zero.place(x=50,y=50)

        one_label=Label(result_window,text="One",font=font,
                        background="#F7F9F9").place(x=100,y=310)
        one=ttk.Progressbar(result_window,orient='vertical',
                            length=250,style="TProgressbar",)
        one.place(x=100,y=50)

        two_label=Label(result_window,text="Two",font=font,
                        background="#F7F9F9").place(x=150,y=310)
        two=ttk.Progressbar(result_window,orient='vertical',
                            length=250,style="TProgressbar")
        two.place(x=150,y=50)

        three_label=Label(result_window,text="Three",font=font,
                          background="#F7F9F9").place(x=195,y=310)
        three=ttk.Progressbar(result_window,orient='vertical',
                              length=250,style="TProgressbar")
        three.place(x=200,y=50)

        four_label=Label(result_window,text="Four",font=font,
                         background="#F7F9F9").place(x=250,y=310)
        four=ttk.Progressbar(result_window,orient='vertical',
                             length=250,style="TProgressbar")
        four.place(x=250,y=50)

        five_label=Label(result_window,text="Five",font=font,
                         background="#F7F9F9").place(x=302,y=310)
        five=ttk.Progressbar(result_window,orient='vertical',
                             length=250,style="TProgressbar")
        five.place(x=300,y=50)

        six_label=Label(result_window,text="Six",font=font,
                        background="#F7F9F9").place(x=353,y=310)
        six=ttk.Progressbar(result_window,orient='vertical',
                            length=250,style="TProgressbar")
        six.place(x=350,y=50)

        seven_label=Label(result_window,text="Seven",font=font,
                          background="#F7F9F9").place(x=395,y=310)
        seven=ttk.Progressbar(result_window,orient='vertical',
                              length=250,style="TProgressbar")
        seven.place(x=400,y=50)

        eight_label=Label(result_window,text="Eight",font=font,
                          background="#F7F9F9").place(x=448,y=310)
        eight=ttk.Progressbar(result_window,orient='vertical',
                              length=250,style="TProgressbar")
        eight.place(x=450,y=50)

        nine_label=Label(result_window,text="Nine",font=font,
                         background="#F7F9F9").place(x=500,y=310)
        nine=ttk.Progressbar(result_window,orient='vertical',
                             length=250,style="TProgressbar")
        nine.place(x=500,y=50)

        per=list(map(int,self.model_result()))

        for i in range(per[0]):
            time.sleep(0.0005)
            zero['value']=i
            zero.update()

        for i in range(per[1]):
            time.sleep(0.0005)
            one['value']=i
            one.update()

        for i in range(per[2]):
            time.sleep(0.0005)
            two['value']=i
            two.update()

        for i in range(per[3]):
            time.sleep(0.0005)
            three['value']=i
            three.update()

        for i in range(per[4]):
            time.sleep(0.0005)
            four['value']=i
            four.update()

        for i in range(per[5]):
            time.sleep(0.0005)
            five['value']=i
            five.update()

        for i in range(per[6]):
            time.sleep(0.0005)
            six['value']=i
            six.update()

        for i in range(per[7]):
            time.sleep(0.0005)
            seven['value']=i
            seven.update()

        for i in range(per[8]):
            time.sleep(0.005)
            eight['value']=i
            eight.update()

        for i in range(per[9]):
            time.sleep(0.0005)
            nine['value']=i
            nine.update()

        zero_per=Label(result_window,text=str(per[0])+" %",font=font,
                       background="#F7F9F9").place(x=50,y=20)

        one_per=Label(result_window,text=str(per[1])+" %",font=font,
                       background="#F7F9F9").place(x=100,y=20)

        two_per=Label(result_window,text=str(per[2])+" %",font=font,
                       background="#F7F9F9").place(x=150,y=20)

        three_per=Label(result_window,text=str(per[3])+" %",font=font,
                       background="#F7F9F9").place(x=200,y=20)

        four_per=Label(result_window,text=str(per[4])+" %",font=font,
                       background="#F7F9F9").place(x=250,y=20)

        five_per=Label(result_window,text=str(per[5])+" %",font=font,
                       background="#F7F9F9").place(x=300,y=20)

        six_per=Label(result_window,text=str(per[6])+" %",font=font,
                       background="#F7F9F9").place(x=350,y=20)

        seven_per=Label(result_window,text=str(per[7])+" %",font=font,
                       background="#F7F9F9").place(x=400,y=20)

        eight_per=Label(result_window,text=str(per[8])+" %",font=font,
                       background="#F7F9F9").place(x=450,y=20)

        nine_per=Label(result_window,text=str(per[9])+" %",font=font,
                       background="#F7F9F9").place(x=500,y=20)



        self.img_1=PhotoImage(file="./numbers/"+str(per.index(max(per)))+".png")
        image_label=Label(result_window,image=self.img_1,
                          background="#F7F9F9").place(x=560,y=90)

        res=Label(result_window,text="Answer is "+str(per.index(max(per))),
                  background="#F7F9F9",font=Font(family='Segoe Print',
                                                 size=20)).place(x=130,y=410)

    def model_result(self):
        img=resize(imread('./data/image.jpg'),(8,8))
        img=rescale_intensity(img,out_range=(0,16))
        img=[sum(pixel)/3.0 for row in img for pixel in row]

        with open("model",'rb') as f:
            model=pickle.load(f)

        ans=model.predict([img])
        prob=model.predict_proba([img])*100
        return [value for row in prob for value in row]

    def information(self):
        info_window=Toplevel(main_menu)
        info_window.geometry("720x480+120+120")
        info_window.title("Information")
        info_window.resizable(0,0)
        info_window.configure(background='#F7F9F9')
        font=Font(family='Segoe Print',size=10)
        self.wall=PhotoImage(file="./background/wallpaper.png")
        wallpaper=Label(info_window,image=self.wall,background="#F7F9F9").pack()

        button=Button(info_window,image=self.icon4,background="#F7F9F9",border='0',
                      activebackground='#F7F9F9',
                      command=info_window.destroy).place(x=643,y=404)

        text_window=Text(info_window,width=69,height=15,font=Font(family='Segoe Print',
                                                 size=10))
        text_window.place(x=10,y=30)
        text="""The Hand Writter Digit Recognizer

The dataset is taken from sklearn.datasets package. This dataset is made up of 1797 8x8 images.
I have used the Support Vector Mechine(SVM) a supervised machine learning algorithm to solve this
classification problem.Dataset contain DESCR,data,images,target,target_names from which

x-labels are 64 columns contaning the pixel value of the 8x8 image(data).
y-label is the diget range from 0 to 9(target).

I have applied classification algorithm like DecisionTreeClassifier,RandomForestClassifier,SVC,
KNeighborsClassifier,GaussianNB and test some cases DecisionTreeClassifier,RandomForestClassifier
gives the Accuracy of 100% but are not so good in practical but KNeighborsClassifier gives Accuracy
of 99% but in good in practical so I have used KNeighborsClassifier algorithm for the model.

Accuracy of the model is : 99%

        """
        text_window.insert(INSERT,text)

main_menu=Tk()
main_object=main_class(main_menu)
main_menu.mainloop()
