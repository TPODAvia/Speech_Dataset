import phonemizer
global_phonemizer = phonemizer.backend.EspeakBackend(language='vi', preserve_punctuation=True,  with_stress=True)

def phonemize(global_phonemizer, text):
    return global_phonemizer.phonemize([text])[0]

# Open the file
with open('D:\\Datasets\\vivos\\train\\prompts.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Save the extracted data to a TXT file with the specified format and UTF-8 encoding
with open('vivos_extr.txt', 'w', encoding='utf-8') as output_file:
    for line in lines:
        if line == '\t\n':
            continue
        else:
            parts = line.strip().split('\t')
            id_full = parts[0]
            id_short = id_full.split('_')[0]
            sentence = parts[1]

            # print(id_short, id_full, sentence)
            output_file.write(f"/vivos/train/waves/{id_short}/{id_full}.wav|{phonemize(global_phonemizer, sentence)}|0\n")