import { getAxios } from "./api.js"
import { AUTH_STORAGE_KEY } from "./constants.js"
import queryString from "query-string"
import { SET_AUTH, SET_MESSAGE, SET_LOADED } from "./auth"

export const loadAuth = history => (dispatch) => {
  console.info("Loading auth")
  const auth = JSON.parse(localStorage.getItem(AUTH_STORAGE_KEY) || "{}")
  const { token } = auth
  if (token) {
    const apiURL = "/dj-rest-auth/token/verify/"
    const axious = getAxios(dispatch)
      .post(apiURL, { token })
      .then(() => {
        dispatch(SET_AUTH(auth))
        dispatch(SET_LOADED())
        console.info("Loaded auth")
      })
      .catch(() => {
        localStorage.removeItem(AUTH_STORAGE_KEY)
        dispatch(SET_LOADED())
      })
  } else {
    localStorage.removeItem(AUTH_STORAGE_KEY)
    dispatch(SET_LOADED())
  }
}

export const logout = history => (dispatch) => {
  console.info("Logging out")
  const apiUrl = "/dj-rest-auth/logout/"
  getAxios(dispatch)
    .post(apiUrl)
    .then(() => {
      localStorage.removeItem(AUTH_STORAGE_KEY)
      dispatch(SET_AUTH({}))
      history.push("/")
      console.info("Logged out")
      dispatch(
        SET_MESSAGE({ body: "You succesfully logged out", variant: "success" })
      )
    })
}

export const login =
  (values, setFormErrors, location, history) => (dispatch) => {
    console.info("Logging in")
    const apiURL = "/dj-rest-auth/login/"
    getAxios(dispatch)
      .post(apiURL, values)
      .then(({ data }) => {
        const { access_token: token, user } = data
        const { username, email } = user
        const auth = { token, username, email }
        localStorage.setItem(AUTH_STORAGE_KEY, JSON.stringify(auth))
        dispatch(SET_AUTH(auth))
        const { search } = location
        const { next } = queryString.parse(search)
        const redirect = next ? next : "/"
        history.push(redirect)
        console.info("Logged in")
        dispatch(SET_MESSAGE({ body: "You succesfully logged in", variant: "success" }))
      })
      .catch(({ response }) => {
        const { data } = response || {}
        const { non_field_errors: nonFieldsErrors, ...fieldsErrors } =
          data || {}
        if (nonFieldsErrors) {
          const body = nonFieldsErrors.join(",")
          dispatch(SET_MESSAGE({ body, variant: "danger" }))
        }
        fieldsErrors && setFormErrors(fieldsErrors)
      })
  }

export const register = (values, setFormErrors, history) => (dispatch) => {
  console.info("Registering")
  const apiURL = "/dj-rest-auth/registration/"
  getAxios(dispatch)
    .post(apiURL, values)
    .then(() => {
      history.push("/signin")
      dispatch(
        SET_MESSAGE({
          body: "Please log in with sign up email and password",
          variant: "success",
        })
      )
      console.info("Registered")
    })
    .catch(({ response }) => {
      const { data } = response
      data && setFormErrors(data)
    })
}

export const notFound = (location, history) => (dispatch) => {
  const {pathname: notFoundURL} = location
  const notFoundMessage = `There is no such page - ${notFoundURL}`
  console.warn(notFoundMessage)
  history.push({
    pathname: "/",
  })
  dispatch(SET_MESSAGE({
    title: "Not found",
    body: notFoundMessage,
    variant: "warning",
  }))
}
