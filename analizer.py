import time
import os

# Renkler
G, Y, R, B, W = '\033[92m', '\033[93m', '\033[91m', '\033[94m', '\033[0m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading(text):
    print(f"{B}{text.ljust(35)}{W}", end="")
    for _ in range(12):
        time.sleep(0.04)
        print(f"{G}█{W}", end="", flush=True)
    print(" [ OK ]")

def input_check(prompt, min_val, max_val):
    while True:
        try:
            entry = input(f"{Y}{prompt}{W}").strip()
            val = int(entry)
            if min_val <= val <= max_val:
                return val
            print(f"{R} Geçersiz! {min_val}-{max_val} arası bir sayı girin.{W}")
        except ValueError:
            print(f"{R} Hata! Lütfen harf değil, sadece sayı kullanın.{W}")

def main():
    clear()
    print(f"{Y}1- Türkçe | 2- English{W}")
    lang_choice = input_check(" Seçim / Choice: ", 1, 2)
    tr = lang_choice == 1
    
    # DİL SÖZLÜĞÜ - TİTİZLİKLE DÜZENLENDİ
    d = {
        'title': '🚀 SİSTEM FPS ANALİZÖRÜ v7.0' if tr else '🚀 SYSTEM FPS ANALIZER v7.0',
        'cpu_b': '[1] CPU MARKASI:' if tr else '[1] CPU BRAND:',
        'gpu_b': '[2] GPU MARKASI:' if tr else '[2] GPU BRAND:',
        'ram': '[3] RAM KAPASİTESİ:' if tr else '[3] RAM CAPACITY:',
        'disk': '[4] DEPOLAMA BİRİMİ:' if tr else '[4] STORAGE UNIT:',
        'cool': '[5] SOĞUTMA SİSTEMİ:' if tr else '[5] COOLING SYSTEM:',
        'cat': '[6] GRAFİK KATEGORİSİ:' if tr else '[6] GRAPHIC CATEGORY:',
        'choice': ' Seçiminiz: ' if tr else ' Your Choice: ',
        'loading': 'Sistem Analiz Ediliyor...' if tr else 'Analyzing System...',
        'res_title': 'PERFORMANS RAPORU' if tr else 'PERFORMANCE REPORT',
        'status_lbl': '📊 Durum' if tr else '📊 Status',
        'fps_lbl': '🚀 Tahmini FPS' if tr else '🚀 Estimated FPS',
        'game_label': '🎮 Grafik Türü' if tr else '🎮 Graphics Type',
        'st_bad': 'OYNANAMAZ (KASAR)' if tr else 'UNPLAYABLE (LAGGY)',
        'st_mid': 'OYNANABİLİR (ORTA)' if tr else 'PLAYABLE (MID)',
        'st_good': 'KUSURSUZ (AKICI)' if tr else 'PERFECT (SMOOTH)'
    }

    clear()
    print(f"{Y}===================================================={W}")
    print(f"{G}    {d['title']}       {W}")
    print(f"{Y}          Developer: Emir & Gemini                  {W}")
    print(f"{Y}===================================================={W}\n")

    # 1. CPU
    print(f"{B}{d['cpu_b']}{W} 1- Intel | 2- AMD")
    cpu_br = input_check(d['choice'], 1, 2)
    if cpu_br == 1:
        print(f"\n{B}Intel Model:{W} 1- Core i3 | 2- Core i5 | 3- Core i7")
    else:
        print(f"\n{B}AMD Model:{W} 1- Ryzen 3 | 2- Ryzen 5 | 3- Ryzen 7")
    cpu_model = input_check(d['choice'], 1, 3)

    # 2. GPU
    print(f"\n{B}{d['gpu_b']}{W} 1- NVIDIA | 2- AMD | 3- Intel (Dahili)")
    gpu_br = input_check(d['choice'], 1, 3)
    gpu_pow = 0
    if gpu_br == 1:
        print(f"\n{B}NVIDIA:{W} 1- GTX | 2- RTX 30 | 3- RTX 40")
        gpu_pow = input_check(d['choice'], 1, 3)
    elif gpu_br == 2:
        print(f"\n{B}AMD RX:{W} 1- RX 5000 | 2- RX 6000 | 3- RX 7000")
        gpu_pow = input_check(d['choice'], 1, 3)

    # 3. RAM & DISK & COOL
    ram = input_check(f"\n{B}{d['ram']}{W} 1- 4GB | 2- 8GB | 3- 16GB | 4- 32GB\n{d['choice']}", 1, 4)
    print(f"\n{B}{d['disk']}{W} 1- HDD | 2- SATA SSD | 3- NVMe SSD")
    disk_idx = input_check(d['choice'], 1, 3)
    cool_idx = input_check(f"\n{B}{d['cool']}{W} 1- Stok | 2- Hava | 3- Sıvı\n{d['choice']}", 1, 3)

    # 4. YENİ KATEGORİ SİSTEMİ
    print(f"\n{B}{d['cat']}{W}")
    if tr:
        print(" 1- Piksel Grafikli | 2- 2 Boyutlu | 3- 3D Hafif | 4- 3D Orta | 5- 3D Ağır")
    else:
        print(" 1- Pixel Graphics | 2- 2D Graphics | 3- 3D Light | 4- 3D Medium | 5- 3D Heavy")
    cat_idx = input_check(d['choice'], 1, 5)

    # Kategorilere göre zorluk çarpanları
    categories_tr = ["Piksel Grafikli", "2 Boyutlu", "3D Hafif", "3D Orta", "3D Ağır"]
    categories_en = ["Pixel Graphics", "2D Graphics", "3D Light", "3D Medium", "3D Heavy"]
    diffs = [0.2, 0.4, 0.7, 1.2, 2.5]
    
    current_cat = categories_tr[cat_idx-1] if tr else categories_en[cat_idx-1]
    current_diff = diffs[cat_idx-1]

    clear()
    loading(d['loading'])

    # Hesaplama Motoru
    c_p = [40, 75, 100][cpu_model-1]
    g_p = [20, 55, 95, 135][gpu_pow]
    r_p = [30, 60, 95, 115][ram-1]
    disk_m = [0.9, 1.0, 1.05][disk_idx-1]
    cool_m = [0.85, 1.0, 1.1][cool_idx-1]

    power = (g_p * 0.5 + c_p * 0.3 + r_p * 0.2) * cool_m * disk_m
    final_fps = int((power / current_diff) * 1.2)

    # SONUÇ EKRANI
    print(f"\n{Y}===================================================={W}")
    print(f"{G}             {d['res_title']}           {W}")
    print(f"{Y}===================================================={W}")
    print(f"{d['game_label'].ljust(25)} : {B}{current_cat}{W}")
    print(f"{d['fps_lbl'].ljust(25)} : {G if final_fps >= 60 else (Y if final_fps >= 30 else R)}{final_fps} FPS{W}")
    
    st_msg = d['st_good'] if final_fps >= 60 else (d['st_mid'] if final_fps >= 30 else d['st_bad'])
    print(f"{d['status_lbl'].ljust(25)} : {st_msg}")
    print(f"{Y}===================================================={W}")

if __name__ == "__main__":
    main()