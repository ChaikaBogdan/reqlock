import React, { useEffect } from "react"
import { BACKEND_URL } from "../constants.js"
import axios from "axios"
import { useHistory } from "react-router-dom"

export const LogOut = () => {
  const apiUrl = `${BACKEND_URL}/dj-rest-auth/logout/`
  const history = useHistory()

  useEffect(() => {
    axios
      .post(apiUrl)
      .then(res => {
        localStorage.removeItem('auth')
        console.info('Logout')
        history.push('/')
      })
      .catch(error => console.error(error))
  }, [])

  return null
}
