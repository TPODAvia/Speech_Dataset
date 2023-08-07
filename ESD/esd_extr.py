import phonemizer
global_phonemizer = phonemizer.backend.EspeakBackend(language='en-us', preserve_punctuation=True,  with_stress=True)

def phonemize(global_phonemizer, text):
    return global_phonemizer.phonemize([text])[0]

# Open the file
with open('D:\\Datasets\\ESD\\0017\\0017.txt', 'r', encoding='utf-8') as f: # utf-16le or utf-8
    lines = f.readlines()

# Save the extracted data to a TXT file with the specified format and UTF-8 encoding
with open('esd_extr_17.txt', 'w', encoding='utf-8') as output_file:
    for line in lines:
        if line == '\t\n' or line == '\n':
            continue
        else:
            parts = line.strip().split('\t')
            id_full = parts[0]
            id_short = id_full.split('_')[0]
            sentence = parts[1]
            sentiment = parts[2]
            # print(id_short, id_full, sentence, sentiment)
            output_file.write(f"/ESD/{id_short}/{sentiment}/train/{id_full}.wav|{phonemize(global_phonemizer, sentence)}|0\n")