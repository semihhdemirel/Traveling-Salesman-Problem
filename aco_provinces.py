# -*- coding: utf-8 -*-

"""
İstanbul(0)-Kocaeli(1)-Sakarya(2)-Düzce(3)-Ankara(4)-Yalova(5)-Bursa(6)-
Bilecik(7)-Eskişehir(8)-Kütahya(9)

İstanbul(0)-İstanbul(0):0
İstanbul(0)-Kocaeli(1):113km
İstanbul(0)-Sakarya(2):148km
İstanbul(0)-Düzce(3):216km
İstanbul(0)-Ankara(4):453km           
İstanbul(0)-Yalova(5):178km            
İstanbul(0)-Bursa(6):244km
İstanbul(0)-Bilecik(7):248km
İstanbul(0)-Eskişehir(8):323km
İstanbul(0)-Kütahya(9):354km
------------------------------------------------
Kocaeli(1)-İstanbul(0):113km
Kocaeli(1)-Kocaeli(1):0
Kocaeli(1)-Sakarya(2):37km
Kocaeli(1)-Düzce(3):106km
Kocaeli(1)-Ankara(4):342km
Kocaeli(1)-Yalova(5):65km             
Kocaeli(1)-Bursa(6):131km             
Kocaeli(1)-Bilecik(7):137km
Kocaeli(1)-Eskişehir(8):213km
Kocaeli(1)-Kütahya(9):244km
----------------------------------------------------
Sakarya(2)-İstanbul(0):148km
Sakarya(2)-Kocaeli(1):37km
Sakarya(2)-Sakarya(2):0
Sakarya(2)-Düzce(3):68km
Sakarya(2)-Ankara(4):305km            
Sakarya(2)-Yalova(5):103km            
Sakarya(2)-Bursa(6):157km
Sakarya(2)-Bilecik(7):100km
Sakarya(2)-Eskişehir(8):176km
Sakarya(2)-Kütahya(9):206km
----------------------------------------------------
İstanbul(0)-Kocaeli(1)-Sakarya(2)-Düzce(3)-Ankara(4)-Yalova(5)-Bursa(6)-
Bilecik(7)-Eskişehir(8)-Kütahya(9)
------------------------------------------------------------------------
Düzce(3)-İstanbul(0):216km
Düzce(3)-Kocaeli(1):106km
Düzce(3)-Sakarya(2):68km
Düzce(3)-Düzce(3):0
Düzce(3)-Ankara(4):237km             
Düzce(3)-Yalova(5):171km               
Düzce(3)-Bursa(6):225km
Düzce(3)-Bilecik(7):168km
Düzce(3)-Eskişehir(8):244km
Düzce(3)-Kütahya(9):275km
-------------------------------------
Ankara(4)-istanbul(0):453km
Ankara(4)-Kocaeli(1):342km
Ankara(4)-Sakarya(2):305km
Ankara(4)-Düzce(3):237km
Ankara(4)-Ankara(4):0
Ankara(4)-Yalova(5):407km               
Ankara(4)-Bursa(6):385km                
Ankara(4)-Bilecik(7):314km
Ankara(4)-Eskişehir(8):234km
Ankara(4)-Kütahya(9):312km
---------------------------------------
Yalova(5)-İstanbul(0):178km
Yalova(5)-Kocaeli(1):65km
Yalova(5)-Sakarya(2):103km
Yalova(5)-Düzce(3):171km
Yalova(5)-Ankara(4):407km               
Yalova(5)-Yalova(5):0                   
Yalova(5)-Bursa(6):69km
Yalova(5)-Bilecik(7):124km
Yalova(5)-Eskişehir(8):219km
Yalova(5)-Kütahya(9):250km
--------------------------------------------------------------------------
İstanbul(0)-Kocaeli(1)-Sakarya(2)-Düzce(3)-Ankara(4)-Yalova(5)-Bursa(6)-
Bilecik(7)-Eskişehir(8)-Kütahya(9)
--------------------------------------------------------------------------
Bursa(6)-İstanbul(0):244km
Bursa(6)-Kocaeli(1):131km
Bursa(6)-Sakarya(2):157km
Bursa(6)-Düzce(3):225km
Bursa(6)-Ankara(4):385km
Bursa(6)-Yalova(5):69km                 
Bursa(6)-Bursa(6):0                    
Bursa(6)-Bilecik(7):95km
Bursa(6)-Eskişehir(8):152km
Bursa(6)-Kütahya(9):182km
------------------------------------
Bilecik(7)-İstanbul(0):248km
Bilecik(7)-Kocaeli(1):137km
Bilecik(7)-Sakarya(2):100km
Bilecik(7)-Düzce(3):168km
Bilecik(7)-Ankara(4):314km
Bilecik(7)-Yalova(5):124km              
Bilecik(7)-Bursa(6):95km                 
Bilecik(7)-Bilecik(7):0
Bilecik(7)-Eskişehir(8):80km
Bilecik(7)-Kütahya(9):111km
------------------------------------
Eskişehir(8)-İstanbul(0):323km
Eskişehir(8)-Kocaeli(1):213km
Eskişehir(8)-Sakarya(2):176km
Eskişehir(8)-Düzce(3):244km
Eskişehir(8)-Ankara(4):234km
Eskişehir(8)-Yalova(5):219km             
Eskişehir(8)-Bursa(6):152km               
Eskişehir(8)-Bilecik(7):80km
Eskişehir(8)-Eskişehir(8):0
Eskişehir(8)-Kütahya(9):79km
-------------------------------------
Kütahya(9)-İstanbul(0):354km
Kütahya(9)-Kocaeli(1):244km
Kütahya(9)-Sakarya(2):206km
Kütahya(9)-Düzce(3):275km
Kütahya(9)-Ankara(4):312km
Kütahya(9)-Yalova(5):250km               
Kütahya(9)-Bursa(6):182km                 
Kütahya(9)-Bilecik(7):111km
Kütahya(9)-Eskişehir(8):79km
Kütahya(9)-Kütahya(9):0
------------------------------------
Random routes of 10 ants are given below;

A->0 7	3	4	2	1	9	6	8	5	0

B->0 9	5	4	3	1	8	2	7	6	0

C->0 2	6	9	7	4	8	1	3	5	0

D->0 9	6	5	4	3	2	1	8	7	0

E->0 6	5	4	1	8	2	9	3	7	0

F->0 1	3	2	9	8	7	4	6	5	0

G->0 7	1	8	5	6	9	2	3	4	0

H->0 9	6	5	2	8	4	3	7	1	0

I->0 8	3	1	2	4	6	9	7	5	0

J->0 2	7	5	8	1	3	4	9	6	0












"""
