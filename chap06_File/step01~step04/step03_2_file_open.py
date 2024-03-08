# -*- coding: utf-8 -*-

from tkinter.filedialog import askopenfilename


readFile = askopenfilename() # 파일 탐색기 제공 

if readFile != None:
    infile = open(readFile, "r") # file 객체 생성

# text file 내용 출력
for line in infile.readlines():
    line = line.strip()
    print(line)
    
infile.close() # 파일 객체 닫기