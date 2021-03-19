from flask import Flask, render_template, request, jsonify

app = Flask(__name__,
            template_folder='templates',
            static_folder='static',
            static_url_path='/static')


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/generate-data', methods=["GET"])
def generate_data():
    lam = request.args.get('lambda')
    alpha = request.args.get('alpha')
    beta = request.args.get('beta')
    delta = request.args.get('delta')
    mu = request.args.get('mu')

    if not (lam and alpha and beta and delta and mu):
        return "Required parameters not found: lambda, alpha, beta, delta, mu", 400

    print(lam)

    return jsonify(lam=lam,
                   alpha=alpha,
                   beta=beta,
                   delta=delta,
                   mu=mu)


if __name__ == '__main__':
    app.run(DEBUG=True)
