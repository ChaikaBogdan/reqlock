import React from "react"
import { Alert, Button } from "react-bootstrap"
import { useSelector, useDispatch } from "react-redux"
import { SET_MESSAGE } from "../auth"

export const DismissableAlert = () => {
  const dispatch = useDispatch()
  const { message } = useSelector((state) => state.auth)
  const { title, body, variant } = message
  const show = Boolean(body && variant)
  if (!show) {
    return null
  }
  const onClick = () => {
    dispatch(SET_MESSAGE({}))
  }
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
