from flask import Flask, request, send_file, abort
import barcode
from barcode.writer import ImageWriter
import io

app = Flask(__name__)

@app.route("/")
def home():
    return "API funcionando"

@app.route("/barcode")
def gerar_barcode():
    texto = request.args.get("text")
    if not texto:
        abort(400, "Parâmetro 'text' é obrigatório")
    writer = ImageWriter()
    writer_options = {
        "module_width": 1.5,
        "module_height": 80.0,
        "font_size": 20,
        "text_distance": 6.0,
        "quiet_zone": 10,
        "dpi": 300,
        "write_text": True
    }

    code = barcode.get("code128", texto, writer= writer)
    buffer = io.BytesIO()
    code.write(buffer)
    buffer.seek(0)

    return send_file(buffer, mimetype="image/png")