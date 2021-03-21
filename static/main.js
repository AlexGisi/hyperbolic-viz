let ctx = document.getElementById('vizChart').getContext('2d');
let chart = new Chart(ctx, {
    type: 'line',
    data: {
        datasets: [{
            data: [{
                x: 0,
                y: 0.1,
            },
                {
                    x: 0.5,
                    y: 1
                }]

        }]
    },
    options: {
        responsive: true,
        title: {
            display: true,
        },
        legend: {
            display: false,
        },
        scales: {
            xAxes: [{
                offset: true,
                scaleLabel: {
                    display: true,
                },
                ticks: {
                    min: 0,
                    max: 1,
                }
            }],
            yAxes: [{
                display: true,
                ticks: {
                    beginAtZero: true,
                }
            }]
        }
    }
});

async function get_data(l, a, b, d, m) {
    let response = await fetch('/generate-data?' + new URLSearchParams({
        lambda: l,
        alpha: a,
        beta: b,
        delta: d,
        mu: m,
    }));

    if(response.ok) {
        let json = await response.json();
        draw(json)
    } else {
        show_e("Bad input");
        console.log("HTTP Error: " + response.status)
    }
}

function draw(data) {
    for(let key in data) {
        if (!data.hasOwnProperty(key)) continue;

        console.log(key + ": " + data[key])
    }
}

let e_div = document.getElementById('error');
let sels = document.querySelectorAll('input');
let lambda_sel = document.getElementById('lambda');
let alpha_sel = document.getElementById('alpha');
let beta_sel = document.getElementById('beta');
let delta_sel = document.getElementById('delta');
let mu_sel = document.getElementById('mu');

function val_change() {
    hide_e();
    get_data(lambda_sel.value,
             alpha_sel.value,
             beta_sel.value,
             delta_sel.value,
             mu_sel.value);
}

function hide_e() {
    e_div.style.display = "none";
}

function show_e(text) {
    e_div.style.display = "flex";
    document.getElementById('error-text').innerText = "Error: " + text;
}

hide_e();
