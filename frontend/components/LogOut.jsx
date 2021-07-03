import React, { useEffect, useContext } from "react"
import { useHistory } from "react-router-dom"
import { AppContext } from "./AppContext.jsx"
import { logout } from "../actions.js"

export const LogOut = () => {
  const [state, dispatch] = useContext(AppContext)
  const history = useHistory()
  useEffect(() => dispatch(logout(history)), [])
  return null
}
