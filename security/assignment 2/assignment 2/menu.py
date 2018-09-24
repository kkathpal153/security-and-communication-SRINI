from Tkinter import *
import Tkinter
import urllib2,cookielib ,urllib
import zipfile, StringIO
import requests, zipfile, StringIO
import urllib2,cookielib ,urllib
import zipfile, StringIO
import requests, zipfile, StringIO
import time
def readme():
    pass
def requirement():
    pass

#evry url has two parts fist then dates then last the front and the last part remains constant always its the dates that changes
link={"bhav_copy1":"https://www.nseindia.com/content/historical/EQUITIES/","bhav_copy2":"bhav.csv.zip",
      "daily_vol1":"https://www.nseindia.com/archives/nsccl/volt/CMVOLT_","daily_vol2":".CSV",
      "market1":"https://www.nseindia.com/archives/equities/mkt/MA","market2":".csv",
      "sw1":"https://www.nseindia.com/archives/equities/mto/MTO_","sw2":".DAT",
      "margin1":"https://www.nseindia.com/archives/equities/margin/Margintrdg_","margin2":".zip",
      "short1":"https://www.nseindia.com/archives/equities/shortSelling/shortselling_","short2":".csv",
      "sc1":"https://www.nseindia.com/archives/nsccl/mult/C_CATG_","sc2":".T01",
      "pulse1":"https://www.nseindia.com/archives/fo/monthly/NSE_Market_Pulse_","pulse2":".pdf",
      "equity1":"http://www.bseindia.com/download/BhavCopy/Equity/EQ","equity2":"_CSV.ZIP",
      "derivatives1":"http://www.bseindia.com/download/Bhavcopy/Derivative/bhavcopy","derivatives2":".zip",
      "currency1":"http://www.bseindia.com/bsedata/CIML_bhavcopy/CurrencyBhavCopy_","currency2":".ZIP",
      "debt1":"http://www.bseindia.com/download/Bhavcopy/Debt/DEBTBHAVCOPY","debt2":".zip"}
#it will explain weather the dates of the link has spacing or not, if yes what type of spacing is that
explain={"bhav_copy":"no",
      "daily_vol":"no",
      "market":"no",
      "sw":"no",
      "margin":"no",
      "short":"no",
      "sc":"no",
      "pulse":"no",
      "equity":"no",
      "derivatives":"yes",
      "currency":"no",
      "debt":"no"}
#it will tell us what type of downlaoder should be used to downlaod the file
filetype={"bhav_copy":".zip",
      "daily_vol":".csv",
      "market":".csv",
      "sw":".DAT",
      "margin":".zip",
      "short":".csv",
      "sc":".T01",
      "pulse":".pdf",
      "equity":".zip",
      "derivatives":".zip",
      "currency":".zip",
      "debt":".zip"}
#it will tell the format of dates either it is dates:month:year or year:month:dates
format={"bhav_copy":"sidha",
      "daily_vol":"sidha",
      "market":"sidha",
      "sw":"sidha",
      "margin":"sidha",
      "short":"sidha",
      "sc":"sidha",
      "pulse":"sidha",
      "equity":"sidha",
      "derivatives":"sidha",
      "currency":"ulta",
      "debt":"sidha"}
#it will tell us the year is in yyyy or yy format
yeard={"bhav_copy":"full",
      "daily_vol":"full",
      "market":"short",
      "sw":"full",
      "margin":"short",
      "short":"full",
      "sc":"full",
      "pulse":"full",
      "equity":"short",
      "derivatives":"short",
      "currency":"full",
      "debt":"full"}
#it is used to convert the dates types month to numeric type as we know that in the url it varies
month_con={"JAN":"01","FEB":"02","MAR":"03","APR":"04","MAY":"05","JUN":"06","JUL":"07","AUG":"08","SEP":"09","OCT":"10","NOV":"11","DEC":"12"}

date=""
ddi=[]
def save(string):
    ddi.append(string)
    print "file downloaded date" + ddi[-1]
    return
root =Tk()

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
buff=[]
def emptybuff():
    for i in range(0,len(buff)):
        buff.pop()
    return

def emptyddi():
    for i in range(0,len(ddi)):
        ddi.pop()
    return



#root frame intitialization
main=Frame(root,height=20,bd=2,relief=SUNKEN )
nsef=Frame(root,height=20,bd=93,bg="red" ,relief=SUNKEN )
bsef=Frame(root,height=20,bd=43,relief=SUNKEN ,bg="blue" )

#downloader frame initialization
single=Frame(root,height=40, bd=23,relief=SUNKEN )
multi=Frame(root,height=20, bd=33,relief=SUNKEN )

#NSE frame initialization
bhav_copy=Frame(root,height=20,bd=33,relief=SUNKEN ,bg="red" )
daily_vol=Frame(root,height=20,bd=33,relief=SUNKEN ,bg="red" )
market=Frame(root,height=20,bd=33,relief=SUNKEN ,bg="red" )
sw=Frame(root,height=20,bd=33,relief=SUNKEN ,bg="red" )
margin=Frame(root,height=20,bd=33,relief=SUNKEN ,bg="red" )
short=Frame(root,height=20,bd=33,relief=SUNKEN ,bg="red" )
sc=Frame(root,height=20,bd=33,relief=SUNKEN ,bg="red" )
pulse=Frame(root,height=20,bd=33,relief=SUNKEN ,bg="red" )

#for BSE frame initialization
equity=Frame(root,height=20,bd=33,relief=SUNKEN,bg="blue")
derivatives=Frame(root,height=20,bd=33,relief=SUNKEN,bg="blue")
currency=Frame(root,height=20,bd=33,relief=SUNKEN,bg="blue")
debt=Frame(root,height=20,bd=33,relief=SUNKEN,bg="blue")



def raise_frame(frame):
    if(frame==main):
        root.geometry("300x210")
        emptybuff()
    elif(frame==nsef):
        root.geometry("400x400")
        emptybuff()
    #frame setting for nse frame
    elif(frame==bhav_copy):
        root.geometry("200x210")
        buff.append("bhav_copy")
    elif(frame==daily_vol):
        root.geometry("200x210")
        buff.append("daily_vol")
    elif(frame==market):
        root.geometry("200x210")
        buff.append("market")
    elif(frame==sw):
        root.geometry("200x210")
        buff.append("sw")
    elif(frame==margin):
        root.geometry("200x210")
        buff.append("margin")
    elif(frame==short):
        root.geometry("200x210")
        buff.append("short")
    elif(frame==sc):
        root.geometry("200x210")
        buff.append("sc")
    elif(frame==pulse):
        root.geometry("200x210")
        buff.append("pulse")
    #frame setting for BSE frame
    elif(frame==equity):
        root.geometry("200x210")
        buff.append("equity")
    elif(frame==derivatives):
        root.geometry("200x210")
        buff.append("derivatives")
    elif(frame==currency):
        root.geometry("200x210")
        buff.append("currency")
    elif(frame==debt):
        root.geometry("200x210")
        buff.append("debt")
    elif(frame==bsef):
        root.geometry("200x210")
        emptybuff()
    elif(frame==single):
        root.geometry("400x250")
    elif(frame==multi):
        root.geometry("360x240")
    frame.tkraise()


    
for frame in (main,nsef,single,multi,bsef,bhav_copy,single,daily_vol,market,sw,margin,short,sc,pulse,equity,derivatives,currency,debt):
    frame.grid(row=0, column=0, sticky='news')


def downloader_zip(string):
    try:
        r = requests.get(string, stream=True,headers=hdr)
        z = zipfile.ZipFile(StringIO.StringIO(r.content))
        z.extractall()
    except:
        print ("link doesn't exist")



def other_downloader(string):
    try:
        filename=buff[-1]+ ddi[-1] +filetype[buff[-1]]
        #print "file name is" + filename
        with open(filename, 'wb') as handle:
            response = requests.get(string, stream=True,headers=hdr)

            if not response.ok:
                pass
            for block in response.iter_content(1024):
                handle.write(block)
    except:
        print("link doesnt exist")
def month_conv(monthi):
    if( buff[-1]=="bhav_copy" or buff[-1]=="sc" or buff[-1]=="pulse"):
        return monthi
    else:
        return month_con[monthi]
def year_conv(yeari):
    if ( yeard[buff[-1]]=="full"):
        return yeari
    else:
        return yeari[2:4]


def date_style(date,month,year):
    if(format[buff[-1]]=="sidha"):
        return date+month+year
    else:
        return year+month+date

def generate_string(present_date,month,year):
    emptyddi()
    resetsingly()
    dates=present_date
    
    month=month_conv(month)
   
    year=year_conv(year)
    date=date_style(dates,month,year)
    save(date)
    if(buff[-1]=="bhav_copy"):
        converted_date=year+"/"+month+"/cm"+date
        string=link[buff[-1]+"1"]+converted_date+link[buff[-1]+"2"]
        return string
    elif(buff[-1]=="sc" or buff[-1]=="pulse"):
         string=link[buff[-1]+"1"]+month+year+link[buff[-1]+"2"]
         return string
    elif(buff[-1]=="derivatives"):
        string=link[buff[-1]+"1"]+date+"-"+month+"-"+year+link[buff[-1]+"2"]
        return string
    else:
        string=  link[buff[-1]+"1"]+date+link[buff[-1]+"2"]
        #print "the url is "+string
        return string
    

def singly():#entry 4 #entry5 #entry 6
    dates=entry4.get()
    string=generate_string(entry4.get(),entry5.get(),entry6.get())
    if(filetype[buff[-1]]==".zip"):
         downloader_zip(string)
         return
    else:
         other_downloader(string)
#########

def multif():#entry8 entry 9 entry 10 entry 11
    start_date=entry8.get()
    end_date=entry9.get()
    #print int(start_date)
    #print int(end_date)+1
    for i in range (int(start_date),int(end_date)+1):
        if(i<=9):
            j='0'+str(i)
        #print j
        string=generate_string(j,entry10.get(),entry11.get())
        if(filetype[buff[-1]]==".zip"):
            downloader_zip(string)
            return
        else:
            other_downloader(string)
        time.sleep(5)
        

pic=PhotoImage(file="nse.gif")
pic2=PhotoImage(file="bse.gif")
#for the main screen
menui=Menu(main)
important=Menu(menui,tearoff=0)
important.add_command(label="Read me", command=readme)
important.add_separator()
important.add_command(label="Essentials", command=requirement)
menui.add_cascade(label="Click Me",menu=important)

label=Tkinter.Label(main,image=pic)
label.photo=pic
label.grid(row=0, column=0)
label2=Tkinter.Label(main,image=pic2)
label2.photo=pic2
label2.grid(row=1, column=0)


Button(main, text='For Nse', command=lambda:raise_frame(nsef),bg="red").grid(row=0,column=1)
Button(main, text='For Bse', command=lambda:raise_frame(bsef),bg="blue").grid(row=1,column=1)



#for NSE and its menu
label=Tkinter.Label(nsef,text="Please enter your choice",bg="red")
label.grid(row=0)
Button(nsef, text="1. Bhav Copy", command=lambda:raise_frame(bhav_copy)).grid(row=1)
Button(nsef, text="2. Daily Volatility File", command=lambda:raise_frame(daily_vol)).grid(row=2)
Button(nsef, text="3. Equities - Market Activity Report", command=lambda:raise_frame(market)).grid(row=3)
Button(nsef, text="4. Equities - Security-wise Delivery Position", command=lambda:raise_frame(sw)).grid(row=4)
Button(nsef, text="5. Equities - Margin Trading", command=lambda:raise_frame(margin)).grid(row=5)
Button(nsef, text="6. Equities - Short-Selling", command=lambda:raise_frame(short)).grid(row=6)
Button(nsef, text="7. NSCCL - Security Category", command=lambda:raise_frame(sc)).grid(row=7)
Button(nsef, text="8. NSE Market Pulse", command=lambda:raise_frame(pulse)).grid(row=8)
Button(nsef, text='Go back to main Menu', command=lambda:raise_frame(main),bg="red").grid(row=9,column=0)


#for Bse and its menu
label2=Tkinter.Label(bsef,text="Please enter your choice:",bg="blue")
label2.grid(row=0)
Button(bsef, text="Equity Bhav Copy", command=lambda:raise_frame(equity)).grid(row=1)
Button(bsef, text="Derivatives Bhav Copy", command=lambda:raise_frame(derivatives)).grid(row=2)
Button(bsef, text="Currency Derivative/IRD", command=lambda:raise_frame(currency)).grid(row=3)
Button(bsef, text="Debt", command=lambda:raise_frame(debt)).grid(row=4)
Button(bsef, text='Go back to main Menu', command=lambda:raise_frame(main),bg="blue").grid(row=9,column=0)


#for single file download
label3=Tkinter.Label(single,text="Enter the details respectively",bg="red")
label3.grid(row=0)
label4=Tkinter.Label(single,text="date",bg="red")
label4.grid(row=1,column=0)
entry4=Entry(single,bd=4)
entry4.insert(END,"dd")
entry4.grid(row=1,column=1)
label5=Tkinter.Label(single,text="month",bg="red")
label5.grid(row=2,column=0)
entry5=Entry(single,bd=4)
entry5.insert(END,"January='JAN'")
entry5.grid(row=2,column=1)
label6=Tkinter.Label(single,text="year",bg="red")
label6.grid(row=3,column=0)
entry6=Entry(single,bd=4)
entry6.insert(END,"yyyy")
entry6.grid(row=3,column=1)
Button(single, text='click to download', command=singly,bg="green").grid(row=4,column=0)
Button(single, text='Go back to main Menu', command=lambda:raise_frame(main),bg="red").grid(row=5,column=0)
def resetsingly():
    entry6.insert(END,"yyyy")
    entry5.insert(END,"January='JAN'")
    entry4.insert(END,"dd")
    



#for multi file download
label7=Tkinter.Label(multi,text="Enter the details respectively",bg="red")
label7.grid(row=0)
label8=Tkinter.Label(multi,text="start date",bg="red")
label8.grid(row=1,column=0)
entry8=Entry(multi,bd=4)
entry8.insert(END,"dd")
entry8.grid(row=1,column=1)
label9=Tkinter.Label(multi,text="ending date",bg="red")
label9.grid(row=2,column=0)
entry9=Entry(multi,bd=4)
entry9.insert(END,"dd")
entry9.grid(row=2,column=1)
label10=Tkinter.Label(multi,text="month",bg="red")
label10.grid(row=3,column=0)
entry10=Entry(multi,bd=4)
entry10.insert(END,"January='JAN'")
entry10.grid(row=3,column=1)
label11=Tkinter.Label(multi,text="year",bg="red")
label11.grid(row=4,column=0)
entry11=Entry(multi,bd=4)
entry11.insert(END,"yyyy")
entry11.grid(row=4,column=1)
Button(multi, text='click to download', command=multif,bg="green").grid(row=5,column=0)
Button(multi, text='Go back to main Menu', command=lambda:raise_frame(main),bg="red").grid(row=7,column=0)





#for NSE_BhavCopy
label4=Tkinter.Label(bhav_copy,text="Please enter your choice",bg="red")
label4.grid(row=0)
Button(bhav_copy, text="single file download", command=lambda:raise_frame(single)).grid(row=1)
Button(bhav_copy, text="multiple file download", command=lambda:raise_frame(multi)).grid(row=2)
Button(bhav_copy, text='Go back to NSE Menu', command=lambda:raise_frame(nsef),bg="red").grid(row=3,column=0)
Button(bhav_copy, text='Go back to main Menu', command=lambda:raise_frame(main),bg="red").grid(row=4,column=0)


#daily_vol frame
label11=Tkinter.Label(daily_vol,text="Please enter your choice ",bg="red")
label11.grid(row=0)
Button(daily_vol, text="single file download", command=lambda:raise_frame(single)).grid(row=1)
Button(daily_vol, text="multiple file download", command=lambda:raise_frame(multi)).grid(row=2)
Button(daily_vol, text='Go back to NSE Menu', command=lambda:raise_frame(nsef),bg="red").grid(row=3,column=0)
Button(daily_vol, text='Go back to main Menu', command=lambda:raise_frame(main),bg="red").grid(row=4,column=0)

#market frame
label12=Tkinter.Label(market,text="Please enter your choice",bg="red")
label12.grid(row=0)
Button(market, text="single file download", command=lambda:raise_frame(single)).grid(row=1)
Button(market, text="multiple file download", command=lambda:raise_frame(multi)).grid(row=2)
Button(market, text='Go back to NSE Menu', command=lambda:raise_frame(nsef),bg="red").grid(row=3,column=0)
Button(market, text='Go back to main Menu', command=lambda:raise_frame(main),bg="red").grid(row=4,column=0)

#sw frame
label13=Tkinter.Label(sw,text="Please enter your choice",bg="red")
label13.grid(row=0)
Button(sw, text="single file download", command=lambda:raise_frame(single)).grid(row=1)
Button(sw, text="multiple file download", command=lambda:raise_frame(multi)).grid(row=2)
Button(sw, text='Go back to NSE Menu', command=lambda:raise_frame(nsef),bg="red").grid(row=3,column=0)
Button(sw, text='Go back to main Menu', command=lambda:raise_frame(main),bg="red").grid(row=4,column=0)

#margin frame
label15=Tkinter.Label(margin,text="Please enter your choice",bg="red")
label15.grid(row=0)
Button(margin, text="single file download", command=lambda:raise_frame(single)).grid(row=1)
Button(margin, text="multiple file download", command=lambda:raise_frame(multi)).grid(row=2)
Button(margin, text='Go back to NSE Menu', command=lambda:raise_frame(nsef),bg="red").grid(row=3,column=0)
Button(margin, text='Go back to main Menu', command=lambda:raise_frame(main),bg="red").grid(row=4,column=0)


#short frame
label14=Tkinter.Label(short,text="Please enter your choice",bg="red")
label14.grid(row=0)
Button(short, text="single file download", command=lambda:raise_frame(single)).grid(row=1)
Button(short, text="multiple file download", command=lambda:raise_frame(multi)).grid(row=2)
Button(short, text='Go back to NSE Menu', command=lambda:raise_frame(nsef),bg="red").grid(row=3,column=0)
Button(short, text='Go back to main Menu', command=lambda:raise_frame(main),bg="red").grid(row=4,column=0)

#sc frame
label16=Tkinter.Label(sc,text="Please enter your choice",bg="red")
label16.grid(row=0)
Button(sc, text="single file download", command=lambda:raise_frame(single)).grid(row=1)
Button(sc, text="multiple file download", command=lambda:raise_frame(multi)).grid(row=2)
Button(sc, text='Go back to NSE Menu', command=lambda:raise_frame(nsef),bg="red").grid(row=3,column=0)
Button(sc, text='Go back to main Menu', command=lambda:raise_frame(main),bg="red").grid(row=4,column=0)

#pulse frame

label17=Tkinter.Label(pulse,text="Please enter your choice",bg="red")
label17.grid(row=0)
Button(pulse, text="single file download", command=lambda:raise_frame(single)).grid(row=1)
Button(pulse, text="multiple file download", command=lambda:raise_frame(multi)).grid(row=2)
Button(pulse, text='Go back to NSE Menu', command=lambda:raise_frame(nsef),bg="red").grid(row=3,column=0)
Button(pulse, text='Go back to main Menu', command=lambda:raise_frame(main),bg="red").grid(row=4,column=0)





#for bse sub frames
#for euity frame
label18=Tkinter.Label(equity,text="Please enter your choice",bg="blue")
label18.grid(row=0)
Button(equity, text="single file download", command=lambda:raise_frame(single)).grid(row=1)
Button(equity, text="multiple file download", command=lambda:raise_frame(multi)).grid(row=2)
Button(equity, text='Go back to BSE Menu', command=lambda:raise_frame(bsef),bg="blue").grid(row=3,column=0)
Button(equity, text='Go back to main Menu', command=lambda:raise_frame(main),bg="blue").grid(row=4,column=0)

#for derivatives frame
label19=Tkinter.Label(derivatives,text="Please enter your choice",bg="blue")
label19.grid(row=0)
Button(derivatives, text="single file download", command=lambda:raise_frame(single)).grid(row=1)
Button(derivatives, text="multiple file download", command=lambda:raise_frame(multi)).grid(row=2)
Button(derivatives, text='Go back to BSE Menu', command=lambda:raise_frame(bsef),bg="blue").grid(row=3,column=0)
Button(derivatives, text='Go back to main Menu', command=lambda:raise_frame(main),bg="blue").grid(row=4,column=0)

# for currency frame
label20=Tkinter.Label(currency,text="Please enter your choice",bg="blue")
label20.grid(row=0)
Button(currency, text="single file download", command=lambda:raise_frame(single)).grid(row=1)
Button(currency, text="multiple file download", command=lambda:raise_frame(multi)).grid(row=2)
Button(currency, text='Go back to BSE Menu', command=lambda:raise_frame(bsef),bg="blue").grid(row=3,column=0)
Button(currency, text='Go back to main Menu', command=lambda:raise_frame(main),bg="blue").grid(row=4,column=0)

#for debt frame
label21=Tkinter.Label(debt,text="Please enter your choice",bg="blue")
label21.grid(row=0)
Button(debt, text="single file download", command=lambda:raise_frame(single)).grid(row=1)
Button(debt, text="multiple file download", command=lambda:raise_frame(multi)).grid(row=2)
Button(debt, text='Go back to BSE Menu', command=lambda:raise_frame(bsef),bg="blue").grid(row=3,column=0)
Button(debt, text='Go back to main Menu', command=lambda:raise_frame(main),bg="blue").grid(row=4,column=0)





raise_frame(main)
root.config(menu=menui)
root.mainloop()


