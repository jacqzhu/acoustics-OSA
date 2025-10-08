import os
import pandas as pd

excel_path = r"R:\Speech and Craniofacial analysis\Codes\AcousticAnalyses\Jacqueline\AcousticFeatures_April16.xlsx"
df = pd.read_excel(excel_path)

def extract_base_filename(path):
    filename = os.path.basename(path)
    base = filename.split('_Seg')[0] + '.wav'
    
    return base

def extract_vowel(location):
    filename = os.path.basename(location)
    parts = filename.split('_')
    if len(parts) >= 5:
        return parts[3]
    return ''

df['Video_File'] = df['Location'].apply(extract_base_filename)
df['vowel'] = df['Location'].apply(extract_vowel)

output_path = r"R:\Speech and Craniofacial analysis\Codes\AcousticAnalyses\Jacqueline\AcousticFeatures_April16_UPDATED.xlsx"
df.to_excel(output_path, index=False)

print(f"Updated Excel saved to: {output_path}")