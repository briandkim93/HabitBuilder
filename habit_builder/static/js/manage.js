let add_menu_el = document.getElementsByClassName('add-menu')[0];
let close_button_el = document.getElementsByClassName('close-button')[0];
let days_list_el = document.getElementsByClassName('days-list')[0];

if (add_menu_el && close_button_el && days_list_el) {
    close_button_el.addEventListener('click', function() {
        add_menu_el.classList.add('hidden');
    }, false);

    days_list_el.addEventListener('click', function(event) {
        day_item_el = event.target;
        if (day_item_el.classList.contains('selected')) {
            day_item_el.classList.remove('selected');
        } else {
            day_item_el.classList.add('selected');
        }
    }, true);
}