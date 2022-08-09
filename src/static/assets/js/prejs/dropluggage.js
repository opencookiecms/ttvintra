"use strict";
var KTAppTravelSaveCategory = (function () {
    const e = () => {
            $("#kt_travel_conditions2").repeater({
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
                    const e = document.querySelectorAll('[name="luggageneeded"][type="radio"]'),
                        t = document.querySelector('[data-option-select="Yes"]');
                    e.forEach((e) => {
                        e.addEventListener("change", (e) => {
                            "Yes" === e.target.value ? t.classList.remove("d-none") : t.classList.add("d-none");
                        });
                    });
                })();    
        },
    };
})();
KTUtil.onDOMContentLoaded(function () {
    KTAppTravelSaveCategory.init();
});
