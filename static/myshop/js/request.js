
const CSRF = 'csrftoken'
function getCookie(name) {
  const cookiePair = document.cookie
    .split(";")
    .find((row) => row.trim().startsWith(`${name}=`));
  return cookiePair ? decodeURIComponent(cookiePair.split("=")[1]) : null;
}
const config = {
    baseURL: '/',
    timeout: 30000,
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
}
const instance = axios.create(config)
instance.interceptors.request.use(function(config) {
    Alpine && Alpine.store('loading').show()
    config.headers['X-CSRFToken'] = getCookie(CSRF)
    return config
})
instance.interceptors.response.use(function(response) {
    Alpine && Alpine.store('loading').hide()
    console.log(response)
    let {data} = response
    if (data.success) {
        return data
    }
    let {msg, errors} = data
    console.log(errors, '---')
    msg && Alpine.store('toast').show(msg)
    return data
}, function (err) {
    Alpine.store('loading').hide()
    let msg = err?.response?.data?.msg
    msg && Alpine.store('toast').show(msg)
    return Promise.reject(err)
})

window.$http = instance

htmx.on('htmx:configRequest', function(event) {
    event.detail.headers['X-CSRFToken'] = getCookie(CSRF)
})