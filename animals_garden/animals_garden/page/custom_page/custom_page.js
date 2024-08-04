
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

		<div class="container"> 
			<div class="row">
				<div class="col-md-4">

					<div class="card">
						<div class="card-body">
							<h5 class="card-title">Card title</h5>
							<p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
							<a href="#" class="btn btn-primary">Go somewhere</a>
						</div>
						</div>

						
				</div>


				<div class="col-md-4">
							<h3>We are here </h3>
						</div>

			</div>
		</div>



		`;


		$(frappe.render_template( htmlContent, this)).appendTo(this.page.main);  
	
	}
})