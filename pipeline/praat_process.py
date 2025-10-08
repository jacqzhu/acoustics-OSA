import os
import pandas as pd

segment_folder = r"R:\Speech and Craniofacial analysis\Collected Data\UMich Data\May_14_2025\Jacqueline\0514_segment"
output_folder = r"R:\Speech and Craniofacial analysis\Collected Data\UMich Data\May_14_2025\Jacqueline"

data = []

for filename in os.listdir(segment_folder):
        path = os.path.join(segment_folder, filename)
        data.append({"Location": path})

df = pd.DataFrame(data)

output_path = os.path.join(output_folder, "May14_location.xlsx")
df.to_excel(output_path, index=False)