'use strict'
$(document).ready(function(){
    $('#id_hodapproval').change(function(){
        var id = $('#id_hodapproval').val();
        console.log(id);
        if(id != ''){
            $.ajax({
                url:"http://localhost:8000/loadmailhod",
                method:'GET',
                data : {id:id},
                success:function(data){
                    $('#id_hodemail').html(data);
                    console.log(data)
                }
            });
        }
    });

    $('#id_directorapproval').change(function(){
        var id = $('#id_directorapproval').val();
        console.log(id);
        if(id != ''){
            $.ajax({
                url:"http://localhost:8000/loadmaindirector",
                method:'GET',
                data : {id:id},
                success:function(data){
                    $('#id_dremail').html(data)    
                }
            });
        }
    });

});
