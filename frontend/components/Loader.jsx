import React, { useEffect } from "react"
import { useHistory } from "react-router-dom"
import { Spinner } from "react-bootstrap"
import { loadAuth } from "../actions.js"
import { useSelector, useDispatch } from "react-redux"

export const Loader = ({ children }) => {
  const dispatch = useDispatch()
  const history = useHistory()
  const { isLoaded } = useSelector((state) => state.auth)
  useEffect(() => dispatch(loadAuth(history)), [])
  if (isLoaded) {
    return <>{children}</>
  }
  return <Spinner animation="border" />
}
