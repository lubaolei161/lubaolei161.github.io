{% if not (theme.duoshuo and theme.duoshuo.shortname) and not theme.duoshuo_shortname and not (theme.disqus.enable and theme.disqus.shortname) and  not theme.gentie_productKey and not theme.changyan.enable %}
	{% if page.comments and theme.gitment.enable and theme.gitment.username and theme.gitment.client_id and theme.gitment.client_secret %}
	<div onclick="showGitment()" id="gitment_title" class="gitment_title">显示 Gitment 评论</div>
<div id="container" style="display:none"></div>
<link rel="stylesheet" href="https://imsun.github.io/gitment/style/default.css">
<script src="https://imsun.github.io/gitment/dist/gitment.browser.js"></script>
<script>
const myTheme = {
	render(state, instance) {
		const container = document.createElement('div');
		container.lang = "en-US";
		container.className = 'gitment-container gitment-root-container';
		container.appendChild(instance.renderHeader(state, instance));
		container.appendChild(instance.renderEditor(state, instance));
		container.appendChild(instance.renderComments(state, instance));
		container.appendChild(instance.renderFooter(state, instance));
		return container;
	}
}
function showGitment() {
	$("#gitment_title").attr("style", "display:none");
	$("#container").attr("style", "").addClass("gitment_container");
	var gitment = new Gitment({
		id: window.location.pathname,
		theme: myTheme,
		owner: '{{ theme.gitment.owner }}',
		repo: '{{ theme.gitment.repo }}',
		oauth: {
			client_id: '{{ theme.gitment.client_id }}',
			client_secret: '{{ theme.gitment.client_secret }}'
		}
	});
	gitment.render('container');
}
</script>
{% endif %}
{% endif %}
