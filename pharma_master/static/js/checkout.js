$(document).ready(function (){
    $('.paywithrazorpay').click(function (e){
         e.preventDefault();
         console.log("hai")

         var fname=$("[name='c_fname']").val();
         var lname=$("[name='c_lname']").val();
         var address=$("[name='c_address']").val();
         var email=$("[name='c_email_address']").val();
         var phone=$("[name='c_phone']").val();
         console.log(fname)
         if(fname == "" || lname == "" || address == "" || email == "" || phone == "")
         {
//          Swal.fire('Alert!','all fields are mandatory','error');
//          return false;
            console.log("all fields are mandatory")

         }
         else
         {

         $.ajax({
            method: "GET",
            url: "/proceed-to-pay",
            success: function (response){
//                 console.log(response);

         var options = {
    "key": "rzp_test_TuXjYdjKmLjUZJ", // Enter the Key ID generated from the Dashboard
    "amount": response.total_price, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
    "currency": "INR",
    "name": "Pharma Store", //your business name
    "description": "Thank You Buying From Us",
    "image": "https://example.com/your_logo",
//    "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
    "handler": function (response){
        alert(response.razorpay_payment_id);
        alert(response.razorpay_order_id);
        alert(response.razorpay_signature)
    },
    "prefill": { //We recommend using the prefill parameter to auto-fill customer's contact information, especially their phone number
        "name": fname+""+lname, //your customer's name
        "email": email,
        "contact": phone  //Provide the customer's phone number for better conversion rates
    },
    "theme": {
        "color": "#3399cc"
    }
};
    var rzp1 = new Razorpay(options);

    rzp1.open();


            }

         });

         }

    });
});

