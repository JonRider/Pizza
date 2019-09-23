document.addEventListener('DOMContentLoaded', function() {

   // Pizza Modal Script
   var modal = document.querySelector("#pizza-modal");
   var triggers = document.querySelectorAll(".add");
   // Toppings Order Button
   var orderToppings = document.querySelector("#order");

   // Sub Modal Script
   var subModal = document.querySelector("#sub-modal");
   var subTriggers = document.querySelectorAll(".sub-add");


   // Global Toppings count
   var count = 0;
   var allowedToppings = 0;

   // Get number of toppings allowed
   function getNumber(toppingNumber) {
     // Cheese (0) is already handled by Django Template
     if(toppingNumber == "Special") {
       return 5;
     }
     else if (toppingNumber == "Cheese") {
       return 0;
     }
     else if (toppingNumber == "1 Topping" || toppingNumber == "1 Item") {
       return 1;
     }
     else if (toppingNumber == "2 Toppings" || toppingNumber == "2 Items") {
       return 2;
     }
     else {
       return 3;
     }
   }

   // Setup Checkboxes div to call tally
   document.querySelector('#checkboxes').addEventListener('change', tally);
   // Tally number of current checked checkboxes
   function tally() {
     count = document.querySelectorAll('#checkboxes input[type="checkbox"]:checked').length;
     console.log(count);
     // enable submit button if toppings number is right
     if(count == allowedToppings) {
       orderToppings.disabled = false;
     }
     else {
       orderToppings.disabled = true;
     }
   }

   // Get infor about the pizza order. Pizza type and id number then display in modal
   function getOrder(type, id, toppingNumber) {
     let pizzaType = document.querySelector("#pizza-type");
     let pizzaID = document.querySelector("#pizza-id");
     let toppingLabel = document.querySelector("#toppings");
     // Get and Show topping number
     allowedToppings = getNumber(toppingNumber);
     pizzaType.value = type;
     pizzaID.value = id;
     toppingLabel.innerText = "Choose " + allowedToppings + " toppings"
     if(allowedToppings == 1) {
       toppingLabel.innerText = "Choose " + allowedToppings + " topping"
     }
     // Show the modal with given info
     modal.classList.toggle("show-modal");
   }

   // Get Sub Toppings and Details
   function getSub(id) {
     // Get what sub we are looking at and add it to the sub-ids value
     let subID = document.querySelector("#sub-id");
     subID.value = id;

     // Get steak div
     let steak = document.querySelector("#steak");
     // Is it a steak? ID's 17, 18, 19 and 20
     console.log(id);
     if(id > 16 && id < 21) {
       steak.style.visibility = 'visible';
     }
     else steak.style.visibility = 'hidden';
     // Show the modal with given info
     subModal.classList.toggle("show-modal");
   }

   // Add event listeners to each pizza button which requires more options
   triggers.forEach(function (e) {
     e.onclick = function () {
       let type = e.firstChild.value;
       let id = e.id;
       let toppingNumber = e.firstChild.name;
       getOrder(type, id, toppingNumber);
     }
   });

   // Add event listeners to each sub button which gives more options
   subTriggers.forEach(function (e) {
     e.onclick = function () {
       let id = e.id;
       getSub(id);
     }
   });


});
