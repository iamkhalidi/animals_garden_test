
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
							<h5 class="card-title">Article Count</h5>
							<h1 id="article-count"></h1>     <!-- use the id below to fill this with data -->

						</div>
						</div>

						
				</div>


				<div class="col-md-4">
							<h3> This is itme two   </h3>
						</div>

			</div>
		</div>


		`;

		let articleCount = function(){
			frappe.call({
				method: "animals_garden.animals_garden.page.custom_page.custom_page.get_article_count", // write dotted path
				callback: function(articleCount){
					console.log(articleCount);
					$("#article-count").text(articleCount.message) // #article-count is id for tag above 
				}
			});
		}


		$(frappe.render_template( htmlContent, this)).appendTo(this.page.main);  

		articleCount();
	
	}
})