# Inside QR

> Building the foundations of a QR Code generator to understand how QR Codes actually work.

![Python](https://img.shields.io/badge/Python-3.13+-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Learning%20Project-success)
![License](https://img.shields.io/badge/License-MIT-green)

## Overview

Most developers generate QR Codes using a single line of code:

```python
import qrcode

img = qrcode.make("Hello World")
```

But that hides an incredible amount of engineering.

I wanted to understand **what actually happens behind that single function call**, so I started building the core components of a QR Code generator myself.

Along the way, I implemented several fundamental building blocks of the QR Code specification, including the matrix structure, finder patterns, timing patterns, separators, and byte-mode encoding.

While building this project, I also discovered why production QR libraries contain thousands of lines of code. Features like Reed–Solomon error correction, masking, BCH encoding, format information, and data placement are significantly more complex than they appear.

This repository documents that journey.

---

# Project Goals

- Understand the internal structure of QR Codes.
- Implement the core QR construction process manually.
- Learn how QR data is encoded.
- Visualize the QR matrix step by step.
- Generate production-ready QR Codes.

---

# Features

## From Scratch

- 21 × 21 Version 1 QR Matrix
- Finder Pattern Generation
- Timing Pattern Generation
- Separator Placement
- Reserved Format Information Areas
- Dark Module
- Byte Mode Encoding
- Modular QR Builder Architecture

## Production QR Generation

- Generate scannable QR Codes
- Supports text and URLs
- Automatic QR Version Selection
- PNG Export
- Production-grade QR generation

---

# Project Structure

```
qr-from-scratch/
│
├── assets/
│
├── output/
│   ├── step1_blank_matrix.png
│   ├── step2_finder_patterns.png
│   ├── step3_timing_patterns.png
│   ├── step4_function_patterns.png
│   ├── final_qr.png
│   └── linkedin_qr.png
│
├── builder.py
├── constants.py
├── encoder.py
├── matrix.py
├── patterns.py
├── real_qr.py
├── renderer.py
├── main.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# QR Construction Progress

This project builds the QR Code layer by layer.

```
Step 1
⬜ Blank Matrix

↓

Step 2
⬛ Finder Patterns

↓

Step 3
⬛ Timing Patterns

↓

Step 4
⬛ Function Patterns

↓

Step 5
🟩 Production QR Code
```

---

# How It Works

## 1. Matrix Creation

The project first creates an empty **21 × 21** matrix representing a Version 1 QR Code.

```
□□□□□□□□□□□□□□□□□□□□□
□□□□□□□□□□□□□□□□□□□□□
□□□□□□□□□□□□□□□□□□□□□
```

---

## 2. Finder Patterns

Three finder patterns are placed in the corners.

These allow scanners to detect:

- Position
- Rotation
- Orientation

---

## 3. Timing Patterns

Alternating black and white modules help scanners determine the size of each module.

```
■ □ ■ □ ■ □ ■
```

---

## 4. Reserved Areas

Certain cells are reserved for:

- Format Information
- Future QR metadata

These cells cannot contain user data.

---

## 5. Byte Mode Encoding

Text is converted into binary.

Example:

```
HELLO

↓

01001000
01000101
01001100
01001100
01001111
```

---

## 6. Production QR Generation

After implementing the core concepts manually, the final QR Code is generated using a production-grade QR library.

This ensures the generated QR follows the complete QR specification and remains compatible with all QR scanners.

---

# Example

Input

```
https://www.linkedin.com/in/your-profile/
```

Output

```
████████████████████████
██ ▄▄▄▄▄ ██▄▀▄█ ▄▄▄▄▄ ██
██ █   █ █ ▄▄▀█ █   █ ██
██ █▄▄▄█ █▄█ ▀█ █▄▄▄█ ██
██▄▄▄▄▄▄▄█ ▀▄█▄▄▄▄▄▄▄███
...
```

Scan →

Opens your LinkedIn profile.

---

# Running the Project

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/qr-from-scratch.git

cd qr-from-scratch
```

Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it

macOS/Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

Example

```
Enter text or URL:

https://www.linkedin.com/in/your-profile/

Output filename:

linkedin_qr
```

Generated file

```
output/linkedin_qr.png
```

---

# Technologies Used

- Python
- Pillow
- qrcode
- Object-Oriented Programming

---

# What I Learned

Building this project taught me that QR Codes are far more sophisticated than they appear.

Some of the biggest takeaways include:

- QR Codes are highly structured data, not random black squares.
- Finder patterns allow scanners to detect orientation.
- Timing patterns determine module spacing.
- Byte mode converts text into binary before placement.
- Much of a QR Code consists of fixed function patterns rather than user data.
- Reed–Solomon error correction is a major reason damaged QR Codes still scan.
- Production QR libraries encapsulate years of engineering and standards compliance.

---

# Future Improvements

- Implement full QR data placement
- Reed–Solomon error correction from scratch
- QR masking algorithms
- BCH format information generation
- Support multiple QR versions
- Support different error correction levels
- Export as SVG
- CLI support

---

# Why This Project Exists

This repository was built as a learning project.

The goal was not to replace mature QR libraries, but to understand the engineering principles behind them.

By implementing the core components manually before using a production library for the final QR generation, I gained a much deeper appreciation for the complexity of the QR Code standard.

---

# License

This project is licensed under the MIT License.

---

## Connect With Me

**Aditya Sharma**

LinkedIn: https://www.linkedin.com/in/aditya-sharma-b04390365/