noHabitsEl = document.getElementsByClassName('no-habits-container')[0];
habitsListEl = document.getElementsByClassName('habits-list')[0];

if (noHabitsEl && habitsListEl) {
    if (habitsListEl.getElementsByTagName('li').length == 1) {
       noHabitsEl.classList.remove('hidden'); 
    }
}