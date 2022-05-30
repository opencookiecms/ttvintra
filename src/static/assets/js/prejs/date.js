"use strict";


$("#id_request_date").flatpickr();
$("#id_shipment_date").flatpickr();
$("#id_date").flatpickr({
    defaultDate: "today",
});
$("#id_datearrive").flatpickr();
$("#id_timearrive").flatpickr({
    enableTime: true,
    noCalendar: true,
    dateFormat: "H:i",
    defaultDate:'null'
});

$("#id_datereturn").flatpickr();
$("#id_timereturn").flatpickr({
    enableTime: true,
    noCalendar: true,
    dateFormat: "H:i",
    defaultDate:'null'
});
