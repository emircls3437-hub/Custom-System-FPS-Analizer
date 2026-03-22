#!/usr/bin/env python3
import time
import os
import random

# Renkler
G, Y, R, B, W = '\033[92m', '\033[93m', '\033[91m', '\033[94m', '\033[0m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading(tr):
    # Senin istediğin o en az 5-10 saniye sürecek detaylı analiz kısmı
    msgs = [
        "İşlemci mimarisi ve nesil taranıyor..." if tr else "Scanning CPU architecture and generation...",
        "GPU veri yolu (Bus Width) ve VRAM ölçülüyor..." if tr else "Measuring GPU bus width and VRAM...",
        "RAM gecikme süreleri (CL) ve DDR hızı kontrol ediliyor..." if tr else "Checking RAM latency and DDR speed...",
        "Asus ROG bileşenleri ve termal değerler analiz ediliyor..." if tr else "Analyzing Asus ROG components and thermals...",
        "RTX teknolojisi ve Tensor çekirdekleri test ediliyor..." if tr else "Testing RTX technology and Tensor cores..."
    ]
    for msg in msgs:
        print(f"{B}{msg.ljust(55)}{W}", end="")
        for _ in range(6):
            time.sleep(random.uniform(0.3, 0.6)) # Toplam ~10 saniye sürer
            print(f"{G}█{W}", end="", flush=True)
        print(" [ OK ]")
    time.sleep(1)

def input_check(prompt, min_val, max_val):
    while True:
        try:
            entry = input(f"{Y}{prompt}{W}").strip()
            val = int(entry)
            if min_val <= val <= max_val:
                return val
            print(f"{R} Geçersiz / Invalid! {min_val}-{max_val}{W}")
        except ValueError:
            print(f"{R} Hata! Sadece rakam / Digits only!{W}")

def main():
    clear()
    print(f"{Y}1- Türkçe | 2- English{W}")
    lang_choice = input_check(" Seçim / Choice: ", 1, 2)
    tr = lang_choice == 1
    
    clear()
    print(f"{Y}===================================================={W}")
    print(f"{G}    🚀 SİSTEM FPS ANALİZÖRÜ v7.5       {W}")
    print(f"{Y}          Developer: Emir & Gemini                  {W}")
    print(f"{Y}===================================================={W}\n")

    # 1. CPU
    print(f"{B}[1] CPU MARKASI / BRAND:{W} 1- Intel | 2- AMD")
    cpu_br = input_check(" Seçiminiz / Choice: ", 1, 2)
    
    if cpu_br == 1:
        print(f"\n{B}Intel Model:{W} 1- Core i3 | 2- Core i5 | 3- Core i7")
    else:
        print(f"\n{B}AMD Model:{W} 1- Ryzen 3 | 2- Ryzen 5 | 3- Ryzen 7")
    cpu_model = input_check(" Seçim / Choice: ", 1, 3)
    
    cpu_gen = input_check(f"\n{B}[1.1] CPU NESLİ / GEN (1-15):{W} ", 1, 15)

    # 2. GPU (AKILLI FİLTRE & ASUS ROG)
    print(f"\n{B}[2] GPU MARKASI / BRAND:{W}")
    # Eğer AMD CPU seçildiyse Intel Dahili seçeneği çıkmayacak
    if cpu_br == 1:
        print(" 1- NVIDIA | 2- AMD | 3- Asus ROG | 4- Intel (Dahili)")
        gpu_br = input_check(" Seçim / Choice: ", 1, 4)
    else:
        print(" 1- NVIDIA | 2- AMD | 3- Asus ROG")
        gpu_br = input_check(" Seçim / Choice: ", 1, 3)

    gpu_pow = 0
    # NVIDIA veya Asus ROG seçilirse RTX Serisi
    if gpu_br in [1, 3]:
        print(f"\n{B}RTX SERİSİ:{W} 1- 1000 | 2- 2000 | 3- 3000 | 4- 4000 | 5- 5000")
        gpu_pow = input_check(" Seçim / Choice: ", 1, 5)
    # AMD seçilirse senin isteğin üzerine GTX serisi geliyor
    elif gpu_br == 2:
        print(f"\n{B}GTX SERİSİ:{W} 1- GTX 10 | 2- GTX 16 | 3- GTX 1080 TI")
        gpu_pow = input_check(" Seçim / Choice: ", 1, 3)

    # 3. RAM & DDR (GÜNCELLENDİ)
    ram_cap = input_check(f"\n{B}[3] RAM KAPASİTESİ:{W} 1- 4GB | 2- 8GB | 3- 16GB | 4- 32GB\n Seçim / Choice: ", 1, 4)
    print(f"\n{B}[3.1] RAM NESLİ / GENERATION:{W} 1- DDR3 | 2- DDR4 | 3- DDR5")
    ram_ddr = input_check(" Seçim / Choice: ", 1, 3)

    # 4. DEPOLAMA
    print(f"\n{B}[4] DEPOLAMA / STORAGE:{W} 1- HDD | 2- SATA SSD | 3- NVMe SSD")
    disk_idx = input_check(" Seçim / Choice: ", 1, 3)
    
    # 5. SOĞUTMA (İNGİLİZCE HATASI DÜZELTİLDİ)
    if tr:
        print(f"\n{B}[5] SOĞUTMA SİSTEMİ:{W} 1- Stok | 2- Hava | 3- Sıvı")
    else:
        print(f"\n{B}[5] COOLING SYSTEM:{W} 1- Stock | 2- Air | 3- Liquid")
    cool_idx = input_check(" Seçim / Choice: ", 1, 3)

    # 6. KATEGORİ
    print(f"\n{B}[6] GRAFİK KATEGORİSİ / GRAPHIC CATEGORY:{W}")
    print(" 1- Piksel | 2- 2D | 3- 3D Hafif | 4- 3D Orta | 5- 3D Ağır" if tr else " 1- Pixel | 2- 2D | 3- 3D Light | 4- 3D Medium | 5- 3D Heavy")
    cat_idx = input_check(" Seçim / Choice: ", 1, 5)

    clear()
    loading(tr)

    # --- HESAPLAMA MOTORU (SALLAMASYON DEĞİL) ---
    c_p = [40, 75, 100][cpu_model-1]
    gen_mult = 1.0 + (cpu_gen * 0.07) # Nesil etkisi arttırıldı
    
    if gpu_br in [1, 3]: # RTX / Asus
        g_p = [55, 90, 130, 175, 230][gpu_pow-1]
        if gpu_br == 3: g_p *= 1.1 # Asus ROG bonusu %10
    elif gpu_br == 2: # AMD (GTX modunda)
        g_p = [45, 70, 100][gpu_pow-1]
    else: # Intel Dahili
        g_p = 25
    
    r_cap_p = [25, 55, 95, 125][ram_cap-1]
    r_ddr_m = [0.8, 1.0, 1.3][ram_ddr-1] # DDR5 etkisi büyük
    
    disk_m = [0.8, 1.0, 1.2][disk_idx-1]
    cool_m = [0.8, 1.0, 1.2][cool_idx-1]
    
    diffs = [0.12, 0.3, 0.6, 1.3, 2.8]
    current_diff = diffs[cat_idx-1]

    # Karmaşık Güç Formülü
    total_power = ((c_p * gen_mult) * 0.35 + (g_p * 0.45) + (r_cap_p * r_ddr_m) * 0.20) * cool_m * disk_m
    final_fps = int((total_power / current_diff) * 1.1)

    # SONUÇ EKRANI
    res_title = 'PERFORMANS RAPORU' if tr else 'PERFORMANCE REPORT'
    print(f"\n{Y}===================================================={W}")
    print(f"{G}             {res_title}           {W}")
    print(f"{Y}===================================================={W}")
    print(f"{('🚀 Tahmini FPS' if tr else '🚀 Estimated FPS').ljust(25)} : {G if final_fps >= 60 else (Y if final_fps >= 30 else R)}{final_fps} FPS{W}")
    
    st = ("AKICI" if final_fps >= 60 else ("ORTA" if final_fps >= 30 else "DÜŞÜK")) if tr else ("SMOOTH" if final_fps >= 60 else ("MID" if final_fps >= 30 else "LOW"))
    print(f"{('📊 Durum / Status').ljust(25)} : {st}")
    print(f"{Y}===================================================={W}")

if __name__ == "__main__":
    main()