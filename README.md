I have created a class called CleanData Language used PYTHON LIBRARIES used: os, csv, bs4, 
requests, texttable(working but jus for test), numpy, metplotlib, and operator

A constructor used for the site url 
Function: 

  wedata{ 
        gets data from the website and spoof the needed 
        parts which is the table and returns the rows, columns, and header 
        } 
        
  displayDataInTable{ 
        which uses the library "texttable" not part of the instruction but good to try for test 
        }
        
  displayDataInCSV{ 
        checks data coming from "webdata" creates csv file, sort it then does the necessary
        modifications to the data then save it to .csv file.
        the paces you see Zero as indicated in the instruction on 2018. Any non 2018 data is replaced 
        with 0. I could have used "N/A" Though. In that case you use 
        cells[:, 3] = 'N/A'
        cells[:, 4] = 'N/A' instead 
        }
        
   sortData{ 
        does the sorting of the data 
        } 
        
  drowChart{ 
        All the used libraties are in the venv, you shouldn't have any issue running straight by pointing your 
        python interpreter to it.
        The CSV file is saved as "csvFile.csv" from where you are running from
        and you something like this:  "Full paht\Al_Kal_ProjectcsvFile.csv SUCCESSFUL" and it needs 
        internet connection to spoof the data from the wesite.
        drows the bar chart by using countries from the spoof recors and the Road deaths as indicated 
        }
        
    THE UPDATED VERSION OPENS THE CSV FILE AUTOMATICALLY
