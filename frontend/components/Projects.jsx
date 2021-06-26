import React, { useState, useEffect } from "react"
import { UncontrolledDiagram } from "./Diagram.jsx"
import { BACKEND_URL } from "../constants.js"
import axios from "axios"
import { useHistory } from "react-router-dom"

const apiUrl = `${BACKEND_URL}/api`

export const Projects = () => {
  const [projects, setProjects] = useState([])
  const history = useHistory();

  useEffect(() => {
    const auth = JSON.parse(localStorage.getItem('auth') || '{}')
    const {token} = auth
    if (!token) {
      history.push('/signin')
      return null
    }
    const config = {
      headers: { Authorization: `Bearer ${token}` }
    }
    axios
    .get(`${apiUrl}/projects/`, config)
    .then(({data}) => setProjects(data))
    .catch(error => console.error(error));
  }, [])

  const projectsSchema = {
    nodes: projects.map(project => ({
      id: project.id.toString(),
      content: project.name,
      coordinates: [100, 100],
    })),
  }
  if (projects.length) {
    return <UncontrolledDiagram initialSchema={projectsSchema} />
  }
  return null
}
