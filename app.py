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
    try:
        lam = int(request.args.get('lambda'))
        alpha = int(request.args.get('alpha'))
        beta = int(request.args.get('beta'))
        delta = int(request.args.get('delta'))
        mu = int(request.args.get('mu'))
    except TypeError:
        return "Required parameters not found: lambda, alpha, beta, delta, mu", 400

    if not verify_param_domains(lam=lam, delta=delta, alpha=alpha, beta=beta):
        return "Invalid domains for at least one parameter", 400

    print(lam)

    return jsonify(lam=lam,
                   alpha=alpha,
                   beta=beta,
                   delta=delta,
                   mu=mu)


def verify_param_domains(lam, delta, alpha, beta):
    if lam > 0:
        return (delta >= 0 and
                alpha > 0 and
                -alpha < beta < alpha)
    elif lam == 0:
        return (delta > 0 and
                alpha > 0 and
                -alpha < beta < alpha)
    else:
        return (delta > 0 and
                alpha >= 0 and
                -alpha <= beta <= alpha)


if __name__ == '__main__':
    app.run(DEBUG=True)
