import React, { useEffect, useContext } from "react"
import { useHistory } from "react-router-dom"
import { UncontrolledDiagram } from "./Diagram.jsx"
import { Spinner } from "react-bootstrap"
import { AppContext } from "./AppContext.jsx"
import { loadAuth } from "../actions.js"

export const Loader = ({ children }) => {
  const [state, dispatch] = useContext(AppContext)
  const history = useHistory()
  const { isLoaded } = state
  useEffect(() => dispatch(loadAuth(history)), [])
  if (isLoaded) {
    return (<>{children}</>)
  }
  return (
    <Spinner animation="border" />
  )
}
