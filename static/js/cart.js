// get add to cart button clicks
var updateBtns = document.getElementsByClassName('add-to-cart');
for (let i=0;i<updateBtns.length;i++) {
    updateBtns[i].addEventListener('click', function() {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productId:', productId, 'action:', action);
        console.log('USER:', user);
        if (user === 'AnonymousUser') {
            console.log('User is not authenticated');
        } else {
            console.log("I was clicked");
            // updateUserOrder(productId, action);
        }
    });
}



// for (let i=0;i<updateBtns.length;i++) {
//     updateBtns[i].addEventListener('click', function() {
//         var productId = this.dataset.product;
//         var action = this.dataset.action;
//         console.log('productId:', productId, 'action:', action);
//         console.log('USER:', user);
//         if (user === 'AnonymousUser') {
//             console.log('User is not authenticated');
//         } else {
//             updateUserOrder(productId, action);
//         }
//     });
// }
