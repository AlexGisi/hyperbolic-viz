from flask import Flask, render_template, request, jsonify
from scipy import stats

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
        lam = float(request.args.get('lambda'))
        alpha = float(request.args.get('alpha'))
        beta = float(request.args.get('beta'))
        delta = float(request.args.get('delta'))
        mu = float(request.args.get('mu'))
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


def generate_student_t():
    """
    # The student t distribution is obtained for lambda<1, alpha=beta=mu=0.
    :return:
    """
    pass


def generate_norm_inv_gaussian(alpha, beta, mu, delta):
    """
    The NIG is obtained for lambda=-1/2
    scipy.stats.norminvgauss
    :return:
    """
    x_arr = []
    y_arr = []

    for x in range(-10, 10, 1):
        x_arr.append(x/100)
        y_arr.append(stats.norminvgauss.pdf(x/100,
                                            a=alpha,
                                            b=beta,
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


if __name__ == '__main__':
    app.run(DEBUG=True)
