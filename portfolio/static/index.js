const forwarding = slug => {
	window.location.replace(`http://127.0.0.1:8000/home/${slug}`)
}

const btns = [...document.querySelectorAll('#langue')]
btns.forEach(btn =>
	btn.addEventListener('click', () => {
		const slug = btn.innerHTML
		forwarding(slug)
	})
)
