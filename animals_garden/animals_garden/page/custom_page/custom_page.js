
frappe.pages['custom-page'].on_page_load = function(wrapper) {
	new PageContent(wrapper); // just initialize it


}


PageContent = Class.extend({
	init: function(wrapper){
		 this.page = frappe.ui.make_app_page({ //             make var this. , in py self , to recognize it 
			parent: wrapper,
			title: 'custom page',
			single_column: true
		}); //               this func must be here instead of above this more better place

		this.make(); //       this trigger the above function with the below make func

	}, //                takes the whole page


	make: function() {
		// html content - css - js
		
		let htmlContent = `

		<h2> This is our page </h2>
		<h3> This is our page </h3>
		<h4> This is our page </h4>




		`;


		$(frappe.render_template( htmlContent, this)).appendTo(this.page.main);  
	
	}
})