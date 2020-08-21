// static/main.js
console.log("Sanity check!");

// Get Stripe publishable key
fetch("/config/")
    .then((result) => {
        return result.json();
    })
    .then((data) => {
        // Initialize Stripe.js
        const stripe = Stripe(data.publicKey);

        // new
        // Event handler
        document.querySelector("#submitBtn").addEventListener("click", () => {
            // Get Checkout Session ID
            var quantity = document.getElementById("quantity").value;
            // var data = { 'quantity_test' : quantity };
            // var data = quantity
            fetch("/create-checkout-session/" + quantity + "/", {
                                                                  // method: 'POST', // or 'PUT'
                                                                  // // headers: {
                                                                  // //   'Content-Type': 'application/json',
                                                                  // // },
                                                                  // body: JSON.stringify(data),
                                                                })
                .then((result) => {
                    return result.json();
                })
                .then((data) => {
                    console.log(data);
                    // Redirect to Stripe Checkout
                    return stripe.redirectToCheckout({
                        sessionId: data.sessionId
                    })
                })
                .then((res) => {
                    console.log(res);
                });
        });
    });
