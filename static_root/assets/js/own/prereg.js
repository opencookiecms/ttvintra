"use strict";
var KTCreateApp = (function () {
    var e,
        t,
        o,
        r,
        a,
        i,
        n = [];
    return {
        init: function () {
            (e = document.querySelector("#kt_modal_create_app")) &&
                (new bootstrap.Modal(e),
                (t = document.querySelector("#kt_modal_create_app_stepper")),
                (o = document.querySelector("#kt_modal_create_app_form")),
                (r = t.querySelector('[data-kt-stepper-action="submit"]')),
                (a = t.querySelector('[data-kt-stepper-action="next"]')),
                (i = new KTStepper(t)).on("kt.stepper.changed", function (e) {
                    3 === i.getCurrentStepIndex()
                        ? (r.classList.remove("d-none"), r.classList.add("d-inline-block"), a.classList.add("d-none"))
                        : 4 === i.getCurrentStepIndex()
                        ? (r.classList.add("d-none"), a.classList.add("d-none"))
                        : (r.classList.remove("d-inline-block"), r.classList.remove("d-none"), a.classList.remove("d-none"));
                }),
                i.on("kt.stepper.next", function (e) {
                    console.log("stepper.next");
                    var t = n[e.getCurrentStepIndex() - 1];
                    t
                        ? t.validate().then(function (t) {
                              console.log("validated!"),
                                  "Valid" == t
                                      ? e.goNext()
                                      : Swal.fire({
                                            text: "Sorry, looks like there are some errors detected, please try again.",
                                            icon: "error",
                                            buttonsStyling: !1,
                                            confirmButtonText: "Ok, got it!",
                                            customClass: { confirmButton: "btn btn-light" },
                                        }).then(function () {});
                          })
                        : (e.goNext(), KTUtil.scrollTop());
                }),
                i.on("kt.stepper.previous", function (e) {
                    console.log("stepper.previous"), e.goPrevious(), KTUtil.scrollTop();
                }),

                r.addEventListener("click", function (e) {
                    e.preventDefault();
                    if(n){
                        n[2].validate().then(function(status){
                            console.log('validate')
                            if(status == 'Valid'){
                                r.setAttribute('data-kt-indicator','on');
                                r.disabled = true;

                                setTimeout(function(){
                                    r.removeAttribute('data-kt-indicator');
                                    r.disabled = false;

                                    Swal.fire({
                                        text : "Your application has been submited",
                                        icon : "success",
                                        buttonsStyling : false,
                                        confirmButtonText:"Okay, Thank you !!!",
                                        customClass:{
                                            confirmButton : "btn btn-primary"
                                        }
                                    }).then(function(result){
                                        if(result.value === true){
                                            o.submit();
                                            r.removeAttribute("data-kt-indicator"),(r.disabled = !1), i.goNext();
                                            console.log("submitted");
                                        }else{
                                            console.log("failed");
                                        }
                                    });

                                },2e3);
                            }else{
                                Swal.fire({
                                    text:"Sorry some other field you not field in",
                                    icon:"error",
                                    buttonsStyling:!1,
                                    confirmButtonText:"Okay, got it",
                                    customClass:{
                                        confirmButton:"btn btn-primary"
                                    }
                                });
                            }
                        });
                    }

                }),
                $(o.querySelector('[name="card_expiry_month"]')).on("change", function () {
                    n[3].revalidateField("card_expiry_month");
                }),
                $(o.querySelector('[name="card_expiry_year"]')).on("change", function () {
                    n[3].revalidateField("card_expiry_year");
                }),
                n.push(
                    FormValidation.formValidation(o, {
                        fields: { name: { validators: { notEmpty: { message: "App name is required" } } }, category: { validators: { notEmpty: { message: "Category is required" } } } },
                        plugins: { trigger: new FormValidation.plugins.Trigger(), bootstrap: new FormValidation.plugins.Bootstrap5({ rowSelector: ".fv-row", eleInvalidClass: "", eleValidClass: "" }) },
                    })
                ),
                n.push(
                    FormValidation.formValidation(o, {
                        fields: { framework: { validators: { notEmpty: { message: "Framework is required" } } } },
                        plugins: { trigger: new FormValidation.plugins.Trigger(), bootstrap: new FormValidation.plugins.Bootstrap5({ rowSelector: ".fv-row", eleInvalidClass: "", eleValidClass: "" }) },
                    })
                ),
                n.push(
                    FormValidation.formValidation(o, {
                        fields: { dbname: { validators: { notEmpty: { message: "Database name is required" } } }, dbengine: { validators: { notEmpty: { message: "Database engine is required" } } } },
                        plugins: { trigger: new FormValidation.plugins.Trigger(), bootstrap: new FormValidation.plugins.Bootstrap5({ rowSelector: ".fv-row", eleInvalidClass: "", eleValidClass: "" }) },
                    })
                ),
                n.push(
                    FormValidation.formValidation(o, {
                        fields: {
                            card_name: { validators: { notEmpty: { message: "Name on card is required" } } },
                            card_number: { validators: { notEmpty: { message: "Card member is required" }, creditCard: { message: "Card number is not valid" } } },
                            card_expiry_month: { validators: { notEmpty: { message: "Month is required" } } },
                            card_expiry_year: { validators: { notEmpty: { message: "Year is required" } } },
                            card_cvv: { validators: { notEmpty: { message: "CVV is required" }, digits: { message: "CVV must contain only digits" }, stringLength: { min: 3, max: 4, message: "CVV must contain 3 to 4 digits only" } } },
                        },
                        plugins: { trigger: new FormValidation.plugins.Trigger(), bootstrap: new FormValidation.plugins.Bootstrap5({ rowSelector: ".fv-row", eleInvalidClass: "", eleValidClass: "" }) },
                    })
                ));
        },
    };
})();
KTUtil.onDOMContentLoaded(function () {
    KTCreateApp.init();
});
