import os
import torchaudio
import soundfile as sf 
from tqdm import tqdm
from praatio import tgio

vowel_labels = {"see", "soo", "sahh", "so", "set"}

# update to full location
audio_folder = r"R:\Speech and Craniofacial analysis\"
annotation_folder = r"R:\Speech and Craniofacial analysis\"
output_folder = r"R:\Speech and Craniofacial analysis\"

os.makedirs(output_folder, exist_ok=True)

for filename_tg in tqdm(os.listdir(annotation_folder)):
        filename = os.path.splitext(filename_tg)[0]
        
        tg_path = os.path.join(annotation_folder, filename_tg) # annotation/filename.TextGrid
        wav_path = os.path.join(audio_folder, filename + ".wav") # audio/filename.wav

        waveform, sample_rate = torchaudio.load(wav_path)
        # not sure if necessary
        if waveform.shape[0] > 1:
            waveform = waveform.mean(dim=0)  # convert to mono
        waveform = waveform.squeeze().numpy()

        filename_tg = tgio.openTextgrid(tg_path)
        tg = tgio.openTextgrid(tg_path)
        tiername = tg.tierNameList[0]
        tier = tg.tierDict[tiername]

        i = 0
        for start, end, label in tier.entryList:
            label_clean = label.strip().lower().replace("/", "").replace("-f", "")
            
            if label_clean in vowel_labels:
                start_sample = int(start * sample_rate)
                end_sample = int(end * sample_rate)
                segment_audio = waveform[start_sample:end_sample]

                out_filename = f"{filename}_Seg{i}_{label_clean}_f.wav"
                out_path = os.path.join(output_folder, out_filename)

                sf.write(out_path, segment_audio, sample_rate)
                i += 1
