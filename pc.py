import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import os



def BoyerMoore(pattern, text):
    m = len(pattern)
    n = len(text)
    if m > n:
        return -1
    skip = []
    for k in range(256):
        skip.append(m)
    #  CONSTRUCT BAD-MATCH TABLE
    for k in range(m - 1):
        skip[ord(pattern[k])] = m - k - 1
    skip = tuple(skip)
    k = m - 1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            return i + 1
        k += skip[ord(text[k])]
    return -1

def LevenshteinD(doc1, doc2):  # *dynamic programing solution*
    m = len(doc1.split(" "))# tokenize the document
    n = len(doc2.split(" "))
    p = m + n   #lenght of thw two document combined
    table = [[0] * (n + 1)
    for _ in range(m + 1)]
    for i in range(m + 1):
        table[i][0] = i
    for j in range(n + 1):
        table[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if doc1.split(" ")[i - 1] == doc2.split(" ")[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
    plagiarism_percentage = ((2 * p) / (len(doc1) + len(doc2))) * 100
    print("LevenshteinD PLAGIARISM PERCENTAGE: " + str(plagiarism_percentage) + " %")
    print("diffence :   ", table[-1][-1])
    print("similarity : ", (2 * table[-1][-1]) - p )

def tryLD(a,b):
    try:
        LevenshteinD(a,b)
    except:
        print("Empty Tables")


#create the root canvas
root = tk.Tk()
#create the window canvas ditals
frame = tk.Frame(root, bg="white")
# window title
root.title("plagirizim checker")
# state the space of the box in the root canvas
frame.place(relwidth=2, relheight=2, relx=1, rely=1)
# #entry fields
# entry_field = tk.Text()
# entry_field.grid
#definelables
l1 = Label(root, text="document 1")
l1.grid(row=4, column=0)
l2 = Label(root, text="document 2")
l2.grid(row=4, column=2)
#
#text box
e1=Text(master=root, height=20, width=38)
e1.grid(row=9,column=0)
e2=Text(master=root, height=20, width=38)
e2.grid(row=9,column=2)

text_entry1 = e1.get("1.0","end-1c")
text_entry2 = e2.get("1.0","end-1c")
document1 = text_entry1
document2 = text_entry2
#
# text_entry1 = e1.get()
# text_entry2 = e2.get()
# document1 = text_entry1
# document2 = text_entry2
#definelables for list box
l3 = Label(root, text="BoyerMoore algo")
l3.grid(row=1, column=0)
l4 = Label(root, text="LevenshteinD algo")
l4.grid(row=1, column=2)
# l5 = Label(root, text="algo3")
# l5.grid(row=1, column=2)
#define ListBox algo result list
list1=Listbox(root, height=0)
list1.grid(row=2,column=0,columnspan=1 )
#list1.insert(tk.END, LevenshteinD.plagiarism_percentage)
list2=Listbox(root, height=0)
list2.grid(row=2,column=2,columnspan=1 )
#list2.insert(tk.END, BoyerMoore.plagiarism_percentage)
# list3=Listbox(root, height=0)
# list3.grid(row=2,column=2,columnspan=1 )
#Define buttons
b1=Button(root,text="check BoyerMoore", width=18, bg="#9ACD32", command=lambda: print(BoyerMoore(e1.get("1.0","end-1c"),e2.get("1.0","end-1c"))) )
b1.grid(row=20,column=0)
b2=Button(root,text="check LevenshteinD", width=18, bg="#9ACD32", command=lambda: tryLD(e1.get("1.0","end-1c"), e2.get("1.0","end-1c")))
b2.grid(row=20,column=2)
root.mainloop()
