
from flask import request, render_template_string

def calcular_distancia(velocidad, tiempo):
    return velocidad * tiempo

fisica_html = """
<!DOCTYPE html>
<html lang='es'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <title>Ejercicio Física</title>
    <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css' rel='stylesheet'>
    <style>
        body { background: linear-gradient(135deg, #f8fafc 0%, #e0e7ff 100%); min-height: 100vh; }
        .card { max-width: 400px; margin: 60px auto; box-shadow: 0 4px 24px rgba(0,0,0,0.08); border-radius: 16px; }
        .title { font-weight: 700; color: #3b82f6; }
    </style>
</head>
<body>
    <div class='container'>
        <div class='card bg-white p-4'>
            <h2 class='title text-center mb-4'>Física: Distancia Recorrida</h2>
            <form method='post'>
                <div class='mb-3'>
                    <label for='velocidad' class='form-label'>Velocidad (m/s):</label>
                    <input type='number' step='any' class='form-control' id='velocidad' name='velocidad' required>
                </div>
                <div class='mb-3'>
                    <label for='tiempo' class='form-label'>Tiempo (s):</label>
                    <input type='number' step='any' class='form-control' id='tiempo' name='tiempo' required>
                </div>
                <button type='submit' class='btn btn-primary w-100'>Calcular</button>
            </form>
            {% if distancia is not none %}
                <div class='alert alert-success mt-4 text-center'>
                    <strong>Distancia recorrida:</strong> {{ distancia }} metros
                </div>
            {% endif %}
            <a href='/' class='btn btn-outline-secondary w-100 mt-3'>Regresar al menú</a>
        </div>
    </div>
    <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js'></script>
</body>
</html>
"""

def main():
    distancia = None
    if request.method == 'POST':
        try:
            velocidad = float(request.form.get('velocidad', 0))
            tiempo = float(request.form.get('tiempo', 0))
            distancia = calcular_distancia(velocidad, tiempo)
        except Exception:
            distancia = 'Error en los datos ingresados.'
    return render_template_string(fisica_html, distancia=distancia)