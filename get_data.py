import os
from csv import DictReader, DictWriter

# Batch Information
path_to_texas_aggie_files = "/Volumes/digital_project_management/Texas Aggie"
batch_folder = "Batch 3 Scans"
final_csv_name = "texas_aggie_batch_data_new_3.csv"
batch_title = "texas_aggie_batch_3"


all_directories = []
for path, dirs, files in os.walk(f"{path_to_texas_aggie_files}/{batch_folder}"):
    for dir in dirs:
        all_directories.append(dir)

new_data = []
with open("texas_aggie_batch_data.csv", 'r') as og_data:
    reader = DictReader(og_data)
    for row in reader:
        current_id = f"texasaggie_{row.get('Date published')}"
        if current_id in all_directories:
            volume = row.get('Enumeration').split(':')[0].split('.')[-1]
            issue = row.get('Enumeration').split(':')[1].split('.')[-1]
            dir_path = f"/Volumes/digital_project_management/Texas Aggie/{batch_folder}/{current_id}/"
            pages = sum(
                os.path.isfile(os.path.join(dir_path, f)) for f in os.listdir(dir_path)
            )
            date = row.get('Date published')
            if len(date.split('-')) < 3:
                date = f"{date}-01"
            item = {
                "item": f"texasaggie_{row.get('Date published')}",
                "title": f"Texas Aggie. Vol. {volume}, No.{issue}",
                "description": f"The {row.get('Date published')} issue (Vol. {volume}, No. {issue}) of the Texas Aggie.; {pages} pages",
                "date": date,
                "volume": volume,
                "issue": issue,
                "edition": "1",
                "pages": pages,
                "ONI-ChronAm_Batch": batch_title
            }
            new_data.append(item)

with open(final_csv_name, 'w') as new_sheet:
    writer = DictWriter(new_sheet, fieldnames=new_data[0].keys())
    writer.writeheader()
    writer.writerows(new_data)
