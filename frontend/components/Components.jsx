import React, { useState, useEffect } from "react"
import { useHistory } from "react-router-dom"
import { useLocation } from "react-router"
import { UncontrolledDiagram } from "./Diagram.jsx"
import { getAxios } from "../api.js"
import { useSelector, useDispatch } from "react-redux"
import { Button, Form, Col, InputGroup } from "react-bootstrap"

export const Components = () => {
  const dispatch = useDispatch()
  const [components, setComponents] = useState([])
  const history = useHistory()
  const { pathname } = useLocation()
  const { auth } = useSelector((state) => state.auth)
  const { token } = auth
  useEffect(() => {
    const componentsUrl = "/api/components/"

    if (history && !token) {
      history.push({
        pathname: "/signin",
        search: `?next=${pathname}`,
      })
      dispatch({
        type: "SET_MESSAGE",
        payload: {
          title: "Unathorized",
          body: "Please log in first",
          variant: "warning",
        },
      })
      return
    }
    getAxios(dispatch, token)
      .get(componentsUrl)
      .then(({ data }) => setComponents(data))
  }, [])
  const nodes = components.map((component) => {
    return {
      id: component.id.toString(),
      content: component.name,
      coordinates: [100, 100],
    }
  })

  const componentsSchema = {
    nodes,
    links: [],
  }

  if (components && components.length) {
    return (
      <>
        <UncontrolledDiagram initialSchema={componentsSchema} />
        <Button variant="primary">Add Component</Button>
      </>
    )
  }
  return null
}
