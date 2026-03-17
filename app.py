from flask import Flask, request, send_file
from pypdf import PdfReader, PdfWriter
import os

app = Flask(__name__)

TEMPLATE = "template.pdf"
PASSWORD = "SELL@2209"

slots = {
    9: "output1.pdf",
    13: "output2.pdf",
    17: "output3.pdf",
    20: "output4.pdf",
    23: "output5.pdf",
    26: "output6.pdf"
}

os.makedirs("uploads", exist_ok=True)
os.makedirs("final", exist_ok=True)


@app.route("/")
def home():
    return '''
    <h1>Record Generator</h1>
    <h3>Developed by SELLVESH</h3>

    <form method="POST" action="/generate" enctype="multipart/form-data">

    Student Name: <input type="text" name="name" required><br><br>

    Output1: <input type="file" name="output1"><br><br>
    Output2: <input type="file" name="output2"><br><br>
    Output3: <input type="file" name="output3"><br><br>
    Output4: <input type="file" name="output4"><br><br>
    Output5: <input type="file" name="output5"><br><br>
    Output6: <input type="file" name="output6"><br><br>

    <input type="submit" value="Generate Record">

    </form>
    '''


@app.route("/generate", methods=["POST"])
def generate():

    name = request.form["name"]

    template = PdfReader(TEMPLATE)
    writer = PdfWriter()

    # save uploaded outputs
    for key in request.files:
        file = request.files[key]

        if file and file.filename != "":
            path = f"uploads/{name}_{key}.pdf"
            file.save(path)

    # merge template + outputs
    for i, page in enumerate(template.pages, start=1):

        writer.add_page(page)

        if i in slots:

            path = f"uploads/{name}_" + slots[i]

            if os.path.exists(path):

                output_pdf = PdfReader(path)

                for p in output_pdf.pages:
                    writer.add_page(p)

    # encrypt PDF
    writer.encrypt(PASSWORD)

    final_file = f"final/{name}.pdf"

    with open(final_file, "wb") as f:
        writer.write(f)

    return f'''
    <h2>Record Generated Successfully!</h2>

    <a href="/download/{name}">
    <button style="font-size:20px;padding:10px;">
    Download PDF
    </button>
    </a>
    '''


@app.route("/download/<name>")
def download(name):

    file_path = f"final/{name}.pdf"

    if os.path.exists(file_path):
        return send_file(file_path)

    return "File not ready yet"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
