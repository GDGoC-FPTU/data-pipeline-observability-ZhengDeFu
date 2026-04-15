"""
==============================================================
Day 10 Lab: Build Your First Automated ETL Pipeline
==============================================================
Student ID: AI20K-XXXX  (<-- Thay XXXX bang ma so cua ban)
Name: Your Name Here

Nhiem vu:
   1. Extract:   Doc du lieu tu file JSON
   2. Validate:  Kiem tra & loai bo du lieu khong hop le
   3. Transform: Chuan hoa category + tinh gia giam 10%
   4. Load:      Luu ket qua ra file CSV

Cham diem tu dong:
   - Script phai chay KHONG LOI (20d)
   - Validation: loai record gia <= 0, category rong (10d)
   - Transform: discounted_price + category Title Case (10d)
   - Logging: in so record processed/dropped (10d)
   - Timestamp: them cot processed_at (10d)
==============================================================
"""

import json
import pandas as pd
import os
import datetime
import logging

# --- LOGGING CONFIGURATION ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# --- CONFIGURATION ---
SOURCE_FILE = 'raw_data.json'
OUTPUT_FILE = 'processed_data.csv'


def extract(file_path):
    """
    Task 1: Doc du lieu JSON tu file.

    Goi y:
       - Dung json.load() de doc file JSON
       - Xu ly truong hop file khong ton tai (FileNotFoundError)

    Returns:
        list: Danh sach cac records (dictionaries)
    """
    logger.info(f"[EXTRACT] Starting extraction from {file_path}...")

    try:
        # Mo file JSON va doc du lieu
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Dam bao du lieu la list
        if isinstance(data, list):
            logger.info(f"[EXTRACT] Successfully extracted {len(data)} records")
            return data
        else:
            logger.warning("[EXTRACT] JSON data is not a list.")
            return []

    except FileNotFoundError:
        logger.error(f"[EXTRACT] File '{file_path}' not found.")
        return []

    except json.JSONDecodeError:
        logger.error(f"[EXTRACT] File '{file_path}' is not valid JSON.")
        return []


def validate(data):
    """
    Task 2: Kiem tra chat luong du lieu.

    Quy tac validation:
       - Price phai > 0 (loai bo gia am hoac bang 0)
       - Category khong duoc rong

    Goi y:
       - Dung record.get('price', 0) de lay gia
       - Dung record.get('category') de kiem tra category
       - In ra so luong record hop le va khong hop le

    Returns:
        list: Danh sach cac records hop le 
    """
    valid_records = []
    error_count = 0

    for record in data:
        price = record.get('price', 0)
        category = record.get('category', '')
        
        # Kiểm tra điều kiện
        if price > 0 and category and category.strip():
            valid_records.append(record)
        else:
            error_count += 1

    print(f"Validation complete. Valid: {len(valid_records)}, Errors: {error_count}")
    print(f"Processed: {len(valid_records)} valid records, Dropped: {error_count} invalid records.")
    return valid_records


def transform(data):
    """
    Task 3: Ap dung business logic.

    Yeu cau:
       - Tinh discounted_price = price * 0.9 (giam 10%)
       - Chuan hoa category thanh Title Case (vi du: "electronics" -> "Electronics")
       - Them cot processed_at = timestamp hien tai

    Goi y:
       - Dung pd.DataFrame(data) de tao DataFrame
       - df['discounted_price'] = df['price'] * 0.9
       - df['category'] = df['category'].str.title()
       - df['processed_at'] = datetime.datetime.now().isoformat()

    Returns:
        pd.DataFrame: DataFrame da duoc transform
    """
    logger.info(f"[TRANSFORM] Starting transformation on {len(data)} records...")
    
    # Tao DataFrame tu du lieu
    df = pd.DataFrame(data)
    
    # Tinh discounted_price (giam 10%)
    df['discounted_price'] = df['price'] * 0.9
    logger.debug(f"[TRANSFORM] Calculated discounted_price (10% off)")
    
    # Chuan hoa category thanh Title Case
    df['category'] = df['category'].str.title()
    logger.debug(f"[TRANSFORM] Normalized categories to Title Case")
    
    # Them cot processed_at voi timestamp hien tai
    df['processed_at'] = datetime.datetime.now().isoformat()
    logger.debug(f"[TRANSFORM] Added processed_at timestamp")
    
    logger.info(f"[TRANSFORM] Transformation complete. {len(df)} records transformed.")
    return df


def load(df, output_path):
    """
    Task 4: Luu DataFrame ra file CSV.

    Goi y:
       - df.to_csv(output_path, index=False)
    """
    logger.info(f"[LOAD] Starting to save {len(df)} records to {output_path}...")
    df.to_csv(output_path, index=False)
    logger.info(f"[LOAD] Data successfully saved to {output_path}")


# ============================================================
# MAIN PIPELINE
# ============================================================
if __name__ == "__main__":
    logger.info("=" * 50)
    logger.info("ETL Pipeline Started...")
    logger.info("=" * 50)

    # 1. Extract
    raw_data = extract(SOURCE_FILE)

    if raw_data:
        # 2. Validate
        clean_data = validate(raw_data)

        # 3. Transform
        final_df = transform(clean_data)

        # 4. Load
        if final_df is not None:
            load(final_df, OUTPUT_FILE)
            logger.info("=" * 50)
            logger.info(f"✅ Pipeline completed! {len(final_df)} records saved.")
            logger.info("=" * 50)
        else:
            logger.error("\n❌ Transform returned None. Check your transform() function.")
    else:
        logger.error("\n❌ Pipeline aborted: No data extracted.")
