function Confirmation(){
choice=confirm("Do you to delete this medicine ? ")
return choice
}

function PurchaseNumber(parseInt(id)){
let number=parseInt(prompt("Enter order count ",""));
window.location.href="add_wishlist/"+id+"/"+number
}

window.addEventListener( "pageshow", function ( event ) {
  var historyTraversal = event.persisted ||
                         ( typeof window.performance != "undefined" &&
                              window.performance.navigation.type === 2 );
  if ( historyTraversal ) {

    window.location.reload();
  }
});

