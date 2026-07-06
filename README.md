📄 Record Generator

A simple web-based PDF Record Generator developed using Flask and PyPDF.

This application helps students automatically merge their laboratory output PDFs into the correct pages of a predefined record template and generate a final password-protected record PDF.

🚀 Features
Upload up to 6 output PDFs.
Automatically inserts each output into its assigned record page.
Generates a single consolidated record PDF.
Password-protects the generated PDF.
Simple and user-friendly web interface.
Saves time by eliminating manual PDF editing.
🛠️ Technologies Used
Python
Flask
PyPDF
HTML
📂 Project Structure
project/
│
├── app.py
├── template.pdf
├── uploads/
├── final/
├── requirements.txt
└── README.md
📋 How It Works
Enter the student name.
Upload the required output PDFs.
Click Generate Record.
The system:
Reads the template PDF.
Inserts uploaded outputs into predefined locations.
Creates a final merged PDF.
Encrypts the PDF with a password.
Download the generated record.
🔐 PDF Password

The generated PDF is protected using a password configured in the source code.

PASSWORD = "YOUR_PASSWORD"
⚙️ Installation

Clone the repository:

git clone https://github.com/your-username/record-generator.git
cd record-generator

Install dependencies:

pip install -r requirements.txt
▶️ Run the Application
python app.py

Open your browser and visit:

http://localhost:5000
📦 Requirements
Flask
pypdf

or install directly:

pip install flask pypdf
🎯 Use Case

This project was developed to help students quickly generate laboratory record PDFs by automatically placing experiment outputs in their respective sections of the record template.

Instead of manually editing PDFs and arranging pages, students can upload their outputs and receive a ready-to-submit record within seconds.

👨‍💻 Developer

Sellvesh

Electrical and Electronics Engineering Student

Passionate about developing practical solutions that simplify academic and engineering workflows.

📜 License

This project is open-source and available for educational purposes.
