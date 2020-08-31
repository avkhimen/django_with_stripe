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
            var data = { 'quantity' : quantity };
            fetch("/create-checkout-session/", {
                                                method: 'POST',
                                                headers: {'Content-Type': 'application/json'},
                                                body: JSON.stringify(data)})
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

        // new
        // Event handler
        document.querySelector("#submitCustomerRequestBtn").addEventListener("click", () => {
            // Get Checkout Session ID
            var name = document.getElementById("custName").value;
            var email = document.getElementById("custEmail").value;
            var issue = document.getElementById("custIssue").value;
            var text = document.getElementById("custText").value;
            var data = { 'name' : name, 'email' : email, 'issue' : issue, 'text' : text};
            fetch("/send-customer-request/", {
                                                method: 'POST',
                                                headers: {'Content-Type': 'application/json'},
                                                body: JSON.stringify(data)})
                .then((result) => {
                    return result.json();
                })
        });

    });