
$(function() {

$('#pick_up_location').closest('div').toggleClass('position-relative');

$('#pick_up_location').datetimepicker({
  minDate: new Date(),
  format: 'YYYY-MM-DD HH:mm',
  icons: {
      time: 'fas fa-clock',
      date: 'fas fa-calendar',
      up: 'fas fa-arrow-up',
      down: 'fas fa-arrow-down',
      previous: 'fas fa-chevron-left',
      next: 'fas fa-chevron-right',
      today: 'fas fa-calendar-check-o',
      clear: 'fas fa-delete',
      close: 'fas fa-times'
    },
});
});

