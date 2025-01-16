import os
import pandas as pd
import pdfplumber

def extract_pdf_data_with_headers(pdf_path):
    """PDF'den başlık ve değerleri çıkarma."""
    data = {}
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    lines = page_text.split("\n")
                    for line in lines:
                        if ":" in line:
                            key, value = line.split(":", 1)
                            key = key.strip()
                            value = value.strip()
                            data[key] = value
    except Exception as e:
        print(f"Hata oluştu {pdf_path}: {e}")
    return data

def process_pdfs_to_excel(base_folder):
    
    all_data = []
    for root, dirs, files in os.walk(base_folder):
        # Klasör yapısını kontrol et ve proje ile ilçe adını al
        parts = root.split(os.sep)
        if len(parts) >= 3:  # En az 3 seviyeli klasör yapısı bekleniyor
            project_name = parts[-2]  # Proje adı, bir üst klasör
            district_name = parts[-1]  # İlçe adı, mevcut klasör
        else:
            continue

        for file in files:
            if file.lower().endswith(".pdf"):
                pdf_path = os.path.join(root, file)
                village_name = os.path.splitext(file)[0]  # Köy adı, dosya adı
                pdf_data = extract_pdf_data_with_headers(pdf_path)
                pdf_data["Project Name"] = project_name  # Proje adını ekle
                pdf_data["District Name"] = district_name  # İlçe adını ekle
                pdf_data["Village Name"] = village_name  # Köy adını ekle
                all_data.append(pdf_data)

    # Verileri DataFrame'e dönüştür ve Excel'e yaz
    df = pd.DataFrame(all_data)
    
    # Kolon sırasını ayarla
    columns_order = ["Project Name", "District Name", "Village Name"] + [col for col in df.columns if col not in ["Project Name", "District Name", "Village Name"]]
    df = df[columns_order]
    
    # Excel dosyasını kaydet
    output_path = os.path.join(base_folder, "detailed_project_summary.xlsx")
    df.to_excel(output_path, index=False)
    print(f"Veriler {output_path} konumuna kaydedildi.")

# Google Drive'daki klasör yolunu belirtin
base_folder_path = "/content/drive/MyDrive/Projeler"  
process_pdfs_to_excel(base_folder_path)
