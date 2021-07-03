import React, { useContext } from "react"
import { Alert, Button } from "react-bootstrap"
import { AppContext } from "./AppContext.jsx"

export const DismissableAlert = () => {
  const [state, dispatch] = useContext(AppContext)
  const { message } = state
  const { title, body, variant } = message
  const show = Boolean(body && variant)
  if (!show) {
    return null
  }
  const onClick = () => dispatch({ type: "SET_MESSAGE", payload: {} })
  return (
    <Alert show={true} variant={variant}>
     {title && <Alert.Heading>{title}</Alert.Heading>}
      <p>{body}</p>
      <div className="d-flex justify-content-end">
        <Button onClick={onClick} variant={variant}>
          OK
        </Button>
      </div>
    </Alert>
  )
}
