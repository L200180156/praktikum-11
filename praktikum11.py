##kegiatan 1
##from Tkinter import Tk, Label, Button
##from tkMessageBox import showinfo
##
##my_app=Tk(className='DATA DIRI')
##
##L1=Label(my_app, text='DATA DIRI', font=('arial', 15))
##L1.grid(row=0, column=0)
##L2=Label(my_app, text='Nama')
##L2.grid(row=1, column=0)
##L3=Label(my_app, text='Aulia Putri')
##L3.grid(row=1, column=1)
##L4=Label(my_app, text='NIM')
##L4.grid(row=2,column=0)
##L5=Label(my_app, text='L200180156')
##L5.grid(row=2, column=1)
##L6=Label(my_app, text='Buku Favorit')
##L6.grid(row=3,column=0)
##L7=Label(my_app, text='Buku kosong')
##L7.grid(row=3,column=1)
##L8=Label(my_app, text='Idola')
##L8.grid(row=4,column=0)
##L9=Label(my_app, text='Orang Yang Baik Apa Adanya')
##L9.grid(row=4,column=1)
##L10=Label(my_app, text='Motto')
##L10.grid(row=5,column=0)
##L11=Label(my_app, text='Perlakukan orang lain sebagaimana kamu ingin diperlukan')
##L11.grid(row=5,column=1)
##
##B=Button(my_app, text='tutup', command=my_app.destroy)
##B.grid(row=6, column=1)
##my_app.mainloop()

####kegiatan 2
##
##from Tkinter import Tk, Label, Button, Entry, StringVar
##from tkMessageBox import showinfo
##
##my_app= Tk(className='kalkulator')
##
##L1=Label(my_app, text='angka1')
##str1 = StringVar()
##L1.grid(row=0, column=0)
##E1=Entry(my_app, textvariable= str1)
##E1.grid(row=0, column=1, columnspan=3)
##L2=Label(my_app, text='angka2')
##L2.grid(row=1, column=0)
##str2 = StringVar()
##E2=Entry(my_app, textvariable = str2)
##E2.grid(row=1, column=1, columnspan=3)
##
##def tambah():
##    'menjumlahkan dua bilangan'
##    angka1=float(str1.get())
##    angka2=float(str2.get())
##    hasilpenjumlahan= angka1 + angka2
##    hs.config(text=hasilpenjumlahan)
##
##def kurang():
##    'menjumlahkan dua bilangan'
##    angka1=float(str1.get())
##    angka2=float(str2.get())
##    hasilpengurangan= angka1 - angka2
##    hs.config(text=hasilpengurangan)
##
##def perkalian():
##    'menjumlahkan dua bilangan'
##    angka1=float(str1.get())
##    angka2=float(str2.get())
##    hasilperkalian= angka1 * angka2
##    hs.config(text=hasilperkalian)
##
##def pembagian():
##    'menjumlahkan dua bilangan'
##    angka1=float(str1.get())
##    angka2=float(str2.get())
##    hasilpembagian= angka1 / angka2
##    hs.config(text=hasilpembagian)
##
##
##
##
##B1=Button(my_app, text='+', command=tambah)
##B1.grid(row='3', column='0')
##B2=Button(my_app, text='-', command=kurang)
##B2.grid(row='3', column='1')
##B3=Button(my_app, text='x', command=perkalian)
##B3.grid(row='3', column='2')
##B4=Button(my_app, text=':', command=kurang)
##B4.grid(row='3', column='3')
##hs=Label(my_app, text='0')
##hs.grid(row=4, column=1)
##
##my_app.mainloop()

##kegiatan 3

from Tkinter import Tk, Label, Button, Entry, StringVar
from tkMessageBox import showinfo

my_app=Tk(className='JAJAR GENJANG')

j1=Label(my_app, text='JAJAR GENJANG', font=('arial', 15))
j1.grid(row=0, column=0)
j2=Label(my_app, text='''Jajar genjang adalah bangun dua dimensi yang dibentuk oleh dua pasang rusuk, \n yang masing-masing sama panjang dan sejajar dengan pasangannya, serta dua pasang sudut yang sama besar dan berhadapan.''')
j2.grid(row=1, column=0)

L1=Label(my_app, text='alas')
L1.grid(row=2, column=0)
str1=StringVar()
E1=Entry(my_app, textvariable='str1')
E1.grid(row=2, column=1, columnspan=3)

L2=Label(my_app, text='tinggi')
L2.grid(row=3, column=0)
str2=StringVar()
E2=Entry(my_app, textvariable='str2')
E2.grid(row=3, column=1, columnspan=3)

def luas():
    alas=float(str1.get())
    tinggi=float(str2.get())
    luas=alas*tinggi
    HL.config(text=luas)
    
B=Button(my_app, text='Hitung Luas', command=luas)
B.grid(row=4, column=0)
L=Label(my_app, text='Luas', font='calibri 10')
L.grid(row=4, column=1)
HL=Label(my_app, text=0)
HL.grid(row=4, column=2)

my_app.mainloop()
