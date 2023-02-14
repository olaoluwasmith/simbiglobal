const profit = document.querySelectorAll('.profit');

profit.forEach(function (pro) {
    if (pro.textContent > 0) {
        pro.style.color = 'green';
    } 
    if (pro.textContent < 0) {
        pro.style.color = 'red';   
    } 
});