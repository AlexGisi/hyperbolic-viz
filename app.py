from flask import Flask, render_template, request, jsonify, Blueprint
from scipy import stats

hyperbolic_viz = Blueprint('hyperbolic-viz',
                           __name__,
                           template_folder='templates',
                           static_folder='static',
                           static_url_path='/h-v/static')


@hyperbolic_viz.route('/hyperbolic')
def hello_world():
    return render_template('index.html')


@hyperbolic_viz.route('/generate-data', methods=["GET"])
def generate_data():
    try:
        lam = float(request.args.get('lambda'))
        alpha = float(request.args.get('alpha'))
        beta = float(request.args.get('beta'))
        delta = float(request.args.get('delta'))
        mu = float(request.args.get('mu'))
    except TypeError:
        return "Required parameters not found: lambda, alpha, beta, delta, mu", 400

    if not verify_param_domains(lam=lam, delta=delta, alpha=alpha, beta=beta):
        return "Invalid domains for at least one parameter", 400

    res = {"is_implemented": True, "x_arr": [], "y_arr": []}

    res["x_arr"], res["y_arr"] = gen_distribution(lam=lam,
                                                  alpha=alpha,
                                                  beta=beta,
                                                  mu=mu,
                                                  delta=delta)

    return jsonify(res)


def gen_distribution(lam, alpha, beta, mu, delta):
    x_arr = []
    y_arr = []

    a = alpha * delta
    b = beta * delta

    for x in range(-100, 100, 1):
        x_arr.append(x / 100)
        y_arr.append(stats.genhyperbolic.pdf(x / 100,
                          p=lam,
                          a=a,
                          b=b,
                          loc=mu,
                          scale=delta))

    return x_arr, y_arr


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


def is_sl(lam, delta, beta, mu):
    if lam == 0 and delta == 0 and beta == 0 and mu == 0:
        return True
    else:
        return False


def is_t(lam, alpha, beta, mu):
    if lam < 0 and alpha == 0 and beta == 0 and mu == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(hyperbolic_viz)

    app.run()
