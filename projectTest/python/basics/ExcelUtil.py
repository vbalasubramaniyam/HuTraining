import csv

import pandas as pd
class ExcelUtil():

    def writer(self,header, data, filename):
        with open(filename, "w", newline="") as csvfile:
            fieldnames = ['Title', 'Cast', 'Director', 'Genre', 'Length', 'Admin_Rating', 'Lang', 'Timing',
                          'No_Of_Shows', 'FirstShow', 'Int_time', 'Gap_Bw_Shows', 'Capacity']
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)


filename = 'MovieDb.csv'
header = ("Title", "Cast", "Director",'Genre')
data=('vino','sam','saa','sss')
vv=ExcelUtil()
vv.writer(header,data,filename)

    #print(df)
#ret=ExcelUtil
#ret.updatemovieDetails(2,'Vijay')


