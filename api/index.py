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
        "module_width": 0.33,
        "module_height": 25.0,
        "font_size": 10,
        "text_distance": 3.0,
        "quiet_zone": 6.5,
        "dpi": 203,
        "write_text": True
    }

    code = barcode.get("code128", texto, writer= writer)
    buffer = io.BytesIO()
    code.write(buffer)
    buffer.seek(0)

    return send_file(buffer, mimetype="image/png")