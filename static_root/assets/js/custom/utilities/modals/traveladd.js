"use strict";
var KTCreateAccount = (function () {
    var e,
        t,
        i,
        o,
        s,
       
        r,
        a = [];
    return {
        init: function () {
            (e = document.querySelector("#kt_modal_create_account")) && new bootstrap.Modal(e),
                (t = document.querySelector("#kt_create_account_stepper")),
                (i = t.querySelector("#kt_create_account_form")),
                (o = t.querySelector('[data-kt-stepper-action="submit"]')),
                (s = t.querySelector('[data-kt-stepper-action="next"]')),
                (r = new KTStepper(t)).on("kt.stepper.changed", function (e) {
                    6 === r.getCurrentStepIndex()
                        ? (o.classList.remove("d-none"), o.classList.add("d-inline-block"), s.classList.add("d-none"))
                        : 7 === r.getCurrentStepIndex()
                        ? (o.classList.add("d-none"), s.classList.add("d-none"))
                        : (o.classList.remove("d-inline-block"), o.classList.remove("d-none"), s.classList.remove("d-none"));
                }),
                r.on("kt.stepper.next", function (e) {
                    console.log("stepper.next");
                    var t = a[e.getCurrentStepIndex() - 1];
                    t
                        ? t.validate().then(function (t) {
                              console.log("validated!"),
                                  "Valid" == t
                                      ? (e.goNext(), KTUtil.scrollTop())
                                      : Swal.fire({
                                            text: " again.",
                                            icon: "error",
                                            buttonsStyling: !1,
                                            confirmButtonText: "Ok, got it!",
                                            customClass: { confirmButton: "btn btn-light" },
                                        }).then(function () {
                                            KTUtil.scrollTop();
                                        });
                          })
                        : (e.goNext(), KTUtil.scrollTop());
                }),
                r.on("kt.stepper.previous", function (e) {
                    console.log("stepper.previous"), e.goPrevious(), KTUtil.scrollTop();
                }),
                a.push(
                    FormValidation.formValidation(i, {
                        fields: { companyname: { validators: { notEmpty: { message: "Company Name is required" } } } },
                        plugins: { trigger: new FormValidation.plugins.Trigger(), bootstrap: new FormValidation.plugins.Bootstrap5({ rowSelector: ".fv-row", eleInvalidClass: "", eleValidClass: "" }) },
                    })
                ),
                a.push(
                    FormValidation.formValidation(i, {
                        fields: {
                            name: { validators: { notEmpty: { message: "Name is Required" } } },
                            travelpurpose: { validators: { notEmpty: { message: "Why you want to travel, please describe" } } },
                           
                           
                        },
                        plugins: { trigger: new FormValidation.plugins.Trigger(), bootstrap: new FormValidation.plugins.Bootstrap5({ rowSelector: ".fv-row", eleInvalidClass: "", eleValidClass: "" }) },
                    })
                ),
                a.push(
                    FormValidation.formValidation(i, {
                        fields: {
                            destinations: { validators: { notEmpty: { message: "Your Destination ?" } } },
                            datearrive: { validators: { notEmpty: { message: "When you want start travel" } } },
                            datereturn: { validators: { notEmpty: { message: "Estimate date you want to return" } } },
      
                        },
                        plugins: { trigger: new FormValidation.plugins.Trigger(), bootstrap: new FormValidation.plugins.Bootstrap5({ rowSelector: ".fv-row", eleInvalidClass: "", eleValidClass: "" }) },
                    })
                ),
                a.push(
                    FormValidation.formValidation(i, {
                        fields: {
                         
                           
                        },
                        plugins: { trigger: new FormValidation.plugins.Trigger(), bootstrap: new FormValidation.plugins.Bootstrap5({ rowSelector: ".fv-row", eleInvalidClass: "", eleValidClass: "" }) },
                    })
                ),
                a.push(
                    FormValidation.formValidation(i, {
                        fields: {
                            hotelneeded: { validators: { notEmpty: { message: "Yes or No ?" } } },
                            numbernights: { validators: { notEmpty: { message: "No of night ?" } } },
                           
                        },
                        plugins: { trigger: new FormValidation.plugins.Trigger(), bootstrap: new FormValidation.plugins.Bootstrap5({ rowSelector: ".fv-row", eleInvalidClass: "", eleValidClass: "" }) },
                    })
                ),
                a.push(
                    FormValidation.formValidation(i, {
                        fields: {
                            hodapproval: { validators: { notEmpty: { message: "oops!! You need the HOD Approval" } } },
                            directorapproval: { validators: { notEmpty: { message: "oops!! You aslo need Director Approval" } } },
                           
                        },
                        plugins: { trigger: new FormValidation.plugins.Trigger(), bootstrap: new FormValidation.plugins.Bootstrap5({ rowSelector: ".fv-row", eleInvalidClass: "", eleValidClass: "" }) },
                    })
                ),

                

                o.addEventListener('click', function (e) {
                    // Prevent default button action
                    e.preventDefault();
                    
                  
                    if (a) {
                        a[5].validate().then(function (status) {
                            console.log('validated!');
                
                            if (status == 'Valid') {
                                // Show loading indication
                                o.setAttribute('data-kt-indicator', 'on');
                
                                // Disable button to avoid multiple click
                                o.disabled = true;
                
                                // Simulate form submission. For more info check the plugin's official documentation: https://sweetalert2.github.io/
                                setTimeout(function () {
                                    // Remove loading indication
                                    o.removeAttribute('data-kt-indicator');
                
                                    // Enable button
                                    o.disabled = false;
                
                                    // Show popup confirmation
                                    Swal.fire({
                                        text: "Form has been successfully submitted!",
                                        icon: "success",
                                        buttonsStyling: false,
                                        confirmButtonText: "Ok, got it!",
                                        customClass: {
                                            confirmButton: "btn btn-primary"
                                        }
                                    }).then(function (result){
                                        if(result.value === true){
                                        
                                       
                                        i.submit();
                                        o.removeAttribute("data-kt-indicator"), (o.disabled = !1), r.goNext();
                                        console.log("Submitted");
                                        
                                        }else{
                                            console.log("failed");
                                        
                                       
                                      }
                                    });
                
                                    //form.submit(); // Submit form
                                },2e3);
                            }
                            else{
                                Swal.fire({
                                    text: "Sorry, looks like there are some errors detected, please try again.",
                                    icon: "error",
                                    buttonsStyling: !1,
                                    confirmButtonText: "Ok, got it!",
                                    customClass: { confirmButton: "btn btn-primary" },
                                });
                            }
                        });
                    }
                }),
                
               
                $(i.querySelector('[name="hodapproval"]')).on("change", function () {
                    a[5].revalidateField("hodapproval");
                }),
                $(i.querySelector('[name="director"]')).on("change", function () {
                    a[5].revalidateField("director");
                });
   
        },
    };
})();



KTUtil.onDOMContentLoaded(function () {
    KTCreateAccount.init();
});



