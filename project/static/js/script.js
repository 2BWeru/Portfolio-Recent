$(document).ready(function(){
    // submit contact form
    $('form#contact').submit(function(event){
        event.preventDefault();
        var nameInput = $('#name').val();
        var emailInput = $('#email').val();
        var message = $('#message').val();
        

        // if(!nameInput || !emailInput || !message){
        //     var errMsg= " Please fill the form to contact me ";
        //     $('.error-txt').text(errMsg);
        //     return;
        // }
        // else{
        //    $('error-txt').text('')
        // };

        if(nameInput || emailInput || message){
        $('.name-txt').append("Thank you  for your Message ,\n I will get back to you soon.");  
         $('.name-id').append(nameInput);
            $('#send').toggle();
            $('#send2').toggle();
        return;
        
        }
        else{
            $('.name-txt').text('');
        }
    });

});

  // video toggle
  function myFunction(){
    var x = document.getElementById("portfolio");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
  };