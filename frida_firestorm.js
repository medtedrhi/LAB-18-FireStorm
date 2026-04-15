Java.perform(function() {
    function getPassword() {
        console.log("[*] Searching for MainActivity instances...");
        Java.choose('com.pwnsec.firestorm.MainActivity', {
            onMatch: function(instance) {
                try {
                    var pass = instance.Password();
                    console.log("[+] Generated Firebase Password: " + pass);
                } catch (e) {
                    console.log("[-] Error calling Password(): " + e);
                }
            },
            onComplete: function() {
                console.log("[*] Instance search complete.");
            }
        });
    }
    setTimeout(getPassword, 3000); // Wait for native library to load
});
