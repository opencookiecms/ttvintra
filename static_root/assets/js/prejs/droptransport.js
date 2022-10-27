"use strict";
var KTAppTravelSaveCategory = (function () {
    const e = () => {
            $("#kt_travel_conditions").repeater({
                initEmpty: !1,
                defaultValues: { "text-input": "foo" },
                show: function () {
                    $(this).slideDown(), t();
                },
                hide: function (e) {
                    $(this).slideUp(e);
                },
            });
        },
        t = () => {
          
    
        };
    return {
        init: function () {

            e(),
            t(),

                (() => {
                    const e = document.querySelectorAll('[name="transport"][type="radio"]'),
                        t = document.querySelector('[data-option-select="flight"]');
                    e.forEach((e) => {
                        e.addEventListener("change", (e) => {
                            "Flight" === e.target.value ? t.classList.remove("d-none") : t.classList.add("d-none");
                        });
                    });
                })();    
        },
    };
})();
KTUtil.onDOMContentLoaded(function () {
    KTAppTravelSaveCategory.init();
});
