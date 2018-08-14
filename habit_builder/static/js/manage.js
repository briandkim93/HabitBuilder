let addMenuEl = document.getElementsByClassName('add-menu')[0];
let closeButtonEl = document.getElementsByClassName('close-button')[0];
let daysListEl = document.getElementsByClassName('days-list')[0];
let addCellEl = document.getElementsByClassName('add-cell')[0];

if (addMenuEl && closeButtonEl && daysListEl && addCellEl) {
    closeButtonEl.addEventListener('click', function() {
        addMenuEl.classList.add('hidden');
    }, false);

    daysListEl.addEventListener('click', function(event) {
        dayItemEl = event.target;
        if (dayItemEl.nodeName == 'LABEL') {
            if (dayItemEl.classList.contains('selected')) {
                dayItemEl.classList.remove('selected');
            } else {
                dayItemEl.classList.add('selected');
            }
        }
    }, true);
    addCellEl.addEventListener('click', function() {
        addMenuEl.classList.remove('hidden');
    }, false);
}