window.onload = function() {

    function initEventDeliveryChange() {

        let deliveryType = document.getElementById('id_deliveryType');

        deliveryType.addEventListener('change',radioButtonChange,false);


        function radioButtonChange() { 
            let radioButtons = this.getElementsByTagName('input');
    
            for(let i =0; i< radioButtons.length;i++) {
                if(radioButtons[i].checked === true) {
                    let delivery = document.querySelectorAll("select[name='delivery']")[0];
                    let  address = document.querySelectorAll("input[name='address']")[0];
                    address.style.display = "none";
                    delivery.style.display = 'block';
                    delivery.setAttribute("required","");
                    address.removeAttribute("required");
                } else {
                    let delivery = document.querySelectorAll("select[name='delivery']")[0];
                    let address = document.querySelectorAll("input[name='address']")[0];
                    address.style.display = "block";
                    delivery.style.display = 'none';
                    address.setAttribute("required","");
                    delivery.removeAttribute("required");
                    
                }
            }
        }
    }
    function initEventShowOrders() {
        let showOrders = document.getElementsByClassName('checkout-orders__show-wrapper')[0];
        
        showOrders.addEventListener('click', showOrdersClick, false);

        var rotate = 0;
        var clicked = true;
        
        
        function showOrdersClick() {  
            rotate += 180;
            let rotateString = 'rotate('+rotate+'deg)';
            this.getElementsByClassName('checkout-orders__show')[0].style.transform = rotateString;
            let orders = document.getElementsByClassName("checkout-orders")[0];
            
            if(clicked) {
                orders.style.display = 'block'
            } else {
                orders.style.display = 'none'
            }

            clicked = !clicked;
        }
    }
    
    initEventShowOrders();
    initEventDeliveryChange();

};