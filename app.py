from flask import Flask, render_template, request

app = Flask(__name__,
            template_folder='templates',
            static_folder='static',
            static_url_path='/static')


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('generate-data', methods=["GET"])
def generate_data():
    try:
        lam = request.args.get('lambda')
        alpha = request.args.get('alpha')
        delta = request.args.get('delta')
        beta = request.args.get('beta')
        mu = request.args.get('mu')
    except ValueError:
        return "Required parameters not found: lambda, alpha, beta, delta, mu", 400

    print(lam)


if __name__ == '__main__':
    app.run(DEBUG=True)
