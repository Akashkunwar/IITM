import pandas as pd
import sys
import matplotlib.pyplot as plt


df =  pd.read_csv("MAD 1\Week 3 Lab Assignment\data.csv")


try:
    get = sys.argv[1]
    inp = sys.argv[2]
    inp = int(inp)
except:
    pass

if get == '-s':
    htm1 = '''<!DOCTYPE html>
    <html>
    <head>
        <title>Academics</title>
    </head>
    <body>

            <h1>Student Details</h1>
            
            <table border="1">
                <tr>
                    <th>Subject id</th>
                    <th>Course id</th>
                    <th>Marks</th>
                </tr>
    '''

    htm2 = '''        </table>
    </body>
    </html>
    '''
    df = df[df['Student id'] == inp]
    rep = len(df)
    for x in range(rep):
        row = list(df.iloc[x])
        htm1=htm1+'<tr>'
        for y in row:
            htm1 = htm1+'<td>'+str(y)+'</td>'
        htm1 = htm1+'</tr>'

    tot = (df[' Marks'].sum())


    htm1 = htm1+f'<tr> <td colspan="2">Total Marks</td> <td>{tot}</td> </tr>'
    htm = htm1+htm2


    file_name = "result.html"

    with open(file_name, "w") as file:
        file.write(htm)
elif get == '-c':
    df = df[df[' Course id'] == inp]

    htm1 = '''<!DOCTYPE html>
        <html>
        <head>
            <title>Academics</title>
        </head>
        <body>

                <h1>Course Details</h1>
                
                <table border="1">
                    <tr>
                        <th>Average Marks</th>
                        <th>Maximum Marks</th>
                    </tr>
        '''
    mean = df[' Marks'].mean()
    large = mean = df[' Marks'].max()
    htm1+=f'<tr><td>{str(mean)}</td><td>{str(large)}<td></tr>'
    
    plt.hist(df[' Marks'])
    plt.savefig('hist.png')
    htm1+='</table><img src = "hist.png"></body></html>'

    file_name = "result.html"

    with open(file_name, "w") as file:
        file.write(htm1)
else:
    htm1 = '''<!DOCTYPE html>
        <html>
        <head>
            <title>Wrong Input</title>
        </head>
        <body>

                <h1>Wrong Input</h1>
                <p>Something went wrong</p></body></html>
        '''
    file_name = "result.html"

    with open(file_name, "w") as file:
        file.write(htm1)