import React, { useState, useEffect, useContext } from "react"
import { useHistory } from "react-router-dom"
import { UncontrolledDiagram } from "./Diagram.jsx"
import { AppContext } from "./AppContext.jsx"
import { getAxios } from "../api.js"


export const Projects = () => {
  const [state, dispatch] = useContext(AppContext)
  const [projects, setProjects] = useState([])
  const history = useHistory()
  const { auth } = state
  const { token } = auth
  useEffect(() => {
    const projectsUrl = "/api/projects/"
    getAxios(dispatch, token, history)
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
