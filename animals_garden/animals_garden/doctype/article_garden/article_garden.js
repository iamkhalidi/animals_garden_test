// Copyright (c) 2024, khalid and contributors
// For license information, please see license.txt


frappe.ui.form.on("Article_Garden", {


    
	before_save: function(frm) {
        let articleCost = parseInt(frm.doc.article_cost);
        let ticketDeliveryCost = parseInt(frm.doc.ticket_delivery_cost);

        let totalCost = articleCost + ticketDeliveryCost;

        frm.set_value("total_cost", totalCost);
        
    }

    
});