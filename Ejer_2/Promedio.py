
from flask import request, render_template_string

promedio_html = """
<!DOCTYPE html>
<html lang='es'>
<head>
	<meta charset='UTF-8'>
	<meta name='viewport' content='width=device-width, initial-scale=1'>
	<title>Ejercicio Promedio</title>
	<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css' rel='stylesheet'>
	<style>
		body { background: linear-gradient(135deg, #f8fafc 0%, #e0e7ff 100%); min-height: 100vh; }
		.card { max-width: 400px; margin: 60px auto; box-shadow: 0 4px 24px rgba(0,0,0,0.08); border-radius: 16px; }
		.title { font-weight: 700; color: #16a34a; }
	</style>
</head>
<body>
	<div class='container'>
		<div class='card bg-white p-4'>
			<h2 class='title text-center mb-4'>Promedio de Notas</h2>
			<form method='post'>
				<div class='mb-3'>
					<label for='nota1' class='form-label'>Primera nota parcial:</label>
					<input type='number' step='any' class='form-control' id='nota1' name='nota1' required>
				</div>
				<div class='mb-3'>
					<label for='nota2' class='form-label'>Segunda nota parcial:</label>
					<input type='number' step='any' class='form-control' id='nota2' name='nota2' required>
				</div>
				<div class='mb-3'>
					<label for='nota3' class='form-label'>Tercera nota parcial:</label>
					<input type='number' step='any' class='form-control' id='nota3' name='nota3' required>
				</div>
				<button type='submit' class='btn btn-success w-100'>Calcular promedio</button>
			</form>
			{% if promedio is not none %}
				<div class='alert alert-info mt-4 text-center'>
					<strong>Promedio:</strong> {{ promedio }}
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
	promedio = None
	if request.method == 'POST':
		try:
			nota1 = float(request.form.get('nota1', 0))
			nota2 = float(request.form.get('nota2', 0))
			nota3 = float(request.form.get('nota3', 0))
			promedio = round((nota1 + nota2 + nota3) / 3, 2)
		except Exception:
			promedio = 'Error en los datos ingresados.'
	return render_template_string(promedio_html, promedio=promedio)