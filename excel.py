import os
import openpyxl as px
book = px.load_workbook('preprocess(train).xlsx', data_only=True)
now = book.active


row = now.max_row
print("START")
for i in range(2, row):
    dir_id = 'P' + str(i)
    file_id = 'L' + str(i)
    sent_id = 'D' + str(i)

    if not now[dir_id].value:
        continue
    
    else:
        directory = "sentence/" + now[dir_id].value
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        filenames = "train" + now[file_id].value + ".txt"
        f = open(directory + "/" + filenames, 'w')
        f.write(now[sent_id].value)
        f.close()
print("complete.")
