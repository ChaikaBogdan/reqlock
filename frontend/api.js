import axios from "axios"
import { BACKEND_URL } from "./constants.js"

export const getAxios = (dispatch, token, history, timeout = 30, propagateErrors = true) => {
  const api = axios.create({
    baseURL: BACKEND_URL,
    timeout: timeout * 1000,
  })
  const errorHandler = error => {
    const {name, message} = error
    propagateErrors && dispatch({ type: "SET_MESSAGE", payload: {title: name, body: message, variant: "danger"}})
    return Promise.reject(error)
  }
  if (token) {
    api.interceptors.request.use(
      config => {
        config.headers["Authorization"] = `Bearer ${token}`
        return config
      },
      errorHandler,
    )
  } else if (history) {
    history.push('/')
    propagateErrors && dispatch({ type: "SET_MESSAGE", payload: {title: "Unathorized", body: "Please log in first", variant: "warning"}})
  }
  api.interceptors.response.use(
    response => response,
    errorHandler,
  )
  return api
}
