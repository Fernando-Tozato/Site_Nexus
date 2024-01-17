document.addEventListener('DOMContentLoaded',function(){
    const tableOptions = document.querySelectorAll('.table_options');
    const table = document.querySelector('#main_table');
    
    tableOptions.forEach(function(option) {
        option.addEventListener('mouseover', function() {
            tableOptions.forEach(function(otherOption) {
                if (otherOption != option) {
                    otherOption.style.filter = 'brightness(50%)';
                }
                table.style.filter = 'brightness(50)%';
            });
        });

        option.addEventListener('mouseout', function(){
            tableOptions.forEach(function(otherOption) {
                otherOption.style.filter = 'brightness(100%)';
                table.style.filter = 'brightness(100)%';
            });
        });
    });
});

function profile_click() {

}

function distance_click() {

}

function iconClicked(element) {
    element.classList.toggle('fa-regular')
    element.classList.toggle('fa-solid')
    element.classList.toggle('clicked') 
}