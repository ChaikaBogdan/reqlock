import { getAxios } from "./api.js"
import { AUTH_STORAGE_KEY } from "./constants.js"
import queryString from 'query-string'

export const loadAuth = history => dispatch => {
  console.info("Loading auth")
  const auth = JSON.parse(localStorage.getItem(AUTH_STORAGE_KEY) || "{}")
  const { token } = auth
  if (token) {
    const apiURL = "/dj-rest-auth/token/verify/"
    const axious = getAxios(dispatch)
      .post(apiURL, {token})
      .then(() => {
        dispatch({ type: "SET_AUTH", payload: auth })
        dispatch({ type: "SET_LOADED" })
        console.info("Loaded auth")
      }).catch(() =>{
        localStorage.removeItem(AUTH_STORAGE_KEY)
        dispatch({ type: "SET_LOADED", payload: auth })
      })
  } else {
    localStorage.removeItem(AUTH_STORAGE_KEY)
    dispatch({ type: "SET_LOADED", payload: auth })
  }
}

export const logout = history => dispatch => {
  console.info("Logging out")
  const apiUrl = "/dj-rest-auth/logout/"
  getAxios(dispatch)
    .post(apiUrl)
    .then(() => {
      localStorage.removeItem(AUTH_STORAGE_KEY)
      dispatch({ type: "SET_AUTH", payload: {}})
      history.push('/')
      console.info("Logged out")
      dispatch({ type: "SET_MESSAGE", payload: {body: "You succesfully logged out", variant: "success"}})
    })
}

export const login = (values, setFormErrors, location, history) => dispatch => {
  console.info("Logging in")
  const apiURL = '/dj-rest-auth/login/'
  getAxios(dispatch)
    .post(apiURL, values)
    .then(({ data }) => {
      const { access_token: token, user } = data
      const { username, email } = user
      const auth = { token, username, email }
      localStorage.setItem(AUTH_STORAGE_KEY, JSON.stringify(auth))
      dispatch({ type: "SET_AUTH", payload: auth })
      const { search } = location
      const { next } = queryString.parse(search)
      const redirect = next ? next : "/"
      console.log(search, next, redirect)
      history.push(redirect)
      console.info("Logged in")
      dispatch({ type: "SET_MESSAGE", payload: {body: "You succesfully logged in", variant: "success"}})
    })
    .catch(({ response }) => {
      const { data } = response || {}
      const {non_field_errors: nonFieldsErrors, ...fieldsErrors } = data || {}
      if (nonFieldsErrors) {
        const body = nonFieldsErrors.join(',')
        dispatch({ type: "SET_MESSAGE", payload: {body, variant: "danger"}})
      }
      fieldsErrors && setFormErrors(fieldsErrors)
    })
}

export const register = (values, setFormErrors, history) => dispatch => {
  console.info("Registering")
  const apiURL = "/dj-rest-auth/registration/"
  getAxios(dispatch)
    .post(apiURL, values)
    .then(() => {
      history.push("/signin")
      dispatch({ type: "SET_MESSAGE", payload: {body: "Please log in with sign up email and password", variant: "success"}})
      console.info("Registered")
    })
    .catch(({ response }) => {
      const { data } = response
      data && setFormErrors(data)
    })
}
