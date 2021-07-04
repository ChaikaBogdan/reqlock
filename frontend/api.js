import axios from "axios"
import { BACKEND_URL } from "./constants.js"
import { SET_MESSAGE } from "./auth"

export const getAxios = (dispatch, token, timeout = 30) => {
  const api = axios.create({
    baseURL: BACKEND_URL,
    timeout: timeout * 1000,
  })
  const errorHandler = (error) => {
    const { name, message } = error
    dispatch(SET_MESSAGE({ title: name, body: message, variant: "danger" }))
    return Promise.reject(error)
  }
  if (token) {
    api.interceptors.request.use((config) => {
      config.headers["Authorization"] = `Bearer ${token}`
      return config
    }, errorHandler)
  }
  api.interceptors.response.use((response) => response, errorHandler)
  return api
}
