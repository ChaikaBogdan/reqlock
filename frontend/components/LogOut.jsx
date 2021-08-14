import React, { useEffect } from "react"
import { useHistory } from "react-router-dom"
import { logout } from "../actions.js"
import { useDispatch } from "react-redux"

export const LogOut = () => {
  const dispatch = useDispatch()
  const history = useHistory()
  useEffect(() => dispatch(logout(history)), [])
  return null
}
