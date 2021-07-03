import React, { useState, useEffect, useContext } from "react"
import { useHistory } from "react-router-dom"
import { useLocation } from 'react-router'
import { UncontrolledDiagram } from "./Diagram.jsx"
import { AppContext } from "./AppContext.jsx"
import { getAxios } from "../api.js"

export const Projects = () => {
  const [state, dispatch] = useContext(AppContext)
  const [projects, setProjects] = useState([])
  const history = useHistory()
  const { pathname } = useLocation()
  const { auth } = state
  const { token } = auth
  useEffect(() => {
    const projectsUrl = "/api/projects/"
    if (history && !token) {
      history.push({
        pathname: "/signin",
        search: `?next=${pathname}`
      })
      dispatch({ type: "SET_MESSAGE", payload: {title: "Unathorized", body: "Please log in first", variant: "warning"}})
      return
    }
    getAxios(dispatch, token)
      .get(projectsUrl)
      .then(({ data }) => setProjects(data))
    }, [])
  const projectsSchema = {
    nodes: projects.map((project) => ({
      id: project.id.toString(),
      content: project.name,
      coordinates: [100, 100],
    })),
  }
  if (projects && projects.length) {
    return <UncontrolledDiagram initialSchema={projectsSchema} />
  }
  return null
}
