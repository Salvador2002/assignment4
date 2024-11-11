"use strict";

// This will be the object that will contain the Vue attributes and be used to initialize it.
let app = {};

app.data = {    
    data: function() {
        return {
            contacts: [], // Array to hold contact card data
        };
    },
    methods: {
        addContact() {
            // Add a new empty contact with a placeholder image
            this.contacts.push({
                name: '',
                affiliation: '',
                description: '',
                photo: 'https://bulma.io/assets/images/placeholders/96x96.png', // Default image
            });
        },
        deleteContact(index) {
            // Delete the contact at the specified index
            this.contacts.splice(index, 1);
        },
        updatePhoto(event, contact) {
            // Handle the image upload and update the photo field
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    contact.photo = e.target.result; // Update the photo with the image data URL
                };
                reader.readAsDataURL(file);
            }
        },
    },
};

app.vue = Vue.createApp(app.data).mount("#app");

app.load_data = function () {
    // Initial data loading logic can be implemented here if needed
};

app.load_data();
