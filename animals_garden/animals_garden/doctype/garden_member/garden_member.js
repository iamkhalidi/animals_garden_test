// Copyright (c) 2024, khalid and contributors
// For license information, please see license.txt


frappe.ui.form.on("Garden Member", {

    // 


    last_name: function(){
        let fName = frm.dmyMessageoc.first_name;
        let lName = frm.doc.last_name;
        frm.set_value("full_name", fName + " " + lName);
        },
    first_name: function(frm){
        let fName= frm.doc.first_name;
        let lName= frm.doc.last_name;
        frm.set_value("full_name", fName + " " + lName);
        },





	refresh: function(frm) {

        frm.add_custom_button('Create Membership', () => {
            frappe.new_doc('Garden Membership', {
                garden_member: frm.doc.name
            });
            console.log(frm);
        },"Second Action"
    ),

        frm.add_custom_button('Create Workspace', () => {
            frappe.new_doc('Workspace', {});
            console.log(frm);
        },"Second Action"
    ),
    
        frm.add_custom_button("frist button", function(){
            let myMessage = 'clicked first button';
            frappe.msgprint(myMessage);
        },'my custom action'
    ),
        frm.add_custom_button("Print Your Information", function(){
            let memberName = frm.doc.full_name;
            let memberEmail = frm.doc.email_address;
            frappe.msgprint(`your name is ${memberName}, ${memberEmail}`);
            console.log(`${memberName}, ${memberEmail}`);
        }, 'my custom action'
    ),
        frm.add_custom_button("button three", function() {
            frappe.prompt('fill your number here:', ({value}) => {
                if(value){
                    frm.set_value('phone', value);
                    frm.refresh_field('phone');
                    frappe.msgprint('Phone number added successfully.');
                    frappe.msgprint(`and it is ${frm.doc.phone}`);
                }
            });
        }, 'my custom action'
    ),

        frm.add_custom_button("print all members", function(){
            frappe.call({
                method:
                "animals_garden.animals_garden.doctype.garden_member.api.get_all_members",
                callback: function(r) {
                    console.log(r);
                }
            });
            
        }, 'my custom action'
    ),
        frm.add_custom_button("if members empty do else!", function() {
            frappe.call({
                method: 
                "animals_garden.animals_garden.doctype.garden_member.api.get_all_members",
                callback: function(mbrs){
                    console.log(typeof mbrs); 
                    if(mbrs) { 
                        console.log(mbrs);
                    } else {    
                        console.log('no data found');
                    }
                }
            }
        )
        }, "Second Action"
    ),
        frm.add_custom_button('get member by id', function() {
            frappe.call({
                method: 
                "animals_garden.animals_garden.doctype.garden_member.api.get_member",
                callback: function(d){
                    console.log('test get_member function')
                    console.log(d);
                }
            })
        
        }, "Second Action"
    );
    
	},
});

