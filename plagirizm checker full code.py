import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import os
root = tk.Tk()
plagiarism_percentageBM =0;
plagiarism_percentageLD =0;
def LevenshteinD(doc1, doc2):  # *dynamic programing solution*

    m = len(doc1)  # tokenize the document
    n = len(doc2)

    p = m + n  # lenght of thw two document combined
    table = [[0] * (n + 1)
    for _ in range(m + 1)]
    for i in range(m + 1):
        table[i][0] = i
    for j in range(n + 1):
        table[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if doc1[i - 1] == doc2[j - 1]:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = 1 + min(table[i - 1][j], table[i][j - 1], table[i - 1][j - 1])
                #print(table[i][j])
    # h = plagiarism_percentage
    global plagiarism_percentageLD
    h = n - (table[-1][-1])
    plagiarism_percentageLD = ((2 * (h) ) / (len(doc1) + len(doc2))) * 100
    print("LevenshteinD PLAGIARISM PERCENTAGE: " + str(plagiarism_percentageLD) + " %")
    print("diffence :   ", table[-1][-1])
   # h = p - (table[-1][-1])
    print("similarity : ", h)

    #   SPLIT TEXT DOCUMENT IN word AND APPEND TO ARRAY
    final1 = []
    for i in doc1.split():
        t = i.split()
        for i in t:
            final1.append(i)

    for i in range(0, final1.count("\n")):
        final1.remove("\n")
    for i in range(0, final1.count("\n")):
        final1.remove("\n")

    final2 = []
    for i in doc2.split():
        t = i.split()
        for i in t:
            final2.append(i)

    for i in range(0, final2.count("\n")):
        final2.remove("\n")
    for i in range(0, final2.count("\n")):
        final2.remove("\n")

    def BoyerMoore(pattern, text):
        m = len(pattern)
        n = len(text)
        p = m + n
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

    #  COUNT NUMBER OF MATCHES
    matches = -0
    doc2_joined = ".".join(doc2)
    for y in doc1:
        match = 0
        match = (BoyerMoore(y, doc2_joined))
        if match > - 1:
            matches = matches + 1

    #  CALCULATE PLAGIARISM PERCENTAGE
    global plagiarism_percentageBM
    d = n - matches
    plagiarism_percentageBM = ((2 * (matches)  ) / (len(doc1) + len(doc2))) * 100
    print("BoyerMoore PLAGIARISM PERCENTAGE: " + str(plagiarism_percentageBM) + " %")
    print("diffence :   ", d)
    print("similarity: " + str(matches))

def tryLD(a, b):
    try:
        LevenshteinD(a, b)
        # list1[0] = plagiarism_percentageLD
        # print(list1, list2)
        #if list1.index("end") != 0:
        list1.delete(0, "end")
        list1.insert(0, plagiarism_percentageLD)

        # list1.insert(tk.END, LevenshteinD.plagiarism_percentage)

        #if list2.index("end") != 0:
        list2.delete(0, 'end')
        list2.insert(0, plagiarism_percentageBM)
    except:
        print("Empty Tables")

def tryBM(a, b):
    try:
        BoyerMoore(a, b)
    except:
        print("Empty Tables")

#print(plagiarism_percentageLD, "hhhh", plagiarism_percentageBM)
# create the root canvas
# root = tk.Tk()
# create the window canvas ditals
frame = tk.Frame(root, bg="blue")

# window title
root.title("plagirizim checker")
# state the space of the box in the root canvas
root.geometry("640x450")
frame.place(relwidth=2, relheight=2, relx=1, rely=1)
# definelables
t1 = Label(root, text="o")
t1.grid(row=4, column=0)
l1 = Label(root, text="document 1")
l1.grid(row=4, column=1)
l2 = Label(root, text="document 2")
l2.grid(row=4, column=2)
t2 = Label(root, text="o")
t2.grid(row=4, column=3)
#
# text box
e1 = Text(master=root, height=20, width=38)
e1.grid(row=9, column=1)
e2 = Text(master=root, height=20, width=38)
e2.grid(row=9, column=2)

text_entry1 = e1.get("1.0", "end-1c")
text_entry2 = e2.get("1.0", "end-1c")
document1 = text_entry1
document2 = text_entry2
#

# definelables for list box
l3 = Label(root, text="LevenshteinD algo")
l3.grid(row=1, column=1)
l4 = Label(root, text="BoyerMoore algo")
l4.grid(row=1, column=2)

# # define ListBox algo result list
list1 = Listbox(root, height=0)
list1.grid(row=2, column=1, columnspan=1)
# list1.insert(0, plagiarism_percentageLD)
#
# # list1.insert(tk.END, LevenshteinD.plagiarism_percentage)
list2 = Listbox(root, height=0)
list2.grid(row=2, column=2, columnspan=1)
# list2.insert(0, plagiarism_percentageBM)

# Define buttons
# b1 = Button(root, text="check BoyerMoore", width=18, bg="#9ACD32",
#             command=lambda: tryBM(e1.get("1.0", "end-1c"), e2.get("1.0", "end-1c")))
# b1.grid(row=20, column=0)
b2 = Button(root, text="CHECK PLAGIARISM %", width=18, bg="#9ACD32",
            command=lambda: tryLD(e1.get("1.0", "end-1c"), e2.get("1.0", "end-1c")))
b2.grid(row=11, column=2)
root.mainloop()