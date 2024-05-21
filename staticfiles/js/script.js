console.log('Its working')

let theme = localStorage.getItem('theme')

if(theme == null){
	setTheme('light')
}else{
	setTheme(theme)
}

let themeDots = document.getElementsByClassName('theme-dot')


for (var i=0; themeDots.length > i; i++){
	themeDots[i].addEventListener('click', function(){
		let mode = this.dataset.mode
		console.log('Option clicked:', mode)
		setTheme(mode)
	})
}
function setTheme(mode) {
    let themeStyle = document.getElementById('theme-style');

    if (mode == 'light') {
        themeStyle.href = staticURL + 'default.css';
    }

    if (mode == 'blue') {
        themeStyle.href = staticURL + 'blue.css';
    }

    if (mode == 'green') {
        themeStyle.href = staticURL + 'green.css';
    }

    if (mode == 'purple') {
        themeStyle.href = staticURL + 'purple.css';
    }

    localStorage.setItem('theme', mode);
}
