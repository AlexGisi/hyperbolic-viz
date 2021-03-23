let ctx = document.getElementById('vizChart').getContext('2d');
let chart = new Chart(ctx, {
    type: 'line',
    data: {
        datasets: [{
            data: []
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
                    min: -1,
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
        alert("Bad Input");
        console.log("HTTP Error: " + response.status)
    }
}

function draw(data) {
    for(let key in data) {
        if (!data.hasOwnProperty(key)) continue;

        console.log(key + ": " + data[key])
    }
}

let sels = document.querySelectorAll('input');
let lambda_sel = document.getElementById('lambda');
let alpha_sel = document.getElementById('alpha');
let beta_sel = document.getElementById('beta');
let delta_sel = document.getElementById('delta');
let mu_sel = document.getElementById('mu');

let btns = document.querySelectorAll('button');
let hyper_btn = document.getElementById("hyper-btn");
let sl_btn = document.getElementById('sl-btn');
let st_btn = document.getElementById('st-btn');
let nig_btn = document.getElementById('nig-btn');

let a_b_error = document.getElementById('a-b-error');

function is_a_b_error() {
    if(!(-parseFloat(alpha_sel.value) < parseFloat(beta_sel.value) &&
         parseFloat(beta_sel.value) < parseFloat(alpha_sel.value))) {
        a_b_error.style.display = 'inline';
        return true;
    } else {
        a_b_error.style.display = 'none';
        return false;
    }
}
function val_change() {
    if(!is_a_b_error()) {
        get_data(lambda_sel.value,
            alpha_sel.value,
            beta_sel.value,
            delta_sel.value,
            mu_sel.value);
    }
}

function onclick_hyper() {
    click(hyper_btn)
}

function onclick_sl() {
    click(sl_btn)
}

function onclick_st() {
    click(st_btn)
}

function onclick_nig() {
    click(nig_btn)
}

function click(btn) {
    for(let i=0; i < btns.length; i++) {
        if(!(i === Array.from(btns).indexOf(btn))) unlock(btns[i])
    }
    if (btn.classList.contains("sel")) {
        unlock(btn);
    } else {
        lock(btn);
    }
}

function lock(btn) {
    if(btn.id === "hyper-btn") {
        alert("Not Yet Implemented")
    } else if(btn.id === "sl-btn") {
        alert("Not Yet Implemented")
    } else if(btn.id === "st-btn") {
        alert("Not Yet Implemented")
    } else if(btn.id === "nig-btn") {
        btn.classList.add("sel");
        lambda_sel.disabled = true;
        lambda_sel.value = -0.5;
        delta_sel.min = 0.0000001;
        alpha_sel.min = 0;
        beta_sel.value = 0.01;
        alpha_sel.value = 0.1;
        delta_sel.value = 0.1
    }
}

function unlock(btn) {
    btn.classList.remove("sel");
    if(btn.id === "hyper-btn") {

    } else if(btn.id === "sl-btn") {

    } else if(btn.id === "st-btn") {

    } else if(btn.id === "nig-btn") {
        lambda_sel.disabled = false;
        delta_sel.removeAttribute('min');
        alpha_sel.removeAttribute('min');

    }
}

click(nig_btn);
is_a_b_error();
