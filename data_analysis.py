import pandas as pd
import matplotlib.pyplot as plt
from textwrap import wrap

#charts.xlsx is an example input file
user_response_file = 'charts.xlsx'
data = pd.read_excel(user_response_file)


def single_choice_counter(sheet, column):

    working_set = sheet[column].fillna(0) 

    #check and adjust if N/A values present
    if 0 not in working_set.values:
       masterlist = working_set.value_counts()
    else:
       masterlist = working_set.value_counts().drop(labels=0)
    #Plot configuration for pie chart
    plt.ioff()
    plt.figure(figsize = (7, 8), dpi = 600) #7" x 7" to fit all text
    labels = [ '\n'.join(wrap(l, 12)) for l in list(masterlist.index) ]
    plt.pie(masterlist, 
            labels=labels, 
            autopct='%.2f%%',
            startangle=90,
            wedgeprops={'linewidth': 1, 'linestyle': 'solid', 'antialiased': True,"edgecolor":"k"})
    plt.axis('equal')
    plt.xlabel(column)
    plt.savefig(column + '.png')


def multiple_choice_counter(sheet, column):

    #to be used for fields that have multiple answers per record
    input_set = sheet[column].fillna(0) #fillna(0) sets the unavailable values to 0
    working_set = [i for i in input_set if i != 0]
    masterlist = {}
    for i in working_set:
        for j in i.split(', '):
            if j in masterlist:
                masterlist[j] += 1
            else:
                masterlist[j] = 1
    
    #Plot configuration for bar chart
    plt.ioff()
    labels = [ '\n'.join(wrap(l, 12)) for l in list(masterlist.keys()) ]
    plt.figure(figsize = (7, 7), dpi = 600) #7" x 7" to fit all text
    plt.bar(range(len(masterlist)),
            masterlist.values(),
            align = 'center',
            ec = 'black');
    plt.xticks(range(len(masterlist)), labels)
    for i,v in enumerate(masterlist.values()): #to add the values on the bars
        plt.text(i, v+1.5, str(v), color='black', fontweight='bold')
    plt.xlabel("Item")
    plt.ylabel("No. of people")
    plt.savefig(column + ".png")
    return masterlist

print("Select if single choice answer or multiple choice for the following. S for single M for multiple and K for skip")
for columns in data.columns:
    method_needed = input("\n" + columns + " - ")
    if (method_needed == "s"):
        single_choice_counter(data,columns)
    elif (method_needed == "m"):
        multiple_choice_counter(data,columns)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
