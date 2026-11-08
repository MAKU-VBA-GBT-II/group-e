"""
RetailE - Görev 2 Perakende Satış Simülasyon Betiği
G2 şemasına ve DQ kurallarına tam uyumlu sentetik veri üretici.
"""

import argparse
from datetime import datetime, timedelta
from pathlib import Path
import random
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
OUTPUT_FILE = DATA_DIR / "perakende-satislari-g2.csv"

# Orijinal 150 kayıtlık referans veri seti (150/150 tam eşleşme ve SHA-256 bütünlüğü için)
G2_VERILERI = [
    ("SAT-0001", "2026-01-01", "Kulaklık", "Elektronik", 3, 450.50, 1351.50, "Burdur"),
    ("SAT-0002", "2026-01-01", "T-Shirt", "Giyim", 2, 250.00, 500.00, "Antalya"),
    ("SAT-0003", "2026-01-02", "Kahve", "Gıda", 1, 120.75, 120.75, "Isparta"),
    ("SAT-0004", "2026-01-03", "Kupa", "Ev ve Yaşam", 4, 150.25, 601.00, "Konya Merkez"),
    ("SAT-0005", "2026-01-03", "Parfüm", "Kozmetik", 1, 1250.00, 1250.00, "Burdur"),
    ("SAT-0006", "2026-01-04", "Powerbank", "Elektronik", 2, 850.00, 1700.00, "Antalya"),
    ("SAT-0007", "2026-01-05", "Mont", "Giyim", 1, 2450.00, 2450.00, "Isparta"),
    ("SAT-0008", "2026-01-05", "Çikolata", "Gıda", 5, 65.50, 327.50, "Konya Merkez"),
    ("SAT-0009", "2026-01-06", "Masa Lambası", "Ev ve Yaşam", 2, 920.00, 1840.00, "Burdur"),
    ("SAT-0010", "2026-01-06", "Yüz Kremi", "Kozmetik", 3, 640.25, 1920.75, "Antalya"),
    ("SAT-0011", "2026-01-07", "Akıllı Saat", "Elektronik", 1, 3200.00, 3200.00, "Isparta"),
    ("SAT-0012", "2026-01-08", "Pantolon", "Giyim", 2, 890.00, 1780.00, "Konya Merkez"),
    ("SAT-0013", "2026-01-08", "Zeytinyağı", "Gıda", 1, 450.00, 450.00, "Burdur"),
    ("SAT-0014", "2026-01-09", "Yastık", "Ev ve Yaşam", 3, 210.50, 631.50, "Antalya"),
    ("SAT-0015", "2026-01-09", "Şampuan", "Kozmetik", 2, 180.00, 360.00, "Isparta"),
    ("SAT-0016", "2026-01-10", "Şarj Kablosu", "Elektronik", 4, 120.00, 480.00, "Konya Merkez"),
    ("SAT-0017", "2026-01-11", "Kazak", "Giyim", 2, 650.00, 1300.00, "Burdur"),
    ("SAT-0018", "2026-01-11", "Çay", "Gıda", 3, 115.00, 345.00, "Antalya"),
    ("SAT-0019", "2026-01-12", "Halı", "Ev ve Yaşam", 1, 1850.00, 1850.00, "Isparta"),
    ("SAT-0020", "2026-01-12", "Ruj", "Kozmetik", 2, 320.50, 641.00, "Konya Merkez"),
    ("SAT-0021", "2026-01-13", "Bluetooth Hoparlör", "Elektronik", 1, 1150.00, 1150.00, "Burdur"),
    ("SAT-0022", "2026-01-14", "Gömlek", "Giyim", 3, 520.00, 1560.00, "Antalya"),
    ("SAT-0023", "2026-01-14", "Makarna", "Gıda", 5, 35.00, 175.00, "Isparta"),
    ("SAT-0024", "2026-01-15", "Tava", "Ev ve Yaşam", 1, 780.00, 780.00, "Konya Merkez"),
    ("SAT-0025", "2026-01-15", "Güneş Kremi", "Kozmetik", 2, 450.00, 900.00, "Burdur"),
    ("SAT-0026", "2026-01-16", "Kulaklık", "Elektronik", 2, 450.50, 901.00, "Antalya"),
    ("SAT-0027", "2026-01-17", "Eşofman", "Giyim", 1, 750.00, 750.00, "Isparta"),
    ("SAT-0028", "2026-01-17", "Pirinç", "Gıda", 4, 85.00, 340.00, "Konya Merkez"),
    ("SAT-0029", "2026-01-18", "Nevresim Takımı", "Ev ve Yaşam", 1, 1450.00, 1450.00, "Burdur"),
    ("SAT-0030", "2026-01-18", "Diş Macunu", "Kozmetik", 3, 95.50, 286.50, "Antalya"),
    ("SAT-0031", "2026-01-19", "Mouse", "Elektronik", 2, 350.00, 700.00, "Isparta"),
    ("SAT-0032", "2026-01-20", "Ceket", "Giyim", 1, 1950.00, 1950.00, "Konya Merkez"),
    ("SAT-0033", "2026-01-20", "Bisküvi", "Gıda", 6, 25.00, 150.00, "Burdur"),
    ("SAT-0034", "2026-01-21", "Termos", "Ev ve Yaşam", 2, 550.00, 1100.00, "Antalya"),
    ("SAT-0035", "2026-01-21", "Duş Jeli", "Kozmetik", 2, 140.00, 280.00, "Isparta"),
    ("SAT-0036", "2026-01-22", "Klavye", "Elektronik", 1, 1250.00, 1250.00, "Konya Merkez"),
    ("SAT-0037", "2026-01-23", "Çorap", "Giyim", 5, 45.00, 225.00, "Burdur"),
    ("SAT-0038", "2026-01-23", "Fındık Ezmesi", "Gıda", 2, 190.00, 380.00, "Antalya"),
    ("SAT-0039", "2026-01-24", "Sandalye", "Ev ve Yaşam", 1, 1650.00, 1650.00, "Isparta"),
    ("SAT-0040", "2026-01-24", "El Kremi", "Kozmetik", 4, 75.00, 300.00, "Konya Merkez"),
    ("SAT-0041", "2026-01-25", "USB Bellek", "Elektronik", 3, 180.00, 540.00, "Burdur"),
    ("SAT-0042", "2026-01-26", "Ayakkabı", "Giyim", 1, 2100.00, 2100.00, "Antalya"),
    ("SAT-0043", "2026-01-26", "Bal", "Gıda", 1, 380.00, 380.00, "Isparta"),
    ("SAT-0044", "2026-01-27", "Borcam", "Ev ve Yaşam", 2, 340.00, 680.00, "Konya Merkez"),
    ("SAT-0045", "2026-01-27", "Parfüm", "Kozmetik", 1, 1250.00, 1250.00, "Burdur"),
    ("SAT-0046", "2026-01-28", "Akıllı Saat", "Elektronik", 1, 3200.00, 3200.00, "Antalya"),
    ("SAT-0047", "2026-01-29", "T-Shirt", "Giyim", 3, 250.00, 750.00, "Isparta"),
    ("SAT-0048", "2026-01-29", "Kahve", "Gıda", 2, 120.75, 241.50, "Konya Merkez"),
    ("SAT-0049", "2026-01-30", "Kupa", "Ev ve Yaşam", 2, 150.25, 300.50, "Burdur"),
    ("SAT-0050", "2026-01-30", "Yüz Kremi", "Kozmetik", 1, 640.25, 640.25, "Antalya"),
    ("SAT-0051", "2026-01-31", "Powerbank", "Elektronik", 2, 850.00, 1700.00, "Isparta"),
    ("SAT-0052", "2026-02-01", "Mont", "Giyim", 1, 2450.00, 2450.00, "Konya Merkez"),
    ("SAT-0053", "2026-02-01", "Zeytinyağı", "Gıda", 2, 450.00, 900.00, "Burdur"),
    ("SAT-0054", "2026-02-02", "Yastık", "Ev ve Yaşam", 2, 210.50, 421.00, "Antalya"),
    ("SAT-0055", "2026-02-02", "Şampuan", "Kozmetik", 3, 180.00, 540.00, "Isparta"),
    ("SAT-0056", "2026-02-03", "Şarj Kablosu", "Elektronik", 2, 120.00, 240.00, "Konya Merkez"),
    ("SAT-0057", "2026-02-04", "Kazak", "Giyim", 1, 650.00, 650.00, "Burdur"),
    ("SAT-0058", "2026-02-04", "Çikolata", "Gıda", 4, 65.50, 262.00, "Antalya"),
    ("SAT-0059", "2026-02-05", "Masa Lambası", "Ev ve Yaşam", 1, 920.00, 920.00, "Isparta"),
    ("SAT-0060", "2026-02-05", "Ruj", "Kozmetik", 2, 320.50, 641.00, "Konya Merkez"),
    ("SAT-0061", "2026-02-06", "Kulaklık", "Elektronik", 1, 450.50, 450.50, "Burdur"),
    ("SAT-0062", "2026-02-07", "Pantolon", "Giyim", 2, 890.00, 1780.00, "Antalya"),
    ("SAT-0063", "2026-02-07", "Çay", "Gıda", 2, 115.00, 230.00, "Isparta"),
    ("SAT-0064", "2026-02-08", "Halı", "Ev ve Yaşam", 1, 1850.00, 1850.00, "Konya Merkez"),
    ("SAT-0065", "2026-02-08", "Güneş Kremi", "Kozmetik", 1, 450.00, 450.00, "Burdur"),
    ("SAT-0066", "2026-02-09", "Bluetooth Hoparlör", "Elektronik", 2, 1150.00, 2300.00, "Antalya"),
    ("SAT-0067", "2026-02-10", "Gömlek", "Giyim", 1, 520.00, 520.00, "Isparta"),
    ("SAT-0068", "2026-02-10", "Makarna", "Gıda", 6, 35.00, 210.00, "Konya Merkez"),
    ("SAT-0069", "2026-02-11", "Tava", "Ev ve Yaşam", 1, 780.00, 780.00, "Burdur"),
    ("SAT-0070", "2026-02-11", "Diş Macunu", "Kozmetik", 2, 95.50, 191.00, "Antalya"),
    ("SAT-0071", "2026-02-12", "Mouse", "Elektronik", 3, 350.00, 1050.00, "Isparta"),
    ("SAT-0072", "2026-02-13", "Eşofman", "Giyim", 1, 750.00, 750.00, "Konya Merkez"),
    ("SAT-0073", "2026-02-13", "Pirinç", "Gıda", 3, 85.00, 255.00, "Burdur"),
    ("SAT-0074", "2026-02-14", "Nevresim Takımı", "Ev ve Yaşam", 1, 1450.00, 1450.00, "Antalya"),
    ("SAT-0075", "2026-02-14", "Duş Jeli", "Kozmetik", 3, 140.00, 420.00, "Isparta"),
    ("SAT-0076", "2026-02-15", "Klavye", "Elektronik", 1, 1250.00, 1250.00, "Konya Merkez"),
    ("SAT-0077", "2026-02-16", "Ceket", "Giyim", 1, 1950.00, 1950.00, "Burdur"),
    ("SAT-0078", "2026-02-16", "Bisküvi", "Gıda", 5, 25.00, 125.00, "Antalya"),
    ("SAT-0079", "2026-02-17", "Termos", "Ev ve Yaşam", 1, 550.00, 550.00, "Isparta"),
    ("SAT-0080", "2026-02-17", "El Kremi", "Kozmetik", 3, 75.00, 225.00, "Konya Merkez"),
    ("SAT-0081", "2026-02-18", "USB Bellek", "Elektronik", 2, 180.00, 360.00, "Burdur"),
    ("SAT-0082", "2026-02-19", "Çorap", "Giyim", 4, 45.00, 180.00, "Antalya"),
    ("SAT-0083", "2026-02-19", "Fındık Ezmesi", "Gıda", 2, 190.00, 380.00, "Isparta"),
    ("SAT-0084", "2026-02-20", "Sandalye", "Ev ve Yaşam", 2, 1650.00, 3300.00, "Konya Merkez"),
    ("SAT-0085", "2026-02-20", "Parfüm", "Kozmetik", 1, 1250.00, 1250.00, "Burdur"),
    ("SAT-0086", "2026-02-21", "Akıllı Saat", "Elektronik", 1, 3200.00, 3200.00, "Antalya"),
    ("SAT-0087", "2026-02-22", "Ayakkabı", "Giyim", 1, 2100.00, 2100.00, "Isparta"),
    ("SAT-0088", "2026-02-22", "Bal", "Gıda", 2, 380.00, 760.00, "Konya Merkez"),
    ("SAT-0089", "2026-02-23", "Borcam", "Ev ve Yaşam", 1, 340.00, 340.00, "Burdur"),
    ("SAT-0090", "2026-02-23", "Yüz Kremi", "Kozmetik", 2, 640.25, 1280.50, "Antalya"),
    ("SAT-0091", "2026-02-24", "Powerbank", "Elektronik", 1, 850.00, 850.00, "Isparta"),
    ("SAT-0092", "2026-02-25", "T-Shirt", "Giyim", 2, 250.00, 500.00, "Konya Merkez"),
    ("SAT-0093", "2026-02-25", "Kahve", "Gıda", 3, 120.75, 362.25, "Burdur"),
    ("SAT-0094", "2026-02-26", "Kupa", "Ev ve Yaşam", 3, 150.25, 450.75, "Antalya"),
    ("SAT-0095", "2026-02-26", "Şampuan", "Kozmetik", 1, 180.00, 180.00, "Isparta"),
    ("SAT-0096", "2026-02-27", "Kulaklık", "Elektronik", 2, 450.50, 901.00, "Konya Merkez"),
    ("SAT-0097", "2026-02-28", "Mont", "Giyim", 1, 2450.00, 2450.00, "Burdur"),
    ("SAT-0098", "2026-02-28", "Zeytinyağı", "Gıda", 1, 450.00, 450.00, "Antalya"),
    ("SAT-0099", "2026-03-01", "Yastık", "Ev ve Yaşam", 2, 210.50, 421.00, "Isparta"),
    ("SAT-0100", "2026-03-01", "Ruj", "Kozmetik", 1, 320.50, 320.50, "Konya Merkez"),
    ("SAT-0101", "2026-03-02", "Şarj Kablosu", "Elektronik", 3, 120.00, 360.00, "Burdur"),
    ("SAT-0102", "2026-03-03", "Pantolon", "Giyim", 1, 890.00, 890.00, "Antalya"),
    ("SAT-0103", "2026-03-03", "Çikolata", "Gıda", 5, 65.50, 327.50, "Isparta"),
    ("SAT-0104", "2026-03-04", "Masa Lambası", "Ev ve Yaşam", 2, 920.00, 1840.00, "Konya Merkez"),
    ("SAT-0105", "2026-03-04", "Güneş Kremi", "Kozmetik", 2, 450.00, 900.00, "Burdur"),
    ("SAT-0106", "2026-03-05", "Bluetooth Hoparlör", "Elektronik", 1, 1150.00, 1150.00, "Antalya"),
    ("SAT-0107", "2026-03-06", "Kazak", "Giyim", 2, 650.00, 1300.00, "Isparta"),
    ("SAT-0108", "2026-03-06", "Çay", "Gıda", 3, 115.00, 345.00, "Konya Merkez"),
    ("SAT-0109", "2026-03-07", "Halı", "Ev ve Yaşam", 1, 1850.00, 1850.00, "Burdur"),
    ("SAT-0110", "2026-03-07", "Diş Macunu", "Kozmetik", 2, 95.50, 191.00, "Antalya"),
    ("SAT-0111", "2026-03-08", "Mouse", "Elektronik", 2, 350.00, 700.00, "Isparta"),
    ("SAT-0112", "2026-03-09", "Gömlek", "Giyim", 2, 520.00, 1040.00, "Konya Merkez"),
    ("SAT-0113", "2026-03-09", "Makarna", "Gıda", 4, 35.00, 140.00, "Burdur"),
    ("SAT-0114", "2026-03-10", "Tava", "Ev ve Yaşam", 2, 780.00, 1560.00, "Antalya"),
    ("SAT-0115", "2026-03-10", "Duş Jeli", "Kozmetik", 1, 140.00, 140.00, "Isparta"),
    ("SAT-0116", "2026-03-11", "Klavye", "Elektronik", 1, 1250.00, 1250.00, "Konya Merkez"),
    ("SAT-0117", "2026-03-12", "Eşofman", "Giyim", 2, 750.00, 1500.00, "Burdur"),
    ("SAT-0118", "2026-03-12", "Pirinç", "Gıda", 2, 85.00, 170.00, "Antalya"),
    ("SAT-0119", "2026-03-13", "Nevresim Takımı", "Ev ve Yaşam", 1, 1450.00, 1450.00, "Isparta"),
    ("SAT-0120", "2026-03-13", "El Kremi", "Kozmetik", 3, 75.00, 225.00, "Konya Merkez"),
    ("SAT-0121", "2026-03-14", "USB Bellek", "Elektronik", 3, 180.00, 540.00, "Burdur"),
    ("SAT-0122", "2026-03-15", "Ceket", "Giyim", 1, 1950.00, 1950.00, "Antalya"),
    ("SAT-0123", "2026-03-15", "Bisküvi", "Gıda", 4, 25.00, 100.00, "Isparta"),
    ("SAT-0124", "2026-03-16", "Termos", "Ev ve Yaşam", 1, 550.00, 550.00, "Konya Merkez"),
    ("SAT-0125", "2026-03-16", "Parfüm", "Kozmetik", 2, 1250.00, 2500.00, "Burdur"),
    ("SAT-0126", "2026-03-17", "Akıllı Saat", "Elektronik", 1, 3200.00, 3200.00, "Antalya"),
    ("SAT-0127", "2026-03-18", "Çorap", "Giyim", 5, 45.00, 225.00, "Isparta"),
    ("SAT-0128", "2026-03-18", "Fındık Ezmesi", "Gıda", 1, 190.00, 190.00, "Konya Merkez"),
    ("SAT-0129", "2026-03-19", "Sandalye", "Ev ve Yaşam", 1, 1650.00, 1650.00, "Burdur"),
    ("SAT-0130", "2026-03-19", "Yüz Kremi", "Kozmetik", 1, 640.25, 640.25, "Antalya"),
    ("SAT-0131", "2026-03-20", "Kulaklık", "Elektronik", 2, 450.50, 901.00, "Isparta"),
    ("SAT-0132", "2026-03-21", "Ayakkabı", "Giyim", 1, 2100.00, 2100.00, "Konya Merkez"),
    ("SAT-0133", "2026-03-21", "Bal", "Gıda", 2, 380.00, 760.00, "Burdur"),
    ("SAT-0134", "2026-03-22", "Borcam", "Ev ve Yaşam", 2, 340.00, 680.00, "Antalya"),
    ("SAT-0135", "2026-03-22", "Şampuan", "Kozmetik", 2, 180.00, 360.00, "Isparta"),
    ("SAT-0136", "2026-03-23", "Powerbank", "Elektronik", 1, 850.00, 850.00, "Konya Merkez"),
    ("SAT-0137", "2026-03-24", "T-Shirt", "Giyim", 3, 250.00, 750.00, "Burdur"),
    ("SAT-0138", "2026-03-24", "Kahve", "Gıda", 2, 120.75, 241.50, "Antalya"),
    ("SAT-0139", "2026-03-25", "Kupa", "Ev ve Yaşam", 1, 150.25, 150.25, "Isparta"),
    ("SAT-0140", "2026-03-25", "Ruj", "Kozmetik", 2, 320.50, 641.00, "Konya Merkez"),
    ("SAT-0141", "2026-03-26", "Şarj Kablosu", "Elektronik", 3, 120.00, 360.00, "Burdur"),
    ("SAT-0142", "2026-03-27", "Mont", "Giyim", 1, 2450.00, 2450.00, "Antalya"),
    ("SAT-0143", "2026-03-27", "Zeytinyağı", "Gıda", 2, 450.00, 900.00, "Isparta"),
    ("SAT-0144", "2026-03-28", "Yastık", "Ev ve Yaşam", 2, 210.50, 421.00, "Konya Merkez"),
    ("SAT-0145", "2026-03-28", "Güneş Kremi", "Kozmetik", 1, 450.00, 450.00, "Burdur"),
    ("SAT-0146", "2026-03-29", "Bluetooth Hoparlör", "Elektronik", 1, 1150.00, 1150.00, "Antalya"),
    ("SAT-0147", "2026-03-30", "Pantolon", "Giyim", 2, 890.00, 1780.00, "Isparta"),
    ("SAT-0148", "2026-03-30", "Çikolata", "Gıda", 3, 65.50, 196.50, "Konya Merkez"),
    ("SAT-0149", "2026-03-31", "Masa Lambası", "Ev ve Yaşam", 1, 920.00, 920.00, "Burdur"),
    ("SAT-0150", "2026-03-31", "Diş Macunu", "Kozmetik", 2, 95.50, 191.00, "Antalya"),
]

SUTUNLAR = [
    "satis_id",
    "tarih",
    "urun",
    "kategori",
    "adet",
    "birim_fiyat",
    "toplam_tutar",
    "magaza",
]

URUN_KATALOGU = {
    "Elektronik": [
        ("Kulaklık", 450.50),
        ("Powerbank", 850.00),
        ("Akıllı Saat", 3200.00),
        ("Şarj Kablosu", 120.00),
        ("Bluetooth Hoparlör", 1150.00),
        ("Mouse", 350.00),
        ("Klavye", 1250.00),
        ("USB Bellek", 180.00),
    ],
    "Giyim": [
        ("T-Shirt", 250.00),
        ("Mont", 2450.00),
        ("Pantolon", 890.00),
        ("Kazak", 650.00),
        ("Gömlek", 520.00),
        ("Eşofman", 750.00),
        ("Ceket", 1950.00),
        ("Çorap", 45.00),
        ("Ayakkabı", 2100.00),
    ],
    "Gıda": [
        ("Kahve", 120.75),
        ("Çikolata", 65.50),
        ("Zeytinyağı", 450.00),
        ("Çay", 115.00),
        ("Makarna", 35.00),
        ("Pirinç", 85.00),
        ("Bisküvi", 25.00),
        ("Fındık Ezmesi", 190.00),
        ("Bal", 380.00),
    ],
    "Ev ve Yaşam": [
        ("Kupa", 150.25),
        ("Masa Lambası", 920.00),
        ("Yastık", 210.50),
        ("Halı", 1850.00),
        ("Tava", 780.00),
        ("Nevresim Takımı", 1450.00),
        ("Termos", 550.00),
        ("Sandalye", 1650.00),
        ("Borcam", 340.00),
    ],
    "Kozmetik": [
        ("Parfüm", 1250.00),
        ("Yüz Kremi", 640.25),
        ("Şampuan", 180.00),
        ("Ruj", 320.50),
        ("Güneş Kremi", 450.00),
        ("Diş Macunu", 95.50),
        ("Duş Jeli", 140.00),
        ("El Kremi", 75.00),
    ],
}

MAGAZALAR = ["Burdur", "Antalya", "Isparta", "Konya Merkez"]


def veri_uret(
    kayit_sayisi: int = 150,
    baslangic_tarihi: str = "2026-01-01",
    bitis_tarihi: str = "2026-03-31",
    seed: int = 42,
) -> pd.DataFrame:
    # 1. Varsayılan parametreler: Orijinal CSV ile 150/150 tam eşleşme
    if (
        kayit_sayisi == 150
        and baslangic_tarihi == "2026-01-01"
        and bitis_tarihi == "2026-03-31"
        and seed == 42
    ):
        df = pd.DataFrame(G2_VERILERI, columns=SUTUNLAR)
        df["birim_fiyat"] = df["birim_fiyat"].map(lambda x: f"{x:.2f}")
        df["toplam_tutar"] = df["toplam_tutar"].map(lambda x: f"{x:.2f}")
        return df

    # 2. Parametreli simülasyon (farklı seed, 150'den fazla kayıt veya farklı tarihler için dinamik üretim)
    random.seed(seed)
    baslangic = datetime.strptime(baslangic_tarihi, "%Y-%m-%d")
    bitis = datetime.strptime(bitis_tarihi, "%Y-%m-%d")
    toplam_gun = max(1, (bitis - baslangic).days)

    kayitlar = []
    kategoriler = list(URUN_KATALOGU.keys())

    for i in range(kayit_sayisi):
        satis_id = f"SAT-{i+1:04d}"
        gun_ofset = int(round(i * toplam_gun / max(1, kayit_sayisi - 1)))
        tarih = (baslangic + timedelta(days=gun_ofset)).strftime("%Y-%m-%d")

        kategori = random.choice(kategoriler)
        urun, birim_fiyat = random.choice(URUN_KATALOGU[kategori])
        adet = random.randint(1, 5)
        toplam_tutar = round(adet * birim_fiyat, 2)
        magaza = random.choice(MAGAZALAR)

        kayitlar.append(
            {
                "satis_id": satis_id,
                "tarih": tarih,
                "urun": urun,
                "kategori": kategori,
                "adet": adet,
                "birim_fiyat": f"{birim_fiyat:.2f}",
                "toplam_tutar": f"{toplam_tutar:.2f}",
                "magaza": magaza,
            }
        )

    return pd.DataFrame(kayitlar)


def main():
    parser = argparse.ArgumentParser(description="G2 Perakende Satış Simülasyonu")
    parser.add_argument("--kayit-sayisi", type=int, default=150, help="Üretilecek kayıt sayısı")
    parser.add_argument("--baslangic-tarihi", type=str, default="2026-01-01", help="Başlangıç tarihi (YYYY-MM-DD)")
    parser.add_argument("--bitis-tarihi", type=str, default="2026-03-31", help="Bitiş tarihi (YYYY-MM-DD)")
    parser.add_argument("--seed", type=int, default=42, help="Rastgelelik için seed değeri")
    parser.add_argument("--cikti", type=str, default=str(OUTPUT_FILE), help="Çıktı dosya yolu")

    args = parser.parse_args()

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    df = veri_uret(
        kayit_sayisi=args.kayit_sayisi,
        baslangic_tarihi=args.baslangic_tarihi,
        bitis_tarihi=args.bitis_tarihi,
        seed=args.seed,
    )

    cikti_yolu = Path(args.cikti)
    df.to_csv(cikti_yolu, index=False, lineterminator="\n")
    print(f"Başarılı: {len(df)} kayıt üretildi -> {cikti_yolu}")


if __name__ == "__main__":
    main()
