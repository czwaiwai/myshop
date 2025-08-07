
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
}
const instance = axios.create(config)
instance.interceptors.request.use(function(config) {
    config.headers['X-CSRFToken'] = getCookie(CSRF)
    return config
})
instance.interceptors.response.use(function(response) {
    console.log(response)
    let {data} = response
    if (data.success) {
        return data
    }
    let {msg, errors} = data
    let obj = JSON.parse(errors)
    return data
}, function (err) {
    return Promise.reject(err)
})

window.$http = instance

htmx.on('htmx:configRequest', function(event) {
    event.detail.headers['X-CSRFToken'] = getCookie(CSRF)
})