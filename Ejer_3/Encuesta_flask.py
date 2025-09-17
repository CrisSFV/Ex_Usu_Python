from flask import request, render_template_string

def calcular_puntaje(correctas, incorrectas, blanco):
    return correctas * 3 + incorrectas * -1 + blanco * 0

encuesta_html = """
<!DOCTYPE html>
<html lang='es'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <title>Encuesta Postulantes</title>
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
            <h2 class='title text-center mb-4'>Encuesta de Postulantes</h2>
            <form method='post'>
                <div class='mb-3'>
                    <label for='correctas' class='form-label'>Respuestas correctas:</label>
                    <input type='number' class='form-control' id='correctas' name='correctas' required>
                </div>
                <div class='mb-3'>
                    <label for='incorrectas' class='form-label'>Respuestas incorrectas:</label>
                    <input type='number' class='form-control' id='incorrectas' name='incorrectas' required>
                </div>
                <div class='mb-3'>
                    <label for='blanco' class='form-label'>Respuestas en blanco:</label>
                    <input type='number' class='form-control' id='blanco' name='blanco' required>
                </div>
                <button type='submit' class='btn btn-primary w-100'>Calcular puntaje</button>
            </form>
            {% if puntaje is not none %}
                <div class='alert alert-success mt-4 text-center'>
                    <strong>Puntaje final:</strong> {{ puntaje }}
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
    puntaje = None
    if request.method == 'POST':
        try:
            correctas = int(request.form.get('correctas', 0))
            incorrectas = int(request.form.get('incorrectas', 0))
            blanco = int(request.form.get('blanco', 0))
            puntaje = calcular_puntaje(correctas, incorrectas, blanco)
        except Exception:
            puntaje = 'Error en los datos ingresados.'
    return render_template_string(encuesta_html, puntaje=puntaje)
