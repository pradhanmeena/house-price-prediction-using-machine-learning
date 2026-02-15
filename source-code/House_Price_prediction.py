from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image,ImageTk
import pandas as pd
import numpy as np
from tkinter import messagebox

class House_price_prediction:
    def __init__(self,root):
        #=======================Application name & background Image=============
        self.root=root
        self.root.title("HOUSE PRICE PREDICTION")
        self.root.geometry("1920x1080")
        
        mainp=Image.open(r"D:\python projects\House price prediction\Image1.png")
        mainp=mainp.resize((1920,1080),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(mainp)
        label=Label(self.root,image=self.photoimg,bg="#484e45")
        label.place(x=0,y=0,width=1920,height=1080)
        #===============Variables declairation==================
        self.var_path=StringVar()
       
        self.var_price=StringVar()
        #================Color_variables========================
        self.BGC="#265f70"
        self.Text_lb_bg="#CCC7BF"
        self.Text_lb_c="#31393C"

        #/===============Get & Submmit Dataset path++++++++++++

        Text1=Label(self.root,text="Insert Path :",font=("Verdana",13,"bold"),bg=self.Text_lb_bg,fg=self.Text_lb_c)
        Text1.place(x=467,y=200)

        Dataset_path=Entry(self.root,font=("Verdana",13),bg="#ffffff",bd="0",fg="#081B26",textvariable=self.var_path)
        Dataset_path.place(x=686,y=195,width=553,height=40)

        
        
        Click=Button(self.root,text="Browse",bg=self.BGC,font=("Verdana",15,"bold"),bd="0",activebackground="#f23000",fg="white",command=self.Browse)
        Click.place(x=1260,y=198,width=130,height=36)

        Reset_B=Button(self.root,text="Reset Path",bg=self.BGC,font=("Verdana",15,"bold"),bd="0",activebackground="#f23000",fg="white",command=self.Clear_path)
        Reset_B.place(x=1410,y=198,width=150,height=36)

        Click=Button(self.root,text="Submit",bg=self.BGC,font=("Verdana",15,"bold"),bd="0",activebackground="#f23000",fg="white",comman=self.Submit)
        Click.place(x=1840/2,y=270,width=190,height=35)

        #++++++++++++ Data Entery & Labels First Column++++++++++++++++++++++++
        
        
        label_location=Label(self.root,text="Select House Location :",font=("Verdana",13,"bold"),bg=self.Text_lb_bg,fg=self.Text_lb_c)
        label_location.place(x=280,y=335)
        label_location=ttk.Combobox(self.root,font=("Verdana",13),state="readonly")
        label_location["value"]=("")
        label_location.set("Select Location")
        
        label_location.place(x=540,y=330,width=380,height=40)
        
       

        label_H_Size=Label(self.root,text="Enter House Size(sqft.) :",font=("Verdana",13,"bold"),bg=self.Text_lb_bg,fg=self.Text_lb_c)
        label_H_Size.place(x=280,y=420)

        H_size=Entry(self.root,font=("Verdana",13),bg="#ffffff",bd="0",fg="#081B26")
        H_size.place(x=540,y=415,width=380,height=40)

        label_P_Size=Label(self.root,text="Enter plot size(sqft.) :",font=("Verdana",13,"bold"),bg=self.Text_lb_bg,fg=self.Text_lb_c)
        label_P_Size.place(x=280,y=505)

        P_size=Entry(self.root,font=("Verdana",13),bg="#ffffff",bd="0",fg="#081B26")
        P_size.place(x=540,y=500,width=380,height=40)

        label_N_badrooms=Label(self.root,text="Select No. of Bedrooms:",font=("Verdana",13,"bold"),bg=self.Text_lb_bg,fg=self.Text_lb_c)
        label_N_badrooms.place(x=280,y=590)
        N_badrooms=ttk.Combobox(self.root,font=("Verdana",13),state="readonly")
        N_badrooms["value"]=()
                                 
        N_badrooms.set("Select")
        N_badrooms.place(x=540,y=585,width=380,height=40)
        #++++++++++++ Data Entery & Labels Second Column++++++++++++++++++++++++

        label_N_bathrooms=Label(self.root,text="Select No. of Bathrooms:",font=("Verdana",13,"bold"),bg=self.Text_lb_bg,fg=self.Text_lb_c)
        label_N_bathrooms.place(x=1000,y=335)

        N_bathrooms=ttk.Combobox(self.root,font=("Verdana",13),state="readonly")
        N_bathrooms["value"]=("")
                                 
        N_bathrooms.set("Select")
        N_bathrooms.place(x=1260,y=330,width=380,height=40)
        
        
        Year_build=Label(self.root,text="Select Build year :",font=("Verdana",13,"bold"),bg=self.Text_lb_bg,fg=self.Text_lb_c)
        Year_build.place(x=1000,y=420)

        Year_build_E=ttk.Combobox(self.root,font=("Verdana",13),state="readonly")
        Year_build_E["value"]=("")
        Year_build_E.set("Select Build Year")
        Year_build_E.place(x=1260,y=415,width=380,height=40)

        Condition=Label(self.root,text="Select House Condition :",font=("Verdana",13,"bold"),bg=self.Text_lb_bg,fg=self.Text_lb_c)
        Condition.place(x=1000,y=505)

        Condition_E=ttk.Combobox(self.root,font=("Verdana",13),state="readonly")
        Condition_E["value"]=('')

        Condition_E.set("Select Condition")
        Condition_E.place(x=1260,y=500,width=380,height=40)

        Has_Basement=Label(self.root,text="House Basement(Y/N) :",font=("Verdana",13,"bold"),bg=self.Text_lb_bg,fg=self.Text_lb_c)
        Has_Basement.place(x=1000,y=590)

        Has_Basement_E=ttk.Combobox(self.root,font=("Verdana",13),state="readonly")
        Has_Basement_E["value"]=("")
        Has_Basement_E.set("Select")
        Has_Basement_E.place(x=1260,y=585,width=380,height=40)

        #===============Predict Frame++++++++++++

        Click=Button(self.root,text="Predict Price",bg=self.BGC,font=("Verdana",15,"bold"),bd="0",activebackground="#f23000",fg="white",comman=self.Check_Price)
        Click.place(x=940,y=680,width=160,height=36)
        Text2=Label(self.root,text="Predicted Price :",font=("Verdana",13,"bold"),bg=self.Text_lb_bg,fg=self.Text_lb_c)
        Text2.place(x=830,y=760)
        Entery_Price=Entry(self.root,text="203120",font=("Verdana",13),bg="#ffffff",bd="0",fg="black",textvariable=self.var_price)
        Entery_Price.place(x=1020,y=755,width=240,height=40)
        
        #===============reset button++++++++++++
        Reset_B=Button(self.root,text="Reset All",bg=self.BGC,font=("Verdana",15,"bold"),bd="0",activebackground="#f23000",fg="white",command=self.Clear_All)
        Reset_B.place(x=940,y=840,width=160,height=36)
    def Browse(self):
        Dataset_path=Entry(self.root,font=("Verdana",13),bg="#ffffff",bd="0",fg="#081B26",textvariable=self.var_path)
        Dataset_path.place(x=686,y=195,width=553,height=40)
        file_path =filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("All files", "*.*")])
        Dataset_path.insert(END, file_path)
    def Submit(self):
        if self.var_path.get()=="":
            messagebox.showerror("Error","Enter Dataset Path firstly",parent=self.root)
        else:
            global Location,Size,Plot,Bedrooms,Bathrooms,Year,Condition,Basement,Lr,x,y,dataset
            dataset=pd.read_csv(self.var_path.get())
            Column_names = dataset.columns.tolist()
            if Column_names!=['Location','Square_Feet', 'Lot_Size', 'Bedrooms', 'Bathrooms', 'Year_Built','Condition', 'Has_Basement', 'Price']:
                messagebox.showerror("Error","Dataset Attributes Not Match \n Please Insert Another dataset",parent=self.root)
            else:
                messagebox.showinfo("hurray!","Model Trained Successfully!\nPlease enter required information.",parent=self.root)
                self.var_Location=StringVar
                self.var_H_Size=IntVar()
                
                self.var_P_size=IntVar()
                
                self.var_Badrooms=IntVar()
                
                self.var_Bathrooms=IntVar()
                
                self.var_Year=IntVar()
                
                self.var_Condition=StringVar()
                
                self.var_Basement=StringVar()
                arr1=dataset['Location'].unique()
                List_L=[]
                for i in arr1:
                    List_L.append(i)
                
                self.var_Location=StringVar()
                label_location=ttk.Combobox(self.root,font=("Verdana",13),state="readonly",textvariable=self.var_Location)
                label_location["value"]=List_L

                label_location.set("Select Location")                    
                label_location.place(x=540,y=330,width=380,height=40)

                H_size=Entry(self.root,font=("Verdana",13),bg="#ffffff",bd="0",fg="#081B26",textvariable=self.var_H_Size)
                H_size.place(x=540,y=415,width=380,height=40)

                P_size=Entry(self.root,font=("Verdana",13),bg="#ffffff",bd="0",fg="#081B26",textvariable=self.var_P_size)
                P_size.place(x=540,y=500,width=380,height=40)
                arr1=dataset["Bedrooms"].unique()
                List_L=[]
                for i in arr1:
                    List_L.append(i)
                List_L.sort()
                N_badrooms=ttk.Combobox(self.root,font=("Verdana",13),textvariable=self.var_Badrooms)
                N_badrooms["value"]=List_L
                N_badrooms.set("Select")
                N_badrooms.place(x=540,y=585,width=380,height=40)
                
                arr1=dataset['Bathrooms'].unique()
                List_L=[]
                for i in arr1:
                    List_L.append(i)
                List_L.sort()
                N_bathrooms=ttk.Combobox(self.root,font=("Verdana",13),textvariable=self.var_Bathrooms)
                N_bathrooms["value"]=List_L
                N_bathrooms.set("Select")
                N_bathrooms.place(x=1260,y=330,width=380,height=40)
            
                arr1=dataset['Year_Built'].unique()
                List_L=[]
                for i in arr1:
                    List_L.append(i)
                List_L=sorted(List_L,reverse=True)
                Year_build_E=ttk.Combobox(self.root,font=("Verdana",13),textvariable=self.var_Year,state="readonly")
                Year_build_E["value"]=List_L
                Year_build_E.set("Select Year")
                Year_build_E.place(x=1260,y=415,width=380,height=40)

                arr1=dataset['Condition'].unique()
                List_L=[]
                for i in arr1:
                    List_L.append(i)
                Condition_E=ttk.Combobox(self.root,font=("Verdana",13),state="readonly",textvariable=self.var_Condition)
                Condition_E["value"]=List_L
                Condition_E.set("Select Condition")
                Condition_E.place(x=1260,y=500,width=380,height=40)
    
                arr1=dataset["Has_Basement"].unique()
                List_L1=[]
                for i in arr1:
                    List_L1.append(i)
                
                Has_Basement_E=ttk.Combobox(self.root,font=("Verdana",13),state="readonly",textvariable=self.var_Basement)
                Has_Basement_E["value"]=List_L1
                Has_Basement_E.set("Select") 
                Has_Basement_E.place(x=1260,y=585,width=380,height=40)

                        
                Location=self.var_Location
                Size=self.var_H_Size
                Plot=self.var_P_size
                Bedrooms=self.var_Badrooms
                Bathrooms=self.var_Bathrooms
                Year=self.var_Year
                Condition=self.var_Condition
                Basement=self.var_Basement

                #===============Predict Frame++++++++++++

                Click=Button(self.root,text="Predict Price",bg=self.BGC,font=("Verdana",15,"bold"),bd="0",activebackground="#f23000",fg="white",comman=self.Check_Price)
                Click.place(x=940,y=680,width=160,height=36)
                Text2=Label(self.root,text="Predicted Price :",font=("Verdana",13,"bold"),bg=self.Text_lb_bg,fg="#334b48")
                Text2.place(x=830,y=760)
                Entery_Price=Entry(self.root,text="203120",font=("Verdana",13),bg="#ffffff",bd="0",fg="black",textvariable=self.var_price)
                Entery_Price.place(x=1020,y=755,width=240,height=40)
                

                #===============reset button++++++++++++
                Reset_B=Button(self.root,text="Reset All",bg=self.BGC,font=("Verdana",15,"bold"),bd="0",activebackground="#f23000",fg="white",command=self.Clear_All)
                Reset_B.place(x=940,y=840,width=160,height=36)
        
    def Check_Price(self):
        self.var_price.set('')
        dataset=pd.read_csv(self.var_path.get())
        
        y=dataset[['Price']].values
        x=dataset[['Location','Square_Feet','Lot_Size','Bedrooms','Bathrooms','Year_Built','Condition','Has_Basement']].values
        
        from sklearn.impute import SimpleImputer
        import numpy as np
        imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
        x[:,1:2]=imputer.fit_transform(x[:,1:2]) #Square_Feet
        x[:,2:3]=imputer.fit_transform(x[:,2:3])#Lot_Size
        
        from sklearn.preprocessing import LabelEncoder
        LB=LabelEncoder()
        x[:,0]=LB.fit_transform(x[:,0])
        x[:,6]=LB.fit_transform(x[:,6])
        x[:,7]=LB.fit_transform(x[:,7])
        
        from sklearn.model_selection import train_test_split
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.12)
        
        from sklearn.linear_model import LinearRegression
        Lr=LinearRegression()
        Lr.fit(x_train,y_train)
        if (self.var_Location.get()=="Select Location" or self.var_H_Size.get()==0 or self.var_P_size.get()==0  or self.var_Badrooms.get()=="Select" or self.var_Bathrooms.get()=="Select"
            or self.var_Year.get()=="Select Year" or self.var_Condition.get()=="Select Condition" or self.var_Basement.get()=="Select"):
            messagebox.showerror("Error","Please Fill All Sections",parent=self.root)
        else:
            #==================Storing value++++++++++++++
            x_l=dataset["Location"].unique()
            from sklearn.preprocessing import LabelEncoder
            le=LabelEncoder()
            x=le.fit_transform(x_l)
            list_l=[]
            for i in x:
                list_l.append(i)
            dict_l={}
            count=0
            for i in x_l:
                dict_l[i]=list_l[count]
                count=count+1
            Location=self.var_Location.get()
            for i in dict_l:
                if i==Location:
                    Location=dict_l[Location]
            Square_Feet=self.var_H_Size.get()
        
            Lot_Size=self.var_P_size.get()
        
            Bedrooms=self.var_Badrooms.get()
        
            Bathrooms=self.var_Bathrooms.get()
        
            Year_Built=self.var_Year.get()
            #+++++++++for condition===============
            x_c=dataset["Condition"].unique()
            x=le.fit_transform(x_c)
            list_c=[]
            for i in x:
                list_c.append(i)
            dict_c={}
            count=0
            for i in x_c:
                dict_c[i]=list_c[count]
                count=count+1
            Condition=self.var_Condition.get()
            for i in dict_c:
                if i==Condition:
                    Condition=dict_c[Condition]
            #===========only for basement============
            x_b=dataset["Has_Basement"].unique()
            x=le.fit_transform(x_b)
            list_b=[]
            for i in x:
                list_b.append(i)
            dict_b={}
            count=0
            for i in x_b:
                dict_b[i]=list_b[count]
                count=count+1
            Has_Basement=self.var_Basement.get()
            for i in dict_b:
                
                if i==Has_Basement:
                    Has_Basement=dict_b[Has_Basement]        
            arr=np.array([[Location,Square_Feet,Lot_Size,Bedrooms,Bathrooms,Year_Built,Condition,Has_Basement]])
            pre=Lr.predict(arr)
            pre=pre[0,0]
            pre=round(pre, 2)
            pre=str(pre)+"INR"
            Entery_Price=Entry(self.root,text="203120",font=("Verdana",13),bg="#ffffff",bd="0",fg="black",textvariable=self.var_price)
            Entery_Price.place(x=1020,y=755,width=240,height=40)
            Entery_Price.insert(END,pre)
            
    def Clear_All(self):
        
        self.var_Location.set('Select Location')
        self.var_H_Size.set('')
        self.var_P_size.set('')
        self.var_Badrooms.set('Select')
        self.var_Bathrooms.set('Select')
        self.var_Year.set("Select year")
        self.var_Condition.set('Select House Condition')
        self.var_Basement.set('Select Here')
        self.var_price.set('')

    def Clear_path(self):
        self.var_path.set('')
        
if __name__=="__main__":
    root=Tk()
    obj=House_price_prediction(root)
    root.mainloop()
