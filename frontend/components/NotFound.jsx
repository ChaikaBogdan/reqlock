import React, { useEffect } from "react";
import { notFound } from "../actions.js"
import { useHistory } from "react-router-dom"
import { useLocation } from "react-router"
import { useDispatch } from "react-redux"

export const NotFound = () => {
  const dispatch = useDispatch()
  const location = useLocation()
  const history = useHistory()
  useEffect(() => dispatch(notFound(location, history)), [])
  return null
}
