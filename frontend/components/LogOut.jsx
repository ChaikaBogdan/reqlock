import React, { useEffect } from "react"
import { BACKEND_URL } from "../constants.js"
import axios from "axios"
import { useHistory } from "react-router-dom"

const logOutURL = `${BACKEND_URL}/dj-rest-auth/logout/`

export const LogOut = () => {
  const history = useHistory()

  useEffect(() => {
    axios
      .post(logOutURL)
      .then(res => {
        localStorage.removeItem('auth')
        console.info('Logout')
        history.push('/')
      })
      .catch(error => console.error(error));
  }, [])

  return null
}
