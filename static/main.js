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

async function get_data() {
    let response = await fetch('/generate-data?' + new URLSearchParams({
        lambda: 1,
        alpha: 2,
        beta: 1,
        delta: 4,
        mu: 0,
    }));

    if(response.ok) {
        let json = await response.json();
        draw(json)
    } else{
        console.log("HTTP Error: " + response.status)
    }
}

function draw(data) {
    for(let key in data) {
        if (!data.hasOwnProperty(key)) continue;

        console.log(key + ": " + data[key])
    }
}

get_data();
