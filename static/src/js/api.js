src="https://widget.northeurope.cloudapp.azure.com:9443/v0.1.0/mobile-money-widget-mtn.js"
    https://widget.northeurope.cloudapp.azure.com:9443/demo.html; 
        src="TODO_REPLACE_WITH_PRODUCTION_PATH"
            var element = document.getElementById("myapimtn");
            element.setAttribute("data-amount", 2000);
                var element1 = document.getElementById("myapimtn");
                   element1.addEventListener("mobile-money-qr-payment-created", function (event) {
                   console.log("Invoice:", event.detail);
                   }); 
               