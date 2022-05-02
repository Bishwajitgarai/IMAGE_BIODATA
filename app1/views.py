import os
from django.core.files.storage import FileSystemStorage
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html",{})
def upload(request):
    if request.method == 'POST':
        up_file=request.FILES['csv_file']
        fs=FileSystemStorage()
        fs.save(up_file.name,up_file)
        ur=fs.url(up_file.name)
        Rot=os.path.join('C:/Users/BISWAJIT/OneDrive/Desktop/Django/project2/media/',up_file.name)
        import pytesseract
        import cv2
        import csv
        from pytesseract.pytesseract import Output
        pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        img1=cv2.imread(Rot)
        color=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
        cus_conf=r'--oem 3 --psm 6 '
        th=cv2.threshold(color,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        detail=pytesseract.image_to_data(th,output_type=Output.DICT,config=cus_conf)
        parse_text=[]
        word_list=[]
        last_word=''
        for word in detail['text']:
        
            if word!='':
                word_list.append(word)
                last_word=word
            if (last_word!='' and word=='') or (word==detail['text'][-1]) :
                parse_text.append(word_list)
                word_list=[]
        #SAVE
        with open('C:/Users/BISWAJIT/OneDrive/Desktop/Django/project2/static/result.txt','w',newline="") as file:
            csv.writer(file,delimiter=" ").writerows(parse_text)
        import re
        import phonenumbers
        import spacy
        nlp=spacy.load('en_core_web_lg')
        lis_p=re.compile("^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])( )([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])$")

        month_p="^(JANUARY|JAN|FEBRUARY|FEB|MARCH|MAR|APRIL|APR|MAY|JUNE|JUN|JULY|JUL|AUG|AUGUST|SEPTEMBER|SEP|OCTOBER|OCT|NOVEMBER|NOV|DECEMBER|DEC)"
        dat_y=re.compile("^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\.|-|/| |,)([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])")

        date_pat=re.compile("^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\.|-|/| )([1-9]|0[1-9]|1[0-2]|JANUARY|JAN|FEBRUARY|FEB|MARCH|MAR|APRIL|APR|MAY|JUNE|JUN|JULY|JUL|AUG|AUGUST|SEPTEMBER|SEP|OCTOBER|OCT|NOVEMBER|NOV|DECEMBER|DEC)(\.|-|/| )([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])$")  
        date_pat1=re.compile("^([1-9]|0[1-9]|1[0-2]|JANUARY|JAN|FEBRUARY|FEB|MARCH|MAR|APRIL|APR|MAY|JUNE|JUN|JULY|JUL|AUG|AUGUST|SEPTEMBER|SEP|OCTOBER|OCT|NOVEMBER|NOV|DECEMBER|DEC)(\.|-|/| )([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(\.|-|/| |,)([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])$")  
        date_pat2=re.compile("^([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])(\.|-|/| )([1-9]|0[1-9]|1[0-2]|JANUARY|JAN|FEBRUARY|FEB|MARCH|MAR|APRIL|APR|MAY|JUNE|JUN|JULY|JUL|AUG|AUGUST|SEPTEMBER|SEP|OCTOBER|OCT|NOVEMBER|NOV|DECEMBER|DEC)(\.|-|/| )([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])$")  
        date=[]  
        email_pat=re.compile("^[a-z0-9._%+-]+[\._]?[a-z0-9.-]+[@]\w+([.]\w{2,3})*$")
        email=[]
        name_pat=re.compile('[A-Z]{1}[a-zA-Z]\w')
        name_patt=re.compile('([A-Z]{1}\w\D)')
        nam1_pat=('^[A-Z]{1}[a-zA-Z]\w+(([\',. -][a-zA-Z ])?[a-zA-Z])*$')
        nam="Not Found!!"
        emf=[]
        with open('C:/Users/BISWAJIT/OneDrive/Desktop/Django/project2/static/result.txt') as f:
            lines=f.readlines()
        li=" ".join([str(i) for i in lines])


        p=[]
        a="NAME"
        b="Name"
        yy=" "
        mo="mother"
        fa="father"

        n=0
        for i in lines:
            i=i.strip()
            if a in i:
                nh=[]
                po=str(i).replace("NAME","")
                po=po.split(" ")
                for fg in po:
                    if re.match(name_patt,fg):
                        nh.append(fg)
                fgh=",".join(nh)
                fgh=fgh.replace(","," ")
                hjk=fgh.lower()
                if mo in hjk:pass
                elif fa in hjk:pass
                else:
                    print("NAME : ",fgh)
                    nam=fgh
                    n=1

            if b in i :
                nh=[]
                po=str(i).replace("Name","")
                po=po.split(" ")
                for fg in po:
                    if re.match(name_patt,fg):
                        nh.append(fg)
                fgh=",".join(nh)
                fgh=fgh.replace(","," ")
                hjk=fgh.lower()
                if mo in hjk:pass
                elif fa in hjk:pass
                else:
                    print("NAME : ",fgh)
                    n=1
                    nam=fgh


            if re.match(name_pat,str(i)):
                nh=[]
                po=str(i)
                po=po.split(" ")
                for fg in po:
                    if re.match(name_patt,fg):
                        nh.append(fg)
                fgh=",".join(nh)
                fgh=fgh.replace(","," ")
                if re.match(nam1_pat,fgh):
                    p.append(fgh)
            asd=i.upper()
            if re.match(date_pat,str(asd)):
                    date.append(str(i))
            if re.match(date_pat1,str(asd)):
                    date.append(str(i))
            if re.match(date_pat2,str(asd)):
                    date.append(str(i))
            jkl=i.lower()
            if re.match(email_pat,str(jkl)):
                email.append(i)
                emf.append(i)
            if yy in i:
                jh=i.split(" ")
                for k in jh:
                    klq=k.lower()
                    if re.match(date_pat,str(klq)):
                        date.append(str(k))
                    if re.match(date_pat1,str(klq)):
                        date.append(str(k))
                    if re.match(date_pat2,str(klq)):
                        date.append(str(k))
                    if re.match(email_pat,str(klq)):
                        email.append(k)
                        emf.append(k)
            if yy in i:
                i=i.upper()
                jh=i.split(" ")

                for ol in jh:
                    if re.match(month_p,ol):
                        jhf=i.split(ol)
                        for klkk in jhf:
                            pass
                            oooo=klkk.strip()
                            if re.match(dat_y,oooo):
                                uii=ol,oooo
                                uii=",".join(uii)
                                uii=uii.replace(","," ")
                                date.append(uii)
                    if re.match(month_p,ol):
                        jhf=i.split(ol)
                        uii=",".join(jhf)
                        s = []
                        for t in uii.split():
                            try:
                                s.append(int(t))
                            except ValueError:
                                pass
                        listToStr = ' '.join([str(elem) for elem in s])
                        hjjk=listToStr.strip()

                        if re.match(lis_p,hjjk):
                            trp=ol,hjjk
                            trp=",".join(trp)
                            trp=trp.replace(","," ")
                            date.append(trp)

        h="@"

        e=[]
        if len(emf)>0:
            ex=str(emf[0])
            sp=ex.split(" ")
            for i in sp:
                if h in i:
                    e.append(i)
        res=str(e).split("@")[0]
        alpha=""
        for word in res:
            if word.isalpha():
                alpha+=word
        alpha=alpha.lower()
        #print("Alpha Value",alpha)
        kly=""
        for i in p:
            if yy in i:
                if n==0:
                    op=(str(i)).replace(" ","")
                    k=str(op)
                    p1=k.lower()
                    if len(alpha)!=0:
                        if alpha in p1:
                            nh=[]
                            po=i.split(" ")
                            for fg in po:
                                if re.match(name_patt,fg):
                                    nh.append(fg)
                            fgh=",".join(nh)
                            fgh=fgh.replace(","," ")
                            print("Accuired name from email : ",fgh)
                            nam=fgh
                            n=1
                            kly="hello"
                            break
        if len(kly)==0 :
            kl=[]
            for jk in p:
                if yy in jk:
                    if n==0:
                        op=jk.split(" ")
                        op[0],op[1]=op[1],op[0]
                        odf=",".join(op)
                        odf=odf.replace("\n","")
                        odf=odf.replace(",","")
                        odf=odf.lower()
                        if len(alpha)!=0:
                        
                            if  alpha in odf:
                                nh=[]
                                po=jk.split(" ")
                                for fg in po:
                                    if re.match(name_patt,fg):
                                        nh.append(fg)
                                fgh=",".join(nh)
                                fgh=fgh.replace(","," ")
                                print("Accuired name from email by swap : ",fgh)
                                nam=fgh
                                n=1
                                break
                if yy in jk:
                    if n==0:
                        nlp=spacy.load("en_core_web_lg")
                        hjk=jk.split(" ")
                        fgh=[]
                        for hjkk in hjk:
                            fgh.append(hjkk.capitalize())
                            jk=",".join(fgh)
                            jk=jk.replace(","," ")
                        doc=nlp(jk)
                        oll=1
                        while oll==1:
                            oll=oll+1
                            for on in doc.ents:
                                if on.label_ =="PERSON":
                                    print("Name by spacy :",on.text)#,on.label_)
                                    nam=on.text
                                    n=1
                                    break
        if email:
            for i in email:
                print("Email : ",i)
                em=i
        else:
            print("Email not found !!")
            em=("Email not found !!")

        if date:
            for da in date:
                print("Date : ",da)
            dat=da
        else:
            print("Date not found !!")
            dat="Not found !!"
        nu=0
        n=phonenumbers.PhoneNumberMatcher(li,"IN")
        for num in n:
            nu=1
            print(num)
            nab=num
        if nu==0:
            print("Phone Number Not Found !!")
            nab="Phone Number Not Found !!"


    return render(request,'result.html',{"em":em,"numb":nab,"dat":dat,"name":nam})

def result(request):
    pass