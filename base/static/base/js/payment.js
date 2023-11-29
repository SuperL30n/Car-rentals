const paymentForm = document.getElementById('paymentForm');
paymentForm.addEventListener("submit", payWithPaystack, false);

function payWithPaystack(e) {
  e.preventDefault();

  let handler = PaystackPop.setup({
    key: 'pk_test_5866756b7c065aeb25ae40e0d0ae360e0defbd99', // Replace with your public key
    // email: document.getElementById("email-address").value,
    email: 'davidisaac081@gmail.com',
    // amount: document.getElementById("amount").value * 100,
    amount: 200 * 100,
    ref: ''+Math.floor((Math.random() * 1000000000) + 1), // generates a pseudo-unique reference. Please replace with a reference you generated. Or remove the line entirely so our API will generate one for you
    // label: "Optional string that replaces customer email"
    onClose: function(){
      alert('Window closed.');
    },
    callback: function(response){
    let server_url = 'http://'+window.location.host
    window.location.href = server_url+'/payment/'+id
    // let message = 'Payment complete! Reference: ' + response.reference;
    // alert(server_url+'/verify/')
    data = {
        ref:response.reference
    }
    //   window.location.replace(server_url+'/verify/');
      
        
    }
  });

  handler.openIframe();
}