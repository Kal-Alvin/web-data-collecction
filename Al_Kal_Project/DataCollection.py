import os, csv, bs4, requests, texttable
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter


class CleanData:
    def __init__(self, site):
        # CONSTRUCTOR FOR THE SITE URL
        self.site = site

    def webdata(self):
        try:
            res = requests.get(self.site)
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, "html.parser")
            data = []
            # GET THE SPECIFIC TABLE CLASS TO SCRAP
            table = soup.find('table', attrs={'class': 'wikitable sortable'})
            table_body = table.find('tbody')
            header = table.findAll('th')
            headers = [th.text for th in header[:-2]]

            rows = table_body.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                # ELIMINATE THE NON NEEDE RECORD FROM THE ARRY BY USING LIST COMPREHENSION
                cols = [ele.text.strip() for ele in cols[:-2]]
                data.append([ele for ele in cols if ele])
                # ADDING THE HEADER TO THE FIRST ELEMENT IN THE ARRAY
                data[0] = headers
            return data
        except Exception as e:
            print(e.args)


    # DISPLAY IN TABLE FORM
    def displayDataInTable(self):
        try:
            data = self.webdata()
            headers = data[0]
            cells = (data[1:])
            table = texttable.Texttable()
            table.header(headers)
            for cell in cells:
                table.add_row(cell)
            retval = table.draw()
            return retval
        except Exception as e:
            print(e.args)

    def displayDataInCSV(self):
        try:
            if (self.webdata()):
                fileLocation = os.path.join(os.getcwd() + 'csvFile.csv')
                data = self.webdata()
                headers = data[0]
                # REMOVE RECORD FROM THE ARRAY
                headers.pop(6)
                cell = (data[1:])
                arr = np.array(cell)
                # DELETE UNWANTED COLUMN FROM THE RECORD
                cells = np.delete(arr, 6, axis=1)
                # TURN THR NON 2018 COLUMNS TO ZEROS AS INDICATED IN THE INSTRUCTIONS
                cells[:, 3] = 0
                cells[:, 4] = 0
                sort = self.sortData(cells)
                # REMOVE UNNECESSARY NUMPY ARRAY ENTRIES

                x = [list(i) for i in sort]

                sortarray = np.array(x)
                # print(sortarray)
                # SAVE TO CSV FILE
                with open(fileLocation, 'w') as csvfile:
                    csvwriter = csv.writer(csvfile)
                    csvwriter.writerow(headers)
                    csvwriter.writerows(sortarray)
                    print(fileLocation, 'SUCCESSFUL')
                return sortarray
        except Exception as e:
            print(e.args)

    def sortData(self, data):
        try:
            return sorted(data, key=itemgetter(7))
        except Exception as e:
            print(e.args)

    def drowChart(self):
        try:
            # DISPLAY SORTED DATA IN THE CHART
            data = self.displayDataInCSV()
            countries = [i[0] for i in data]
            sdata = [i[len(i)-1] for i in data]

            # MAKE SURE LENGTH LEFT, HEIGHT AND TICK_LABEL ARE THE SAME TO AVOID ANY ERROR
            left = [i for i in range(0, 145, 5)]
            plt.bar(left, height=sdata, tick_label=countries, width=0.8, color=['blue', 'green'])
            # DISPLAY BAR CHART
            plt.show()
        except Exception as e:
            print(e.args)



site = 'https://en.wikipedia.org/wiki/Road_safety_in_Europe#cite_note-25'
data = CleanData(site)
data.drowChart()
