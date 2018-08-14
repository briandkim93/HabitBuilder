let addMenuEl = document.getElementsByClassName('add-menu')[0];
let closeButtonEl = document.getElementsByClassName('close-button')[0];
let daysListEl = document.getElementsByClassName('days-list')[0];
let addHabitEl = document.getElementsByClassName('add-habit')[0];

if (addMenuEl && closeButtonEl && daysListEl && addHabitEl) {
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
    addHabitEl.addEventListener('click', function() {
        console.log('clicked');
        addMenuEl.classList.remove('hidden');
    }, false);
}