import React, { useState, useEffect } from "react"
import { useHistory } from "react-router-dom"
import { useLocation } from "react-router"
import { UncontrolledDiagram } from "./Diagram.jsx"
import { getAxios } from "../api.js"
import { useSelector, useDispatch } from "react-redux"

export const Projects = () => {
  const dispatch = useDispatch()
  const [projects, setProjects] = useState([])
  const history = useHistory()
  const { pathname } = useLocation()
  const { auth } = useSelector((state) => state.auth)
  const { token } = auth
  useEffect(() => {
    const projectsUrl = "/api/projects/"
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
      .get(projectsUrl)
      .then(({ data }) => setProjects(data))
  }, [])
  const nodes = projects.map((project) => {
    return {
      id: project.id.toString(),
      content: project.name,
      coordinates: [100, 100],
    }
  })
  const links = projects.map((project) => {
    return project.linked_projects.map((linked_project) => {
      return {
        input: project.id.toString(),
        output: linked_project.id.toString(),
      }
    })
  })
  const projectsSchema = {
    nodes,
    links: links.flat(),
  }
  if (projects && projects.length) {
    return <UncontrolledDiagram initialSchema={projectsSchema} />
  }
  return null
}
