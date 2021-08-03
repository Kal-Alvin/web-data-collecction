# web-data-collecction

I have created a class called CleanData
Language used PYTHON
LIBRARIES used:
  os, csv, bs4, requests, texttable(working but jus for test), numpy, 
  metplotlib, and operator
 
 A constructor used for the site url
 Function:
  wedata{
        gets data from the website and spoof the needed parts which is the table
        and returns the rows, columns, and header
        }
   displayDataInTable{
        which uses the library "texttable" not part of the instruction but good to try
        for test
        }
   displayDataInCSV{
        checks data coming from "webdata"
        creates csv file, sort it then does the necessary modifications to the data 
        then save it to .csv file
    sortData{
        does the sorting of the data
         }
     drowChart{
          drows the bar chart by using countries from the spoof recors and the Road deaths 
          as indicated
          }
          
![chart](https://user-images.githubusercontent.com/88352811/127938188-6ed5ad9b-3cdc-400d-afae-eeb1b9e68994.PNG)
  

