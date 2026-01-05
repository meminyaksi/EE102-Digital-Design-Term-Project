def compare_txt_files(file1_path, file2_path):
    with open(file1_path, 'r', encoding='utf-8') as f1, open(file2_path, 'r', encoding='utf-8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    max_lines = max(len(lines1), len(lines2))
    differences = []

    for i in range(max_lines):
        line1 = lines1[i].strip() if i < len(lines1) else "<BOŞ SATIR>"
        line2 = lines2[i].strip() if i < len(lines2) else "<BOŞ SATIR>"

        if line1 != line2:
            differences.append(f"Satır {i+1}:\n  Dosya1: {line1}\n  Dosya2: {line2}\n")

    if differences:
        print("Eşleşmeyen Satırlar:")
        for diff in differences:
            print(diff)
    else:
        print("Tüm satırlar eşleşiyor.")

# Örnek kullanım
compare_txt_files('stimulus.txt', 'githubtest.txt')
