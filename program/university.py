# import university_folder_generator
import requests
from bs4 import BeautifulSoup
import pandas as pd

class university:

    def __init__ (self, name, state, id, year):
        self.name = name
        self.state = state
        self.id = id
        self.year = year
        name = name.replace(' ','_')
        name = name.replace('/','^')
        name = name.replace('?','^')
        self.name_id = name + '_' + id

    def gen_url(self):
        self.url = 'https://nces.ed.gov/collegenavigator/?q=&s=all&id=' + str(self.id)
        # name_w_space = self.name
        # name_plus_sign = name_w_space.replace(' ','+')
        # self.url = 'https://nces.ed.gov/collegenavigator/?q=' + name_plus_sign + '&s=all&id=' + str(self.id)

    def gen_path(self):   
        return '../database/' + self.state + '/' + self.name_id + '/' + self.year 

    def gen_csv(self, item, soup):
        # soup to extract a table with ID
        table = soup.select('table')[item.CNid]   
        rows = table.find_all('tr') 
        output = []
        for row in rows:
            cols_all = row.find_all('td') 
            cols = [item.text.strip() for item in cols_all]
            output.append([item for item in cols if item])
        df = pd.DataFrame(output, columns = item.description)   
        df = df.iloc[1:]
        df.head()
        df.shape
        path = self.gen_path()   
        df.to_csv(path + '//' + item.name + '.csv')
        return 

    def save(self):
        import Item
        self.gen_url()
        # get webpage
        data = requests.get(self.url).text 
        # parse by soup
        soup = BeautifulSoup(data, 'html.parser')
        #####
        for element in Item.item: 
            try: 
                self.gen_csv(element, soup)
            except ValueError:
                pass
            except IndexError:
                pass



if __name__ == '__main__':
    college1 = university('University of Portland', 'OR', '209825', '2022')
    college1.save()
    # college2 = university('University of Washington-Seattle Campus', 'WA', '236948', '2022')
    # college2.save()
    # college3 = university('AdventHealth University', 'FL', '133872', '2022')
    # college3.save()