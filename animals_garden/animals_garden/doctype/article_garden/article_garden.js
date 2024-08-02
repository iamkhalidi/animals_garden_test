// Copyright (c) 2024, khalid and contributors
// For license information, please see license.txt


frappe.ui.form.on("Article_Garden", {




    // lesson 4 advanced 
    refresh: function(frm) {
        frm.add_custom_button("Get Owner Articles", () => {
            let owner = frm.doc.owner1 ;
            let publisher = frm.doc.publisher ;

            
            frappe.call({
                method: "animals_garden.utils.get_owner_articles",
                args: {
                    owner1: owner,
                    // if you do this it means that you will take the arg value from the current doc
                    // when the parameter in get_owner_articles( owner= None )
                    publisher: publisher
                },
                callback: function(articles) {
                    console.log(articles)
                }
            })
        }, "Action");
    },


 













	before_save: function(frm) {
        let articleCost = parseInt(frm.doc.article_cost);
        let ticketDeliveryCost = parseInt(frm.doc.ticket_delivery_cost);

        let totalCost = articleCost + ticketDeliveryCost;

        frm.set_value("total_cost", totalCost);
        
    }

    
});