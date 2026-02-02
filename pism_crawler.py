from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

cService = webdriver.ChromeService(executable_path='/usr/bin/chromedriver')
driver = webdriver.Chrome(service = cService)

base_url = "https://processoseletivo.ufjf.br/"

years = ['2024', '2023', '2022', '2021', '2020']

base_end_url1 = "/notaspism1_aposrevisao/"
base_end_url2 = "/notaspism1_aposrevisao__Q/"

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

people = []

for y in years:
    i = 0
    people = []
    for l in letters:
        try:
            url = f'{base_url}{y}{base_end_url1}{l}.html' if y != '2020' else f'{base_url}{y}{base_end_url2}{l}.html'
            driver.get(url)
            time.sleep(1)
            table = driver.find_elements(By.ID, 'example')[0]
            tb = table.find_elements(By.TAG_NAME, 'tbody')[0]
            rows = tb.find_elements(By.TAG_NAME, 'tr')
            for r in rows:
                open_specified_results = r.find_elements(By.TAG_NAME, 'td')[0]
                driver.execute_script("arguments[0].scrollIntoView();", open_specified_results)
                open_specified_results.click()
                
                rows = tb.find_elements(By.TAG_NAME, 'tr')
                specified_results = rows[rows.index(r) + 1]
                
                tr = specified_results.find_elements(By.TAG_NAME, 'tr')

                portg_obj_row = tr[4].text.split()[-1].replace(',', '.')
                maths_obj_row = tr[5].text.split()[-1].replace(',', '.')
                literature_obj_row = tr[6].text.split()[-1].replace(',', '.')
                hist_obj_row = tr[7].text.split()[-1].replace(',', '.')
                geog_obj_row = tr[8].text.split()[-1].replace(',', '.')
                physics_obj_row = tr[9].text.split()[-1].replace(',', '.')
                chemistry_obj_row = tr[10].text.split()[-1].replace(',', '.')
                biology_obj_row = tr[11].text.split()[-1].replace(',', '.')

                portg_dis_row = tr[12].text.split()[-1].replace(',', '.')
                maths_dis_row = tr[13].text.split()[-1].replace(',', '.')
                literature_dis_row = tr[14].text.split()[-1].replace(',', '.') 
                hist_dis_row = tr[15].text.split()[-1].replace(',', '.')
                geog_dis_row = tr[16].text.split()[-1].replace(',', '.')
                physics_dis_row = tr[17].text.split()[-1].replace(',', '.')
                chemistry_dis_row = tr[18].text.split()[-1].replace(',', '.')
                biology_dis_row = tr[19].text.split()[-1].replace(',', '.') 
                
                name = r.find_elements(By.TAG_NAME, 'td')[1].text
                score = float(r.find_elements(By.TAG_NAME, 'td')[3].text.replace(',', '.'))
                people.append([name, score, 
                portg_obj_row, maths_obj_row, literature_obj_row, 
                hist_obj_row, geog_obj_row, physics_obj_row, 
                chemistry_obj_row, biology_obj_row,
                portg_dis_row, maths_dis_row, literature_dis_row,
                hist_dis_row, geog_dis_row, physics_dis_row,
                chemistry_dis_row, biology_dis_row])
                i += 1
                print(f'Year {y}, student {i}')
                open_specified_results.click()
        except:
            print(f'Couldn\'t resolve letter {l} in {y}')

    people.sort(key=lambda x: x[1])
    people = list(reversed(people))

    with open(f'var/raw_results/results{y}.txt', 'w+') as f:
        for n in range(len(people)):
            f.write(f'{n + 1} {people[n][0]} {people[n][1]} {people[n][2]} {people[n][3]} {people[n][4]} {people[n][5]} {people[n][6]} {people[n][7]} {people[n][8]} {people[n][9]} {people[n][10]} {people[n][11]} {people[n][12]} {people[n][13]} {people[n][14]} {people[n][15]} {people[n][16]} {people[n][17]}\n')
        f.close()
