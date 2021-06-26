import React, { useState, useEffect } from "react"
import { UncontrolledDiagram } from "./Diagram.jsx"
import { BACKEND_URL } from "../constants.js"
import axios from "axios"
import { useHistory } from "react-router-dom"

export const Projects = () => {
  const projectsUrl = `${BACKEND_URL}/api/projects/`
  const verifyUrl = `${BACKEND_URL}/dj-rest-auth/token/verify/`
  const [projects, setProjects] = useState([])
  const history = useHistory();

  useEffect(() => {
    const auth = JSON.parse(localStorage.getItem('auth') || '{}')
    const {token} = auth
    if (!token) {
      history.push('/signin')
      return
    }
    axios
    .post(verifyUrl, {token: token})
    .then(() => {
      console.info('Valid user token')
      const config = {
        headers: { Authorization: `Bearer ${token}` }
      }
      axios.get(projectsUrl, config)
      .then(({data}) => setProjects(data))
      .catch(error => console.error(error))
    }).catch(() => {
      console.error('Invalid user token')
      history.push('/logout')
      return
    })
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
