
## 📄 README.md (英文版)
```markdown
# 🖼️ BVQC Image Encode & Decode

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

This is a **Python program** that implements **BVQC (Block-based Visual Quantization Coding)** encoding and decoding for images. It reduces file size by grouping pixels and averaging their color values, achieving efficient image compression.

## 📖 What is BVQC?

**BVQC (Block-based Visual Quantization Coding)** is an image compression method that:

- Groups pixels into blocks (e.g., 3×3 = 9 pixels per block)
- Calculates the average color value for each block
- Replaces the block with a single representative color
- Significantly reduces file size while maintaining visual quality

This technique is particularly effective for images with large areas of similar colors.

## ✨ Key Features

- **Encode Mode**: Compresses an image using BVQC method
- **Decode Mode**: Restores the compressed image back to viewable format
- **Simple to Use**: Just specify input and output filenames
- **Educational**: Great for understanding image compression fundamentals

## 🛠️ Built With

- **Language**: Python 3.7+
- **Libraries**: PIL / Pillow (for image processing)
- **Algorithm**: BVQC (Block-based Visual Quantization Coding)

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Pillow library (`pip install Pillow`)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/LeoTheAuJai/BVQC-encode-and-decode.git
   cd BVQC-encode-and-decode
   ```

2. **Install dependencies**
   ```bash
   pip install Pillow
   ```

### Usage

1. **Open the Python file** (`eie2108 lab task 3.py`) in any text editor or IDE.

2. **Adjust file paths**:
   - Set `fname_in` to your input image filename (must be in the same directory)
   - Set `fname_out` to your desired output filename

3. **Select mode**:
   - **Encode**: Uncomment the encode function, comment the decode function
   - **Decode**: Uncomment the decode function, comment the encode function

4. **Run the program**
   ```bash
   python "eie2108 lab task 3.py"
   ```

### Example

```python
# Example configuration for encoding
fname_in = "myTimg.png"
fname_out = "myTimg_encoded.out"
# encode() - uncomment this line
# decode() - comment this line
```

## 📁 File Structure

```
BVQC-encode-and-decode/
├── eie2108 lab task 3.py      # Main Python script
├── myTimg.png                  # Example input image
├── myTimg_encoded.out          # Example encoded output
├── MyTimg.bvqc3                # Another encoded example
├── MyTimg-bvqc3-R.png          # Decoded/reconstructed image
├── SImg.png                    # Another test image
├── SImg13x14.png               # Test image (13×14)
├── SImg13x14.bvqc3             # Encoded version
├── SImg13x14-bvqc3-R.png       # Decoded version
├── BTC encode and decode.txt   # Additional notes
├── LICENSE
└── README.md
```

## 🎯 How It Works

1. **Encoding Process**:
   - Reads the input image
   - Divides the image into blocks (e.g., 3×3 pixel blocks)
   - Calculates the average RGB value for each block
   - Saves the compressed data to an output file

2. **Decoding Process**:
   - Reads the compressed file
   - Reconstructs the image by filling each block with its average color
   - Saves the reconstructed image

## 📚 Academic Reference

This implementation is based on the BVQC method described in:

> Kuo, K. Y., & Lai, C. Y. (2019, July). The encoding and decoding complexities of entanglement-assisted quantum stabilizer codes. In *2019 IEEE International Symposium on Information Theory (ISIT)* (pp. 2893-2897). IEEE.

## 📄 License

This project is open-source. See the `LICENSE` file for more details.

## 📬 Contact

Created by **LeoTheAuJai**. Feel free to reach out via GitHub.

---
```

---
```
## 📄 README.zh.md (中文版)

```markdown
# 🖼️ BVQC 影像編碼與解碼工具

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

這是一個使用 **BVQC（基於區塊的視覺量化編碼）** 方法實現影像編碼與解碼的 **Python 程式**。它透過分組像素並計算平均顏色值來減少檔案大小，達到有效的影像壓縮。

## 📖 什麼是 BVQC？

**BVQC（Block-based Visual Quantization Coding，基於區塊的視覺量化編碼）** 是一種影像壓縮方法，其原理為：

- 將像素分組為區塊（例如 3×3 = 9 個像素為一組）
- 計算每個區塊的平均顏色值
- 用單一代表色取代整個區塊
- 在維持視覺品質的同時，大幅減少檔案大小

這種技術特別適用於大面積顏色相近的影像。

## ✨ 主要功能

- **編碼模式**：使用 BVQC 方法壓縮影像
- **解碼模式**：將壓縮後的影像還原為可視格式
- **簡單易用**：只需指定輸入和輸出檔名
- **教育意義**：有助於理解影像壓縮的基本原理

## 🛠️ 使用技術

- **語言**：Python 3.7+
- **函式庫**：PIL / Pillow（用於影像處理）
- **演算法**：BVQC（基於區塊的視覺量化編碼）

## 🚀 快速開始

### 環境需求

- Python 3.7 或更高版本
- Pillow 函式庫（`pip install Pillow`）

### 安裝步驟

1. **複製專案**
   ```bash
   git clone https://github.com/LeoTheAuJai/BVQC-encode-and-decode.git
   cd BVQC-encode-and-decode
   ```

2. **安裝依賴套件**
   ```bash
   pip install Pillow
   ```

### 使用方法

1. **開啟 Python 檔案**（`eie2108 lab task 3.py`）在任何文字編輯器或 IDE 中。

2. **調整檔案路徑**：
   - 設定 `fname_in` 為輸入影像的檔名（需與程式在同一目錄）
   - 設定 `fname_out` 為輸出的檔名

3. **選擇模式**：
   - **編碼模式**：取消註解編碼函式，註解解碼函式
   - **解碼模式**：取消註解解碼函式，註解編碼函式

4. **執行程式**
   ```bash
   python "eie2108 lab task 3.py"
   ```

### 範例

```python
# 編碼模式的設定範例
fname_in = "myTimg.png"
fname_out = "myTimg_encoded.out"
# encode() - 取消註解這一行
# decode() - 註解這一行
```

## 📁 檔案結構

```
BVQC-encode-and-decode/
├── eie2108 lab task 3.py      # 主要 Python 程式
├── myTimg.png                  # 範例輸入影像
├── myTimg_encoded.out          # 範例編碼輸出
├── MyTimg.bvqc3                # 另一個編碼範例
├── MyTimg-bvqc3-R.png          # 解碼還原後的影像
├── SImg.png                    # 另一個測試影像
├── SImg13x14.png               # 測試影像（13×14）
├── SImg13x14.bvqc3             # 編碼版本
├── SImg13x14-bvqc3-R.png       # 解碼版本
├── BTC encode and decode.txt   # 額外說明
├── LICENSE
└── README.md
```

## 🎯 運作原理

1. **編碼流程**：
   - 讀取輸入影像
   - 將影像分割為區塊（例如 3×3 像素區塊）
   - 計算每個區塊的 RGB 平均值
   - 將壓縮後的數據儲存到輸出檔案

2. **解碼流程**：
   - 讀取壓縮檔案
   - 用每個區塊的平均顏色重建影像
   - 儲存重建後的影像

## 📚 學術參考

本實作基於以下文獻中描述的 BVQC 方法：

> Kuo, K. Y., & Lai, C. Y. (2019, July). The encoding and decoding complexities of entanglement-assisted quantum stabilizer codes. In *2019 IEEE International Symposium on Information Theory (ISIT)* (pp. 2893-2897). IEEE.

## 📄 授權條款

本專案為開源專案。詳細授權內容請參閱 `LICENSE` 檔案。

## 📬 聯絡我

此專案由 **LeoTheAuJai** 建立。歡迎透過 GitHub 與我聯繫。
