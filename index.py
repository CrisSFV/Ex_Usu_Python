from flask import Flask, render_template_string

app = Flask(__name__)

menu_html = """
<!DOCTYPE html>
<html lang='es'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <title>Menú de Ejercicios</title>
    <link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css' rel='stylesheet'>
    <style>
        body {
            background: linear-gradient(135deg, #f8fafc 0%, #e0e7ff 100%);
            min-height: 100vh;
        }
        .menu-card {
            max-width: 400px;
            margin: 60px auto;
            box-shadow: 0 4px 24px rgba(0,0,0,0.08);
            border-radius: 16px;
        }
        .menu-title {
            font-weight: 700;
            color: #3b82f6;
        }
    </style>
</head>
<body>
    <div class='container'>
        <div class='menu-card bg-white p-4'>
            <h1 class='menu-title text-center mb-4'>Menú Principal</h1>
            <h4 class='text-center mb-4'>Cristian Santana</h4>
            <div class='d-grid gap-3'>
                <a href='/ejer_1' class='btn btn-primary btn-lg'>Ejercicio 1</a>
                <a href='/ejer_2' class='btn btn-success btn-lg'>Ejercicio 2</a>
                <a href='/ejer_3' class='btn btn-warning btn-lg'>Ejercicio 3</a>
            </div>
        </div>
    </div>
    <script src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js'></script>
</body>
</html>
"""

@app.route('/')
def menu():
    return render_template_string(menu_html)

@app.route('/ejer_1', methods=['GET', 'POST'])
def ejer_1():
    from Ejer_1.Fisica import main
    return main()

@app.route('/ejer_2', methods=['GET', 'POST'])
def ejer_2():
    from Ejer_2.Promedio import main
    return main()

@app.route('/ejer_3', methods=['GET', 'POST'])
def ejer_3():
    from Ejer_3.Encuesta import main
    return main()

if __name__ == '__main__':
    app.run(debug=True)