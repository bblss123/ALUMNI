function search_checkbox(id)
{
	var a = document.getElementById("search-keyword");
	b = a.value.search(id);
	a.value += " " + id;

}

function navigator_display(id)
{
	var sub_menu = document.getElementById(id);
	if(sub_menu.style.display == "none")
		sub_menu.style.display = "inline;
	else if(sub_menu.style.display == "inline")
		sub_menu.style.display = "none";

	if(id != "sub_all")
	 	document.getElementById("sub_all").style.display = "none";
	if(id != "sub_city")
		document.getElementById("sub_city").style.display = "none";
	if(id != "sub_career")
		document.getElementById("sub_career").style.display = "none";
	if(id != "sub_school")
		document.getElementById("sub_school").style.display = "none";
	if(id != "sub_year")
		document.getElementById("sub_year").style.display = "none";
	if(id != "sub_activity")
		document.getElementById("sub_activity").style.display = "none";
}

function refresh_post()
{
	var user_post = document.getElementById("posts_content");
	user_post.value = "Hi!";
}