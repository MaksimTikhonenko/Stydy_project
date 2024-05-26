import csv
from datetime import datetime, date, time, timedelta

dt = datetime.now()  # Дата на данний момент
print(dt)

with open('csv_file.csv', newline='') as file:  #todo Створити та відкрити csv file
    pass

# todo виписати всі змінні які мають дату
# todo порівняти всі змінні з поточною датою, та виписати ті товари у яких закінчується
#  строк придатності через тиждень або раніше
# todo створити файл у який запишуться результати нашої програми